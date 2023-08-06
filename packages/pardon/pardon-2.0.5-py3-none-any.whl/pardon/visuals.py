import os, sys

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.model_selection import learning_curve
import plotly.express as px
import seaborn as sns
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype as is_datetime

from . import utility
from . import pardon_options


_LINEPLOT_ESTIMATORS = {'mean': np.mean, 'median': np.median, 'mode': utility.get_mode, 'count': np.count_nonzero, 'sum': np.sum, 'max': np.max, 'min': np.min, 'z_score': utility.get_z_score}


def create_learning_curve(model, x, y, intervals:list, cv, score_metric:str):
    '''
    Create and show the learning curve for the given model.

        Args:
            model : object
                The model object.
            x : pandas.DataFrame, numpy.array
                The x data to plot.
            y : pandas.DataFrame, pandas.Series, numpy.array
                The y data to plot.
            intervals : list
                A list containing the training interval sizes.
            cv : object
                A cross-validation object.
            score_metric : str
                Specify which metric is to be used when performing the cross-validation.
    '''
    # create the learning curves
    train_sizes, train_scores, test_scores = learning_curve(estimator=model, X=x, y=y, train_sizes=intervals, cv=cv, scoring=score_metric, n_jobs=-1, random_state=13, verbose=3)
    # get the mean for the train and test cross validations
    train_mean = np.mean(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    # get the train and test std as we will plot this
    train_std = np.std(train_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    # plot the chart
    plt.plot(train_sizes, train_mean, label='Training Score')
    plt.plot(train_sizes, test_mean, label='Cross-Validation Score')
    # specify the colour being used for the standard deviatiuon
    std_colour = '#DDDDDD'
    # add the std - this shows the upper and lower bounces
    plt.fill_between(train_sizes, train_mean-train_std, train_mean+train_std, color=std_colour)
    plt.fill_between(train_sizes, test_mean-test_std, test_mean+test_std, color=std_colour)
    try:
        # get the highest value and index
        best_test_score = max(test_mean)
        best_score_index = list(test_mean).index(best_test_score)
        best_train_size = train_sizes[best_score_index]
        plt.plot([best_train_size], [best_test_score], marker="o", markersize=10, markerfacecolor="green")
    except:
        raise Exception(f'Unable to build learning curve with score_metric {score_metric}, change the score_metric and try again.')
    # add the labels
    plt.xlabel(f'Data Size')
    plt.ylabel(f'{score_metric} Score')
    plt.title(f'{type(model).__name__} Model\nLearning Curve for {score_metric}')
    from matplotlib.patches import Patch
    # get the legend and add the standard deviation patch to the legend
    legend = plt.legend(loc='best')
    ax = legend.axes
    handles, labels = ax.get_legend_handles_labels()
    handles.append(Patch(facecolor=std_colour))
    labels.append("Standard Deviation")
    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())
    # add grid lines
    plt.grid()
    # specify the best performing score
    print(f'Best Cross-Validation Score: {round(best_test_score, 2)}')
    # show the chart
    plt.show()


def plot_map(data, target:str, lat:str, lon:str, c:str=None, size:str=None, as_prediction:bool=False):
    '''
    Plot data to a map.

        Args:
            data : pandas.DataFrame
                A pandas.DataFrame containing the data.
            target : str
                The target column (or y axis data).
            lat : str
                Specify which column will indicate latitude.
            lon : str
                Specify which column will indicate longitude.
            c : str, default None
                Specify which column will indicate marker colour scales.
            size : str, default None
                Specify which column will indicate marker sizes.
            as_prediction : bool, default False
                Set True if the data is showing a model's predictions.
    '''
    # plot to a map
    c_title = f'{c}{pardon_options.PREDICTED_COL_SUFFFIX}' if c == target and as_prediction else c

    

    # set the title
    title = f'Map showing data by {c_title}'

    # create the map object
    fig = px.scatter_mapbox(data, lat=lat, lon=lon, 
                            hover_name=c, hover_data=data.columns,
                            color=c, zoom=3, title=title, size=size, size_max=15)
    # set the map style
    fig.update_layout(mapbox_style="open-street-map")
    # set the map layout
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # show
    fig.show()


def plot_corr(data:pd.DataFrame, columns:list=[]):
    '''
    Plot the data correlation heatmap.

        Args:
            data : pandas.DataFrame
                A pandas.DataFrame containing the data.
            columns : list, default []
                The list of columns you want to be included in the correlation plot.
    '''

    if not isinstance(columns, list):
        columns = list(columns)
    # get the full column list
    columns = list(data.columns) if not columns else columns
    
    # make all the column values numeric
    for col in columns:
        labels = utility.get_labels(data=data[col])
        data = utility.map_col_labels(data=data, column=col, labels=labels)

    # create the correlation
    corr = data[columns].corr() if columns else data.corr()
    # set font scaling
    sns.set(font_scale=0.6)
    ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(20, 220, n=200), square=True, xticklabels=True, yticklabels=True, cbar_kws={'label': 'Correlation'})
    # set the axis labels
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right')

    plt.show()


def get_plot_marker_sizes(data:pd.Series, max_plot_size:int=100) -> pd.Series:
    '''
    Scale your data sizes for use with visuals to avoid them being too large on visualisations. The data must be numeric before using this feature.

        Args:
            data : pandas.Series
                A pandas.Series containing the data for a particular column.
            max_plot_size : int, default 100
                The maximum size of a data marker on your plot.

        Returns:
            (pandas.Series) : Returns a pandas.DataFrame with data scaled to the max plot size.
    '''
    # set the max_found
    max_found = max(data)
    # scale everything to MAX_PLOT_SIZE accordingly
    data = data.apply(lambda x: (x / max_found) * max_plot_size)
    return data


def _plot_hist(data, x, n_bins, target, as_prediction):
    # plot a histogram
    # set n_bins to auto if string supplied
    if isinstance(n_bins, str):
        n_bins = 'auto'

    # if we're using categorical data, set n_bins to be 1 for each class
    if not is_numeric_dtype(data[x]):
        n_bins = len(data[x].unique())

    # set the title start
    title = f'Histogram for {x}'  
    # add predicted
    if x == target and as_prediction:
        title += pardon_options.PREDICTED_COL_SUFFFIX

    plt.hist(x=data[x], color='tab:blue', edgecolor='black', bins=n_bins)

    # use this if titles required
    plt.title(title)
    plt.xlabel(x)
    plt.xticks(rotation=45)
    plt.margins(x=0.01, y=0.1)
    plt.ylabel('Count')
    plt.show()


def _plot_classes(data, classes, colours, target, x, y, size):
    # plot the classes with a legend
    _, ax = plt.subplots()
    # for each class, map the data of that class and add to the legend
    for i, class_ in enumerate(classes):
        size_val = data[data[target] == class_][size] if size is not None else None
        ax.scatter(x=data[data[target] == class_][x], y=data[data[target] == class_][y], color=colours[i], label=class_, s=size_val)

    # show the legend
    ax.legend(loc='upper right')


def _plot_colours(classes) -> list:
        # return the plot colours

    colours = [plt.cm.tab10(i/float(len(classes)-1)) for i in range(len(classes))]

    return colours


def _set_plt_ticks(x_labels:dict, y_labels:dict):
        # first check that all the labels are numeric - if they are, they do not need to be converted
        if x_labels is not None:
            if utility.all_numeric(x_labels.keys()):
                x_labels = None
        if y_labels is not None:
            if utility.all_numeric(y_labels.keys()):
                y_labels = None
        # set the plt ticks
        # set the x labels if we converted them to numeric
        if x_labels is not None:
            plt.xticks(ticks=range(len(x_labels)), labels=x_labels.keys())
        if y_labels is not None:
            plt.yticks(ticks=range(len(y_labels)), labels=y_labels.keys()) 


def _plot_scatter(data, x, y, c, size, classes, include_trendline, as_prediction, target, randomised_data=None, randomised_data_title=None):
    # plot the chart data
    # if using size
    if size is not None:
        # only use it on numeric
        if is_numeric_dtype(data[size]):
            data[size] = get_plot_marker_sizes(data=data[size], max_plot_size=100)
            # if necessary, assign data to the randmised dataset
            if randomised_data is not None:
                randomised_data[size] = get_plot_marker_sizes(data=randomised_data[size])
        else:
            print(f'*** WARNING: The {size} column is not numeric and so cannot be used for size. Size set to None ***')
            size = None

    # we want the data set in a list even if only 1
    data_sets = [data]

    # if using random, plot it side by side
    if randomised_data is not None:
        data_sets.append(randomised_data)

    # iterate through
    for i, data in enumerate(data_sets, start=1):
        
        # is this a randmosed iteration
        is_randomised = True if i == 2 or (len(data_sets) == 1 and randomised_data_title is not None) else False

        # determine the plot type
        x_numeric = is_numeric_dtype(data[x])

        # if dealing with dates, we have to make them strings first
        data[y] = data[y].astype(str) if is_datetime(data[y]) else data[y]
        data[x] = data[x].astype(str) if is_datetime(data[x]) else data[x]

        # get the y and x labels
        y_labels = utility.get_labels(data=data[y])
        x_labels = utility.get_labels(data=data[x])
        # set the datasets
        data = utility.map_col_labels(data=data, column=x, labels=x_labels)
        data = utility.map_col_labels(data=data, column=y, labels=y_labels)

        # add predicted if relevant
        x_title = f'{x}{pardon_options.PREDICTED_COL_SUFFFIX}' if x == target and (as_prediction or is_randomised) else x
        y_title = f'{y}{pardon_options.PREDICTED_COL_SUFFFIX}' if y == target and (as_prediction or is_randomised) else y
        c_title = f'{c}{pardon_options.PREDICTED_COL_SUFFFIX}' if c == target and (as_prediction or is_randomised) else c

        title = f'{x_title} and {y_title}'  
        # if using the second dataset, this is the randomised so change the title
        if is_randomised:
            randomised_data_title = '[randomised columns]' if randomised_data_title is None else randomised_data_title
            title += f' {randomised_data_title}' 

        # add the size element to the title if applicable
        title = title + f'\nSize by {size}' if size is not None else title

        # if not c, set the data
        if c is None:
            fig, ax = plt.subplots()
            s = None if size is None else data[size]
            plt.scatter(x=data[x], y=data[y], s=s, alpha=0.5)
        elif is_numeric_dtype(data[c]):
            fig, ax = plt.subplots()
            if size is not None:
                im = ax.scatter(x=data[x], y=data[y], c=data[c], s=data[size], alpha=0.5, cmap="RdYlGn")
            else:
                im = ax.scatter(x=data[x], y=data[y], c=data[c], alpha=0.5, cmap="RdYlGn")
            clb = fig.colorbar(im, ax=ax)
            clb.ax.set_title(c_title, fontdict={'fontsize': 8})
        else:
            # get the classes
            if c != target or classes is None:
                # if not using the targets, set the classes as the items found in the column
                classes = list(data[c].unique())
            # set colours
            colours = _plot_colours(classes=classes)
            # plot the classes and colours
            _plot_classes(data=data, classes=classes, colours=colours, target=c, x=x, y=y, size=size)

        # set the x labels if we converted them to numeric
        _set_plt_ticks(x_labels=x_labels, y_labels=y_labels)

        # add the trend line if requested
        if include_trendline:
            try:
                z = np.polyfit(data[x], data[y], 1)
                sc = np.squeeze(z)
                y_hat = np.poly1d(sc)(data[x])
                plt.plot(data[x], y_hat, "r--", lw=1)
                text = f'r2={round(sklearn.metrics.r2_score(data[y], y_hat), 3)}'
                plt.gca().text(0.05, 0.95, text, transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')
            # if we can't add a trendline for whatever reason, display a warning
            except np.linalg.LinAlgError:
                print(f'\nWARNING: Trendline could not be added. This may be due to zeroes in the data causing issues in division.\n')

        # add titles and x and y labels
        plt.title(title)
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        # if not using a numeric scale, rotate the text
        if not x_numeric:
            plt.xticks(rotation=45)

    plt.show()


def _plot_lineplot(data, x, y, c, size, target, as_prediction, lineplot_estimator):

    if not is_numeric_dtype(data[y]) and not is_datetime(data[y]):
        # set the labels and data for counting
        labels = utility.get_labels(data=data[y])
        data = utility.map_col_labels(data=data, column=y, labels=labels)
        # if we are not using numeric, set count
        if lineplot_estimator != 'count':
            lineplot_estimator = 'count'
            print(f'*** WARNING: lineplot_estimator set to count as dealing with non-numeric column: {y} ***')

    # ensure size is numeric if it is used
    if size is not None:
        if not is_numeric_dtype(data[size]):
            print(f'*** WARNING: The column {size} is not numeric so cannot be used for size. Size set to None ***')
            size = None

    # get the estimator
    estimator = _LINEPLOT_ESTIMATORS[lineplot_estimator]
    # style definition
    sns.set_theme(style="darkgrid")
    # create the line plot
    ax = sns.lineplot(data=data, x=x, y=y, hue=c, size=size, sizes=(1, 8), estimator=estimator, ci=None, markers=True, style=c)
    # set the title as x and y
    y_label = y
    x_label = x

    # add predicted
    if y == target and as_prediction:
        y_label += pardon_options.PREDICTED_COL_SUFFFIX
    if x == target and as_prediction:
        x_label += pardon_options.PREDICTED_COL_SUFFFIX

    # label the aggregator
    y_label = f'{y_label} ({lineplot_estimator})'

    # set axis titles
    ax.set(xlabel=x_label, ylabel=y_label)
    
    # set the c title on the legend if applicable
    if c is not None:
        c_label = c
        if c == target and as_prediction:
            c_label += pardon_options.PREDICTED_COL_SUFFFIX
        # set the legend title
        ax.legend().set_title(c_label)

    # set the main title
    title = f'Lineplot for {x_label} and {y_label}'  
    title = title + f'\nSize by {size}' if size is not None else title 

    plt.title(title)

    plt.show()