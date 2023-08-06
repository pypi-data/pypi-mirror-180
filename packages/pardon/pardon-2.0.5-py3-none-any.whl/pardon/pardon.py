import sys, os
import math
import re
from functools import wraps
import inspect
import collections
from datetime import datetime
import time

import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype, is_datetime64_any_dtype as is_datetime
import matplotlib.pyplot as plt
import shap
import sklearn
import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
from sklearn.model_selection import GridSearchCV, cross_validate, train_test_split
from sklearn import preprocessing
from sklearn.decomposition import PCA
import category_encoders
from scipy import stats
import neattext.functions as nfx
from schemdraw import flow, Drawing

from . import audits
from . import utility
from . import make_rules
from . import visuals
from . import pardon_models
from . import statics
from . import pardon_predict
from . import pardon_options
from . import pardon_encode
from . import pardon_transforms
from . import pickles
from . import config


pd.options.mode.chained_assignment = None 


class Pardon:
    """
    A class allowing data transformations, model training, visualisations, and predictions as well as prediction auditing.

        Args
            target : str, None, default None
                    The column name that we are attempting to predict. Note, the column name is case sensitive. If None, no Model methods will be available, but clusters can be created and plotted, data transformations performed, and data visualisations produced. See the create_clusters and plot_data methods.
            columns : list, default [] (empty list)
                    A list of columns that you want to include in your training. If not used, all columns found in the data will be used.
            encoding : str, default 'latin-1' {'latin-1' , 'ascii', 'utf-8'}
                    The encoding used when opening csv files.
            sep : str, default ','
                    The delimiter to use when opening csv or txt files.
            test_size : float, default 0.3
                    The proportion of the data to retain for model testing. 0.3 refers to 30%. Note, if the target is None, the test_size will be set to 0 and all data will be retained in the train_data attribute.
            remove_single_instance_classes : bool, default False
                    Remove the rows of classes that only contain a single instance of that class. Machine learning models require each class to have at least 2 instances for training. This is set to False as the default to ensure users know these rows are being removed. If they are not removed and a single instance is found in the data, the train_model method will fail.
            is_regression : bool, str, default 'infer' {True, False, 'infer'}
                    Determines if the model is a regression task or a classification task. If True the models used will be regression models, if False, classification models. 'infer' means this will attempt to be determined automatically by checking if the data is numeric and continuous in the target column.
            stratify : bool, default True
                    Use the same proportion of classes encountered in the dataset when splitting data into train and test. For example, if your data contains 5% instances of class A and 95% of class B, these proportions will be maintained in the train and test datasets.
            shuffle : bool, default True
                    Shuffle the dataset into a random order during the train/test split. If using time series data this should be set to False.
            yaml : str, default None
                    Reference to a yaml file containing configuration details. This will be saved as a dictionary object in the config attribute.
        
        Attributes:
            test_size
                The proportion of data being held for model testing.
            target
                The name of the column containing the classes or values being predicted.
            scaler_used
                The name of the type of scaler used. 
            model_trained_date
                The datetime the model finished training. 
            model
                The class object of the machine learning model used. These can be seen in the Available Models section.
            model_type
                The name of the model being used. Will present as the class name of the model classes listed in the model attribute.
            best_hyperparameters
                A dictionary object containing the model being tested and the best parameter values found during hyperparameter tuning with cross validation.
            validation_training_time_mins
                A dictionary object showing the time in minutes the hyperparameter tuning with cross validation took to complete for each model.
            model_training_time_mins
                The time in minutes the model training took to complete.
            class_labels
                A dictionary containing the class labels and their corresponding numeric values as used in the model.
            failed_models
                A list containing the pardon.InvalidModel classes containing the models that failed during the Pardon.rapid_ml method model selection.
            model_unique_identifier
                A unique identifier for the trained model.
            rapid_ml_scores
                A dictionary containing all the models that were trained during the Pardon.rapid_ml method and their corresponding performance scores.
            rapid_ml_score_metric
                The metric used to determine the best performing model when using the rapid_ml_method.
            best_validation_score
                A dictionary object containing the model being tested and the best score found during hyperparameter tuning with cross validation.
            model_train_scores
                The model performance scores during training.
            model_test_scores
                The model performance scores during testing.
            model_eval_metric
                The model evaluation metric used during training.
            data
                A pandas.DataFrame containing the data used in the model. This includes training data, test data, and validation data in its current form after any transformations.
            raw_data
                A pandas.DataFrame containing the raw data used when instantiating the pardon.Pardon object.
            train_data
                A pandas.DataFrame containing the data used in training the model in its current form after any transformations.
            test_data
                A pandas.DataFrame containing the data used in testing the model after training in its current form after any transformations. 
                Note, if the target was set to None during model instantiation, the test_data attribute will return an empty pandas.DataFrame and all data held in the train_data attribute.
            columns
                A list of the data columns used by the model.
            raw_data_columns
                A list of the data columns in the raw data used when instantiating the pardon.Pardon object.
            class_distribution
                A dictionary containing the distribution of each class in the target column in the raw data. Shows the count and percentage of occurrences of each class.
            train_class_distribution
                A dictionary containing the distribution of each class in the target column in the train data. Shows the count of occurrences of each class. Only available after model training.
            test_class_distribution
                A dictionary containing the distribution of each class in the target column in the test data. Shows the count of occurrences of each class. Only available after model training.
            model_fullpath
                The fullpath to where the model was saved. Only available after the save_model method has been completed.
            input_data_fullpath
                The fullpath for the input dataset. Only applicable if the input dataset was a file.
            prediction_audit_fullpaths
                The fullpath(s) to where any prediction audits have been saved.
            fail_ons
                A list containing details of all the FailOns added to your model.
            config
                A dictionary containing the details from the yaml file if provided.
    """
    def __init__(self, data, target:str=None, columns:list=[], encoding:str='latin-1', sep:str=',', error_bad_lines=None, test_size:float=0.3, remove_single_instance_classes:bool=False, is_regression='infer', stratify:bool=True, shuffle:bool=True, yaml:str=None):
        self.__MAX_TEST_VAL_SIZE = 0.95
        self.__MIN_TEST_VAL_SIZE = 0.05
        self.__DEFAULT_OPTIONS_STR = '_default_parameters'
        self._FIT_TRANSFORM_FUNCS = ['_one_hot_encode', '_frequency_encode', '_label_encode', '_ordinal_encode', '_scale_data', '_binary_encode']
        self._SINGLE_INSTANCE_FUNCTIONS = ['find_best_model_parameters']
        self._PLOT_SPLIT_COLS = self._FIT_TRANSFORM_FUNCS + ['_add_clusters']
        self._ignore_transformations_in_pred = []
        self._non_data_functions = []
        self.__OBJECTIVE = {'multi': 'multi:softprob', 'binary': 'binary:logistic'}
        self.__ITER_KEYS = ('n_estimators', 'max_iter')
        self.__IGNORED_CALLERS = ('predict', '__apply_data_transformations')
        utility.assert_item_type(item=target, item_types=[str, None])
        utility.assert_item_type(item=columns, item_types=[list])
        utility.assert_item_type(item=test_size, item_types=[int, float])
        utility.assert_item_type(item=encoding, item_types=[str])
        utility.assert_item_type(item=is_regression, item_types=[str, bool])
        utility.assert_item_type(item=stratify, item_types=[bool])
        utility.assert_item_type(item=shuffle, item_types=[bool])
        utility.assert_item_type(item=yaml, item_types=[str, None])
        self.config = config.load_yaml(yaml) if yaml is not None else {}
        self.input_data_fullpath = utility._check_save_parameters(fullpath=data, suppress_error=True) if isinstance(data, str) else None
        self.test_size = test_size
        self.prediction_audit_fullpaths = []
        self.__fail_ons = []
        self.__target = target
        self._stratify = stratify
        self._shuffle = shuffle
        self._holder_target = None
        self.__columns = columns
        self._classes_balanced = False
        self._remove_single_instance_classes = remove_single_instance_classes
        self._encoding = encoding
        self._sep = sep
        self._error_bad_lines = error_bad_lines
        self._ohe_encoder = None
        self._cross_validation_performed = None
        self._n_splits = 3
        self._n_repeats = 10
        self._ohe_encoded_column_input_names = []
        self._ohe_encoded_column_new_names = None
        self._frequency_encoder = None
        self._frequency_encoded_column_input_names = []
        self._frequency_encoder_new_item_value = 1
        self._label_encoder = None
        self._label_encoded_column_input_names = []
        self._ordinal_encoder = None
        self._ordinal_encoded_column_input_names  = []
        self._binary_encoder = None
        self._binary_encoded_column_input_names = []
        self._scaler = None
        self.scaler_used = None
        self._cluster_model = None
        self._cluster_column_name = None
        self._n_clusters = 0
        self._pca_encoder = None
        self._perform_pca = False
        self._pca_components = None
        self._X_train_pca_columns = None
        self._transformation_list = []
        self._label_encoder_ignore = []
        self._null_fills = {}
        self._convert_numeric = {}
        self._convert_date = {}
        self.model_trained_date = None
        self.model_training_time_mins = None
        self.model_train_scores = {}
        self.model_test_scores = {}
        self.model = None
        self.model_type = None
        self.model_unique_identifier = None
        self.model_fullpath = None
        self.model_eval_metric = None
        self._model_metric_to_save = None
        self._model_score_to_save = None
        self.__default_model_params = None
        self.best_validation_score = {}
        self.best_hyperparameters = {}
        self.validation_training_time_mins = {}
        self.class_labels = {}
        self.class_distribution = None
        self.train_class_distribution = None
        self.test_class_distribution = None
        self.rapid_ml_scores = {}
        self.rapid_ml_score_metric = None
        self.failed_models = []
        self._is_rapid_ml = False
        self.__random_state = 13
        self._data_cleared = False
        self.__convert_specific_funcs = []
        self._is_regression = is_regression if isinstance(is_regression, bool) else 'infer'
        # assign the data
        self.__data_assign(data=data) 

    def __str__(self) -> str:
        # string representation of the class for print
        output = '\n--------------------------\npardon.Pardon Class\n--------------------------\n'
        if self.target is not None:
            output += f'Model Unique Idenfitier: {self.model_unique_identifier}\n'
            output += f'Model Type: {self.model_type}\n'
            output += f'Model Predicts: {self.target}\n'
            if self.model_test_scores:
                scores = {st: round(score, 3) for st, score in self.model_test_scores.items()}
                output += f'Test Scores: {scores}\n'
        output += f'Input Data Fullpath: {self.input_data_fullpath}\n'
        output += f'Total Rows: {self.row_count()}\n'
        output += f'Total Columns: {self.column_count()}\n'
        output += f'Total Transformations: {self.transformation_count()}\n--------------------------\n'
       
        
        return output

    def __eq__(self, compared):
        """
        Compares the unique identifier for trained ML models, or the dataset for untrained models.
        """
        if not isinstance(compared, Pardon):
            return False

        # if not comparing ML models, compare datasets
        if self.model_unique_identifier is None and compared.model_unique_identifier is None:
            return self.data.equals(compared.data)

        # compare the unique identifiers
        return self.model_unique_identifier == compared.model_unique_identifier

    def __add__(self, add):
        """
        Adds the dataset from another Pardon model providing the columns are the same.
        """
        if not isinstance(add, Pardon):
            raise TypeError(f'Item is of type {type(add)}, not {type(self)}')

        # add the data from the model to this model
        self.add_data(data=add.data, overwrite_existing=False, train_model=False)

        return self

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, _):
        # block users from overwriting the target manually
        raise Exception('The target attribute can only be set during model instantiation.')

    @property
    def data(self) -> pd.DataFrame:
        # if the data has been cleared, return an empty dataframe
        if self.train_data is None:
            return pd.DataFrame()

        objs = (self.train_data, self.test_data)
        # combine the 2 dataframes into a single dataframe
        return pd.concat(objs=objs, axis='rows')

    @data.setter
    def data(self, _):
        # block users from overwriting the data
        raise Exception('The data attribute cannot be directly overwritten.')
        
    @property
    def columns(self) -> list:        
        # if we have yet to assign the training data, return the input columns
        if not hasattr(self, 'train_data'):
            return self._columns

        if self.train_data is not None:
            # return the columns from the training data
            output_cols = list(self.train_data.columns)
            if not hasattr(self, '_X_train_columns'):
                self._X_train_columns = self.__x_train_cols()
        else:
            # if it has been cleared, return the x train columns
            if not hasattr(self, '_X_train_columns'):
                self._X_train_columns = [col for col in self.data.columns if col != self.target]

            output_cols = list(self._X_train_columns).copy()

            if self.target is not None:
                output_cols.append(self.target)

        # if the target is none, we need to append the y column
        if self.target is None and self.target not in output_cols:
            searching = self._X_train_columns if self.train_data is None else self.train_data.columns
            for col in searching:
                if col not in output_cols:
                    output_cols.append(col)

        return output_cols

    def ignore_function_in_predictions(self, ignore_func:str, **kwargs):
        """
        Add the function or name of any functions you want to be ignored when applying future transformations.

            Args:
                ignore_func : func, str
                    The function or name of the function to ignore in future transformations.
                kwargs : keyword arguments
                    The keyword arguments associated with your function to ignore.
        """
        # ensure no reserved keyword arguments are being used
        pardon_transforms._validate_kwargs_reserved_words(kwargs)
        # we want to get the pardon methods as we may need to add an _ to the function name
        pardon_methods = dir(self)

        # if the user has passed the actual function, just get the function name
        if hasattr(ignore_func, '__call__'):
            ignore_func = ignore_func.__name__

        # retain the original name for the sake of success message
        orignal_name = ignore_func

        if isinstance(ignore_func, str):
            if ignore_func in pardon_methods:
                # all pardon retained methods will start with _ so we add that as that's what will be checked
                if not ignore_func.startswith('_'):
                    checks = ['_', '__']
                    # see if the actual func is with an _ or __
                    for check in checks:
                        if f'{check}{ignore_func}' in pardon_methods:
                            ignore_func = f'{check}{ignore_func}'
                            break
              
            transforms = pardon_transforms._RetainTransformation(function=ignore_func, kwargs=kwargs)
            # append the function name to the ignore list
            self._ignore_transformations_in_pred.append(transforms)

            print(f'{orignal_name} function successfully added to the ignore list.')
        else:
            raise Exception(f'Error adding {orignal_name}, pass the function name or uninstantiated instance of the function and try again.')

    def add_to_encoded(self, columns:list):
        """
        Add any columns that have been manually created that you want to be ignored by the label encoder. By default, any numeric columns will be ignored by the label encoder.

            Args:
                columns : list 
                    The names of the columns to be added to the columns to be ignored by the label encoder.
        """
        # make sure the columns are a list
        columns = utility.single_to_list(item=columns)

        # iterate through and add the columns to the ignore
        for column in columns:
            self._label_encoder_ignore.append(column)

    def clean_column_names(self, remove_non_ascii=False):
        """
        Remove any characters from column names that will not be accepted by the machine learning models as input, namely characters: "[],<>".
        If duplicates are found after the removal of these characters, they will be renamed with an _ and the next numeric value in the sequence starting from 1.

            Args:
                remove_non_ascii : bool, default False
                    Remove non-ascii characters if found in column names.
        """
        # remove the characters []<>,
        reg_sub = statics.CLEAN_COLUMN_NAME_REGEX
        rename_dict = {}

        for col in self.columns:
            # if the col name contains bad chars remove them and log to dict
            find_bad = re.findall(reg_sub, col, flags=re.I)
            non_ascii = False
            if find_bad:
                # get the name to be added
                clean_name = re.sub(reg_sub, '', col, flags=re.I)
                # check to see if there is already a column with that name
                if clean_name in rename_dict.values():
                    # get a list of occurences of the new name
                    add_num = list(rename_dict.values()).count(clean_name) + 1
                    # add _ num to the name to keep them unique
                    clean_name += f'_{add_num}'

            if remove_non_ascii:
                clean_name = utility.remove_non_ascii(string=col)
                if clean_name != col:
                    non_ascii = True

            if find_bad or non_ascii:
                # add the new name
                rename_dict[col] = clean_name

        # use the internal method to rename the columns and record the transformation
        if rename_dict:
            self.rename_columns(column_names=rename_dict)
        
    def available_models(self) -> tuple:
        """
        Returns the available machine learning models.

            Returns:
                (tuple) : tuple of string names for the available models.
        """

        return tuple([type(model).__name__ for model in self.__rapid_ml_models().keys()])
        
    def __check_args_kwargs_valid(self, func, args, kwargs, data, caller):

        # if this is a non-data func, we can ignore it
        if  func.__name__ in self._non_data_functions:
            return utility._InvalidFunction(function=func.__name__), None

        # if func in ignore list, return invalid as we do not want the prediction to do this
        # we only want to call this during the predict method
        if str(caller).lower() in self.__IGNORED_CALLERS:
            # if the function is one to ignore, we check if it is exactly the same function
            if func.__name__ in [func['function'] for func in self._ignore_transformations_in_pred]:
                same = pardon_transforms._check_same_func(func=func, kwargs=kwargs, ignored_functions=self._ignore_transformations_in_pred, ignored_kwargs={'_apply_func': ['new_column'], '_add_func': ['apply_to_train', 'apply_to_test', 'reconcile']})
                if same:
                    return utility._InvalidFunction(function=func.__name__), None
        
        data_in_args = False
        
        if args:
            # check if the arg contains a dataframe, if so, replace
            for i, arg in enumerate(args):
                if isinstance(arg, pd.DataFrame):
                    args[i] = data
                    data_in_args = True
                # if the arg is in fit transform and fit is true, set to false
                elif func.__name__ in self._FIT_TRANSFORM_FUNCS and isinstance(arg, bool):
                    return utility._InvalidFunction(function=func.__name__), None

        # if there is a fit key, return none as we will ignore this iteration
        if kwargs.get('fit'):  
            return utility._InvalidFunction(function=func.__name__), None

        # check to make sure args and kwargs do not contain the target column
        if str(caller).lower() == 'predict':
            args, kwargs = self.__check_args_kwargs_for_target(args=args, kwargs=kwargs)

        # assign data to the keyword args if not in data args
        if not data_in_args:
            kwargs['data'] = data
            
        return args, kwargs

    def __check_args_kwargs_for_target(self, args, kwargs):
        # check to ensure the target column is not included
        new_args = []
        new_kwargs = {}

        for arg in args:
            # check the valid state, if invalid, an invalid function object will return
            arg_check = self.__valid_checks(item=arg)    
            # if not invalid, add it to args
            if not isinstance(arg_check, utility._InvalidFunction):
                new_args.append(arg)
        
        # check the kwargs
        for key, value in kwargs.items():
            new_value = self.__valid_checks(item=value)
            # if not invalid, add it to kwargs
            if not isinstance(new_value, utility._InvalidFunction):
                new_kwargs[key] = new_value

        return tuple(new_args), new_kwargs

    def __valid_checks(self, item):
        # check to ensure none of the args are the target column
        if isinstance(item, str):
            if item == self.target:
                return  utility._InvalidFunction(item)
        # if the item is iterable, make sure the target is not included
        elif hasattr(item, '__iter__'):
            if self.target in item:
                if isinstance(item, dict):
                    new_item = {k: v for k, v in item.items() if str(k) != self.target and str(v) != self.target}
                else:
                    new_item = [keep for keep in item if keep != self.target]
                    new_item = tuple(new_item) if isinstance(item, tuple) else new_item

                return new_item

        return item

    def __non_data_func(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            self._non_data_functions.append(func.__name__)
            return func(self, *args, **kwargs)
        return inner

    def __ignore_function_in_transforms(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            transformation = pardon_transforms._RetainTransformation(function=func.__name__, args=args, kwargs=kwargs)
            self._ignore_transformations_in_pred.append(transformation)
            return func(self, *args, **kwargs)
        return inner

    def __function_unavailable_after_data_clear(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            if self._data_cleared:
                raise Exception(f'The function {func.__name__} is unavailable because during model saving, the clear_data parameter was set to True and all input data was cleared.')
            return func(self, *args, **kwargs)
        return inner

    def __block_null_target(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            # if the user is not using a target, block the ML functionality
            if self.target is None:
                raise Exception(f'The function: {func.__name__} is unavailable unless performing supervised machine learning with a valid target. Your target is set to None and therefore only clustering and data transformation methods are available.')
            return func(self, *args, **kwargs)
        return inner

    def __retain_transformation(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            df = func(self, *args, **kwargs)
            # if the caller is predict or apply, we ignore as do not want to retain as it is not part of training
            # get the calling func
            stack = str(inspect.stack()[1][3]).lower()
            # if this is not part of the predict call, log it
            if not stack in self.__IGNORED_CALLERS:
                # remove the data from the keyword args as it will be replaced with prediction data
                kwargs.pop('data', None)
                # make sure we put the fit to be False so future data doesnt get fitted
                if 'fit' in kwargs and func.__name__ in self._FIT_TRANSFORM_FUNCS:
                    kwargs['fit'] = False
                # keep a record of the function, args, and kwargs
                func_name = kwargs.get('func_name')
                transformation = pardon_transforms._RetainTransformation(function=func.__name__, args=args, kwargs=kwargs, func_name=func_name)
                # if this function hasn't already been added, adds
                if transformation not in self._transformation_list:
                    self._transformation_list.append(transformation)
            return df
        return inner

    def transformations(self) -> dict:
        """
        Return a dict showing the transformations applied by your model and those ignored.
        Ignored functions are those that were used in the data transformations but will not be applied to data coming in for predictions.

            Returns:
                (dict) : list containing the transformations applied to your data and those ignored during predictions.
        """
        pardon_methods = dir(self)
        ignore_funcs = [func['function'] for func in self._ignore_transformations_in_pred]
        include_funcs = [func['function'] for func in self._transformation_list if func['function'] not in ignore_funcs]
        # remove the underscores from internal methods so they look as the user would have called them
        reg = r'^_+'
        remove_underscores = lambda x: re.sub(reg, '', str(x)) if x in pardon_methods else x
        include_funcs = list(map(remove_underscores, include_funcs))
        ignore_funcs = list(map(remove_underscores, set(ignore_funcs)))

        output = {}
        output['included_transformations'] = include_funcs
        output['ignored_transformations'] = ignore_funcs

        return output
    
    @__function_unavailable_after_data_clear
    def set_best_features(self, max_features=20, min_contribution_score:int=None):
        """
        Automatically sets the data columns to be used in model training based on best performing features. This automatically sets the columns using the get_best_features method.
        
            Args:
                max_features : int, default 20
                    The maximum number of columns to retain. This will mean only the top n best performing columns will be kept.
                min_contribution_score : int, default None
                    The minimum score returned based on the ANOVA F-value for classification tasks and the F-Statistic for regression, for the provided sample. If the column does not meet the minimum score, it will not be retained.
        """
        # get all the columns not including the target
        all_cols = len(self.columns) - 1

        # if the user has specified a percentage get that
        if isinstance(max_features, float):
            # if the user specified more than 1 or less than 0.1, set all
            if max_features >= 1:
                max_features = 'all'
            else:
                # get the proportion of columns    
                n_max = round((all_cols) * max_features)
                # if the result is a float, round up
                max_features = int(np.ceil(n_max)) if isinstance(n_max, float) else n_max
        # set to include all columns if max features is incorrectly supplied
        elif not isinstance(max_features, int):
            max_features = 'all'
            
        if isinstance(max_features, (int, float)):
            # if max is less than 1, raise an error
            if max_features < 1:
                raise ValueError('You cannot have a max_features less than 1.')
            # max features is more than the columns, set it to all
            elif max_features > all_cols:
                max_features = 'all'

        best_features = self.get_best_features(max_features=max_features, min_contribution_score=min_contribution_score)
        # get the columns that were removed
        remove_columns = list(set(self.train_data.columns).difference(set(best_features)))
        # ensure the target is not in the remove just in case
        if self.target in remove_columns:
            remove_columns.remove(self.target)
        # this is done to keep a record of columns that were removed
        if remove_columns:
            self.remove_columns(columns=remove_columns)

    def get_feature_contribution(self, suppress_errors=False) -> dict:
        """
        Produces a dictionary object containing the columns contribution to the prediction of the target based on the ANOVA F-value score for classification and F-statistic for regression. Note, data should have been encoded prior to using this method.
        
            Args:
                suppress_errors : bool, default False
                    If errors are suppressed, any errors will mean an empty dictionary object is returned instead of an error being raised.

            Returns:
                (dict) : dict containing the column names and the associated feature contribution score. 
         """
        # this has to be done at the end after scaling and encoding
        try:
            # set the x, y values
            self.__set_x_y_values() 
            classif = f_regression if self._is_regression else f_classif 
            select = SelectKBest(classif, k='all')
            fit = select.fit(self._X_train, self._y_train)
            # get the feature names
            filter = fit.get_support()
            # get the filter list of columns
            filtered_list = list(self._X_train.columns[filter])
            # get the final dictionary out
            scoring = dict(zip(filtered_list, fit.scores_))
            # sort by highest values first
            scoring = utility.sort_dictionary(scoring)
        # an error may occur if we cannot get feature contribution values for the x and y
        except Exception as err:
            # if errors are suppressed, return an empty dict
            if suppress_errors:
                scoring = {}
            else:
                raise err

        return scoring

    @__function_unavailable_after_data_clear
    @__block_null_target
    def get_best_features(self, max_features=20, min_contribution_score=None) -> list:
        """
        Returns a list of that are determined to be the best performing features.

            Args:
                max_features : int, default 20
                    The maximum number of columns to retain. This will mean only the top n best performing columns will be kept.
                min_contribution_score : int, default None
                    The minimum score returned based on the ANOVA F-value for classification tasks and the F-Statistic for regression, for the provided sample. If the column does not meet the minimum score, it will not be retained.

            Returns:
                (list) : list of the predicted best features for your model from your training data
        
        """
        # this has to be done at the end after encoding
        self.__set_x_y_values() 
        classif = f_regression if self._is_regression else f_classif 
        total_features = len(self._X_train.columns)
        max_features = total_features if str(max_features).lower() == 'all' or (max_features > total_features) else max_features
        select = SelectKBest(classif, k=max_features)

        try:
            # fit the features
            fit = select.fit(self._X_train, self._y_train)
            # get the feature names
            filter = fit.get_support()
        # an error means not all the data is encoded
        except ValueError as err:
            raise ValueError(f'The get_best_features and set_best_features methods can only be used after all non-numerical data has been encoded, and all nulls removed. Encode your data or use model.ordinal_encode() or model.label_encode() and ensure you have removed null values and try again.\nError message was: {err}')
        
        # get the filter list of columns
        filtered_list = list(self._X_train.columns[filter])

        # if the user has specified a min contribution score, remove any not hitting score
        if min_contribution_score:
            # get the scores and names   
            scoring = list(zip(filtered_list, fit.scores_))
            for item in scoring:
                # if the score less than min, remove it
                if item[1] < min_contribution_score or pd.isna(item[1]):
                    filtered_list.remove(item[0])
        
        # if no columns are left, raise an error
        if not filtered_list:
            raise ValueError(f'A min_contribution_score of {min_contribution_score} leaves no columns present. Reduce your min_contribution_score and try again.')

        # append the target as that was not included in the feature selection
        filtered_list.append(self.target)

        return filtered_list

    @__function_unavailable_after_data_clear
    def map_data(self, mapping_data):
        """
        Map data to a mapping value or file.

            Args:
                mapping_data : dict
                    A dictionary object containing a key of the column name to map, and the value being the data that provides the mapping. The value can be any item accepted by the data parameter as per the Pardon instantiation.
                    Think of this function as equivalent to Excel's vlookup, where you specify the column name to apply this to, and then the vlookup. An example would be mapping_data={'SymptomGroup': 'symptom_groups.csv'}. The symptom_groups.csv will contain each value as found in the SymptomGroup column and the corresponding value(s) that should map to. The column(s) containing the corresponding value(s) will be added to the data.
        """
        utility.assert_item_type(item=mapping_data, item_types=[dict])

        # set the values and map the data
        self.__convert_data_using_func(convert_func=self._map_data, apply_convert_to_train=True, apply_convert_to_test=True, mapping_data=mapping_data)

    @__retain_transformation
    def _map_data(self, *, data, mapping_data) -> pd.DataFrame:
        # iterate through and apply the mappings
        for column, map_data in mapping_data.items():
            # can only map when the column exists in the data
            if column in data.columns:
                # get the dataframe object from the input data
                df = utility.data_reader(data=map_data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)
                data = data.merge(df, on=column, how='left')
                
        return data

    def __class_counting(self, data) -> dict:

        # get the class counts from the target column into a dictionary
        counts = data[self.target].value_counts().to_dict()

        return counts

    def __class_distribution(self, data):

        # return none
        if self.target is None:
            return None
        
        # get the counts
        counts = self.__class_counting(data=data.copy())
        totals = sum(counts.values())
        # sort the dictionary by total
        counts = utility.sort_dictionary(counts)

        # if we have the class labels, assign them
        if self.class_labels:
            # check to ensure the keys all match and if they do, get the associated keys
            # this changes encoded class labels to their corresponding string value
            if sorted(list(counts.keys())) == sorted(list(self.class_labels.keys())):
                counts = {self.class_labels.get(k): v for k, v in counts.items()}

        # set the class distribution for each class
        out_dict = {k: f'{v} ({round((counts[k] / totals) * 100, 1)}%)' for k, v in counts.items()}

        return out_dict
     
    def __data_assign(self, data):

        # read the input data
        input_data = self.__read_data(data=data)

        if input_data is None:
            raise ValueError('Invalid input data, please use a valid csv and try again.')

        # make a copy of the input data where we only include labelled targets
        # this will drop rows with no labels
        data = input_data[input_data[self.target].notna()].copy() if self.target is not None else input_data.copy()

        # if the target is none, it means we are not doing machine learning
        if self.target is not None:
            data_len = len(data)
            # double check in case the user has overwritten the value and has only 1 row
            if data_len < 2:
                raise ValueError(f'The dataset only contains 1 row which is too few to develop a machine learning model. Ensure your dataset contains more rows and try again.')

            if data_len < pardon_options.MIN_ROW_REQ:
                raise Exception(f'There are only {data_len} labelled rows in the dataset. Please get {pardon_options.MIN_ROW_REQ} or more rows or reduce the MIN_ROW_REQ attribute using pardon.pardon_options.MIN_ROW_REQ = 10 if you wish to overwrite this.')
  
            # check the test sizes - ensure they are of sufficient size
            if self.test_size < self.__MIN_TEST_VAL_SIZE:
                raise ValueError(f'The test_size of "{self.test_size}" is too small. Please increase your test_size to {self.__MIN_TEST_VAL_SIZE} or above and try again.')
            # ensure the test size is not too large
            if self.test_size > self.__MAX_TEST_VAL_SIZE:
                raise ValueError(f'The test_size of "{self.test_size}" is too large. Please reduce your test_size to {self.__MAX_TEST_VAL_SIZE} or below and try again.')

            # get the counts of each class
            counts = self.__class_counting(data=data.copy())
            # check to see if this is binary class or not
            class_num = len(counts.keys())
            # ensure there is more than 1 class
            if class_num < 2:
                raise ValueError(f'The target column only contains 1 class. Ensure there are 2 or more classes in the target column and try again.')
            # check to see if this is a regression or classification
            if self._is_regression == 'infer':
                self._is_regression = utility._check_if_regression(data=data, target=self.target)

            # check to see if each class has at least 2 items in, if not remove if requested
            # only relevant for classification
            if not self._is_regression:
                items_to_remove = [class_ for class_, cnt in counts.items() if cnt < 2]
                if self._remove_single_instance_classes and items_to_remove:
                    # if we have items to remove, remove them
                    for remove_val in items_to_remove:
                        data = self._remove_rows_containing(data=data, column_items={self.target: remove_val})
                # if there are items to remove but the user has not requested this, raise an error
                elif items_to_remove and not pardon_options.IGNORE_SINGLE_CLASS_ERROR:
                    raise ValueError(f'The Target column: {self.target} has classes containing only 1 instance, which is too few. Remove these from the dataset or pass remove_single_instance_classes=True when instantiating the Pardon class and try again. If this is a regression task, pass is_regression=True to avoid this error. To ignore this error, set pardon.pardon_options.IGNORE_SINGLE_CLASS_ERROR = True')
            
            # set the class distribution
            if not self._is_regression:
                # set the class distribution
                self.class_distribution = self.__class_distribution(data=data)

            # get the x, y values for the dataset
            X, y = self._X_y_values(data=data)

            # set stratify depending on shuffle
            if not self._shuffle:
                if self._stratify and not self._is_regression:
                    print(f'*** WARNING: stratify set to False because stratify cannot be used when shuffle is set to False. ***')
                self._stratify = False

            stratify = y if not self._is_regression and self._stratify else None

            # get the train test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.__random_state, stratify=stratify, shuffle=self._shuffle)

            # set the train and test data                                          
            self.train_data = pd.merge(X_train, y_train, left_index=True, right_index=True)
            self.test_data = pd.merge(X_test, y_test, left_index=True, right_index=True)

            # reset the indexes
            for df in (self.train_data, self.test_data):
                df.reset_index(drop=True, inplace=True)
        else:
            # set stratify to False simply for the sake of the model script as it is not relevant for non-ML tasks as no train test split occurs
            self._stratify = False
            # set test size to 0 as this is now an empty dataframe
            self.test_size = 0
            # set everything to train and an empty dataframe to test
            self.train_data = data
            self.test_data = pd.DataFrame()

        # set the data  
        self.raw_data = data.copy()
        # set the raw input columns
        self.raw_data_columns = list(self.raw_data.columns)
        # ensure data clear is set to False - this is here in case users clear data and then re-add data
        self._data_cleared = False
        # remove the columns not requested to be kept by the user
        # this is done here so if those columns exist in the future, they will be removed
        if self.__columns:
            remove_cols = utility.list2_differences(list1=self.__columns, list2=data.columns)
            if remove_cols:
                self.remove_columns(columns=remove_cols)

            if not self.columns:
                raise Exception(f'All columns have been removed and so no data is available. Check the columns argument contains the correct column list and try again.\nThe available columns are: {list(data.columns)}')

    def row_count(self, dataset='all') -> int:
        """
        Get a count of rows in the selected dataset.

            Args:
                dataset : str, default {'all', 'train', 'test', 'raw'}
                    The dataset to get the row count for. Valid inputs are all, train, test, raw, 'all' is a combination of train and test data.

            Returns:
                (int) : count of rows for the specified dataset
        """
        # make the input lower case and a string
        dataset = str(dataset).lower()
        
        # set the valid data sets that can be row counted
        valid_sets = ('all', 'train', 'test', 'raw')
        
        # raise error that an invalid dataset has been specified
        if dataset not in valid_sets:
            raise ValueError(f'Specify which dataset you want to include from the following: {", ".join(valid_sets)}')

        if not self._data_cleared:
            # get the relevant data
            data = self.data if dataset == 'all' else getattr(self, f'{dataset}_data')
            # check to see if the data has values and return the number of rows
            data = 0 if data is None else len(data)
        else:
            # get the row counts as recorded, only available if the data was cleared
            data = getattr(self, f'_{dataset}_row_count')
        
        return data

    def column_count(self) -> int:
        """
        Return a count of columns in the data.

            Returns:
                (int) : Count of columns in the current data set.
        
        """
        return len(self.columns)

    def transformation_count(self) -> int:
        """
        Return a count of transformations applied to the data.

            Returns:
                (int) : Count of transformations.
        
        """
        return len(self._transformation_list)
    
    def number_of_classes(self) -> int:
        """
        Get a count of the number of classes in the target column of the data.

            Returns:
                (int) : Count of the number of classes in the target columns.
        """
        return len(self.classes())

    def __convert_data_using_func(self, convert_func, apply_convert_to_train=True, apply_convert_to_test=True, **kwargs):
        # apply the custom function and arguments to the data

        # we remove any data from the kwargs because we specify the data using train or test
        if 'data' in kwargs:
            kwargs.pop('data')

        # set the train data
        if apply_convert_to_train:
            self.train_data = convert_func(data=self.train_data, **kwargs)

        # if we are not using a target, we don't use the test data because everything is in train data, so only use if relevant
        if len(self.test_data) > 0 and apply_convert_to_test:
            # fit will mean we are doing transformations to data, and should be set to False for test data
            if 'fit' in kwargs and convert_func.__name__ in self._FIT_TRANSFORM_FUNCS:
                kwargs['fit'] = False
                
            self.test_data = convert_func(data=self.test_data, **kwargs)

        # keep a record of any functions where they were explictly not applied to test or train data
        if not apply_convert_to_train or not apply_convert_to_test:
            retention_dict = {'function': convert_func.__name__, 'apply_convert_to_train': apply_convert_to_train, 'apply_convert_to_test': apply_convert_to_test, 'kwargs': kwargs}
            self.__convert_specific_funcs.append(retention_dict)

    def __raw_classes(self) -> list:

        if self._is_regression:
            return []
        
        # if data cleared get the saved classes
        if self._data_cleared:
            return self._classes
        # get the class counts
        classes = self.__class_counting(data=self.data.copy())
        # get the unique class names
        classes = classes.keys()
        # if all values are numeric, it is possibly because they have been encoded
        if utility.all_numeric(data_list=classes):
            # check to see if we have the class labels
            if self.class_labels:
                # if we do, get the labels
                classes = self.class_labels.values()

        return list(classes)

    def classes(self) -> list: 
        """
        Returns a list of unique classes in the target column of the data.

            Returns:
                (list) : A list of unique classes in the target column.
        """
        # return empty list if regression as not applicable
        if self._is_regression:
            return []

        # if cleared get the saved classes
        if self._data_cleared:
            return self._classes

        # using this ensures order of classes is correct
        if self.model is not None:
            if self.class_labels:
                # ensures the classes are returned in the correct order from the model when relevant
                list_of_classes = [self.class_labels.get(x) for x in list(self.model.classes_)]
            else:
                list_of_classes = [x for x in list(self.model.classes_)]
            
            return list_of_classes

        return sorted(self.__raw_classes())
    
    @__function_unavailable_after_data_clear
    def data_info(self) -> pd.DataFrame:
        """
        Returns information about the data. Uses pandas.DataFrame.info method.

            Returns:
                (pandas.DataFrame) : information about the data
        """
        return self.data.info()

    @__function_unavailable_after_data_clear
    def data_types(self) -> pd.DataFrame:
        """
        Returns the data types for the transformed data.

            Returns:
                (pandas.DataFrame) : Data types for the data
        """
        return self.data.applymap(type).apply(pd.value_counts).fillna(0)

    @__function_unavailable_after_data_clear
    def null_counts(self) -> dict:
        """
        Returns the count of nulls in each column where at least 1 null is present.

            Returns:
                (dict) : Returns a dict with Null counts for each column
        """
        # this gets the number of nulls by column into a dict, providing there is at least 1 null
        null_counts = self.data[self.data.columns[self.data.isnull().any()]].isnull().sum().to_dict()

        return utility.sort_dictionary(null_counts)

    def __read_data(self, data) -> pd.DataFrame:
        # read the data and return a dataframe object
        # if string it is a file
        if isinstance(data, str):
            # get file name and file extension
            self.input_filename, self.input_file_extension = os.path.splitext(data)
        
        # set the dataframe based on the input file
        df = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)

        # if no columns were specified, update the columns with those found in the file
        self._columns = list(df.columns) if not self.__columns else self.__columns

        # validate to ensure the specified columns exist
        if self.__columns:
            invalid_columns = self.__validate_columns(df=df)
            # if there are invalid columns raise a key error
            if invalid_columns:
                col_string = ', '.join([str(x) for x in invalid_columns])
                raise KeyError(f'The following {len(invalid_columns)} columns were not found in the input dataset: "[{col_string}]", please check your columns argument and try again.')
 
        # if this is a supervised task, check the target column is valid
        if self.target is not None:
            # if the target is not in the columns, raise an error
            if self.target not in self.columns:
                raise KeyError(f'The target column: {self.target} does not appear in the column list, please specify a valid target column and try again')

        # return pandas dataframe
        return df
    
    def __validate_columns(self, df) -> list:
        
        # if any of the columns in the self.columns are not in the dataframe, return them
        invalid_columns = [col for col in self.columns if col not in df.columns]
                
        # return a list of invalid columns not found in dataset
        return invalid_columns
    
    @__function_unavailable_after_data_clear
    def remove_unhelpful_columns(self, max_null_ratio:float=0.5):
        """
        Removes columns from the data that have been deemed as unhelpful. An unhelpful column is one categorised as one of the following:
            -> Every data item in the column is the same value.
            -> The column data type is a string, and every data item in the column is different.
            -> The proportion of rows that are null exceeds that specified in the max_null_ratio parameter.
        
        Note: this is only applicable when there are 2 or more rows.

            Args:
                max_null_ratio : float, default 0.5
                    The max proportion of the column that contains null values. 0.5 would mean that if more than 50% of the column values are null, the column will be deemed as unhelpful.
        """
        # get the unhelpful columns
        unhelpful = self.unhelpful_columns(max_null_ratio=max_null_ratio)

        # if any columns return, remove them
        if unhelpful:
            self.remove_columns(columns=unhelpful)
    
    def unhelpful_columns(self, max_null_ratio:float=0.5) -> list:
        """
        Returns a list of columns from the data that have been deemed as unhelpful. An unhelpful column is one categorised as one of the following:
            -> Every data item in the column is the same value.
            -> The column data type is a string, and every data item in the column is different.
            -> The proportion of rows that are null exceeds that specified in the max_null_ratio parameter.
        
            Args:
                max_null_ratio : float, default 0.5
                    The maximum proportion of the column that contains null values. 0.5 would mean that if more than 50% of the column values are null, the column will be deemed as unhelpful.
        
            Returns:
                (list) : returns a lit of string column names of those columns considered to be unhelpful to the model training process.
        """
        # if an integer or float or None is not provided raise an error
        utility.assert_item_type(item=max_null_ratio, item_types=[float, int, None])

        # if none has been specified return an empty list as we do not need to remove anything
        if max_null_ratio is None:
            return []
        
        if max_null_ratio is not None and (max_null_ratio > 1 or max_null_ratio < 0):
            raise ValueError(f'The value for null_ratio must be below 1 and above 0.')
        
        # set the output list
        unhelpful = []

        # get number of rows in dataset
        total_rows = len(self.data)

        if total_rows > 1 :
            # for each column check to see if there is only 1 unique value
            for col in (col for col in self.columns if col != self.target):
                # count the number of unique items
                n_unique = self.data[col].nunique()
                # if there is only 1 unique, add it as unhelpful
                if n_unique == 1:
                    unhelpful.append(col)
                    continue
                # if the column is of object type and every row is different, it also will be unhelpful
                if n_unique == total_rows and self.data[col].dtype == 'object':
                    unhelpful.append(col)
                    continue

                if max_null_ratio is not None:  
                    # see how many nulls there are
                    null_in_row = self.data[col].isna().sum()
                    # if there is a ratio of nulls higher than the specified match, add that column to the remove list
                    if (null_in_row / total_rows) > max_null_ratio:
                        unhelpful.append(col)

        return unhelpful

    @__function_unavailable_after_data_clear
    def convert_to_datetime(self, columns:list, fill_non_datetime='mode', day_first:bool=True, year_first:bool=False, format:str=None):
        """
        Converts the columns specified in the columns parameter to a datetime datatype. Specify how to deal with non-date or empty rows using the fill_non_datetime parameter.

            Args:
                columns : str, list
                    A single column string or list containing the columns to be converted to a datetime datatype.
                fill_non_datetime : str, default 'mode'
                    Use 'mode' to fill empty values with the most common date or pass a date in a string format.
                day_first : bool, default True
                    If True, parse dates as though the day is first. For example,  "10/11/12" is parsed as 2012-11-10.
                year_first : bool, default False
                    If True, parse dates as though the year is first. For example, "10/11/12" is parsed as 2010-11-12. If both day_first=True and year_first=True, year_first will take precedence.
                format : None, str, default None
                    The date format to parse the dates as. Follow the guidance for the correct date format. If None, the format will be inferred automatically.
        """
        # check args
        utility.assert_item_type(item=fill_non_datetime, item_types=[str])
        utility.assert_item_type(item=day_first, item_types=[bool])
        utility.assert_item_type(item=year_first, item_types=[bool])
        utility.assert_item_type(item=format, item_types=[str, None])

        # get the column list
        columns = utility.single_to_list(item=columns)

        # check the fill empty
        if isinstance(fill_non_datetime, str):
            fill_non_datetime = fill_non_datetime.lower()

        # apply the conversion
        self.__convert_data_using_func(convert_func=self._convert_to_datetime, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, fill_non_datetime=fill_non_datetime, day_first=day_first, year_first=year_first, format=format)

    @__retain_transformation
    def _convert_to_datetime(self, *, data, columns:list, fill_non_datetime=None, day_first=True, year_first=False, format=None) -> pd.DataFrame:

        # function used to ensure only digits are kept
        for column in columns:
            # if the column is valid
            if column in data.columns:
                # get all the numbers from raw data
                data[column] = pd.to_datetime(data[column], errors='coerce', format=format, infer_datetime_format=True, dayfirst=day_first, yearfirst=year_first).fillna(np.nan)

                # replace the na values
                if column in self._convert_date:
                    av_data = self._convert_date.get(column)
                else:
                    if fill_non_datetime == 'mode':
                        av_data = self.__get_average(data=data[column], average_type=fill_non_datetime)
                        # if an error with the mode, raise an error
                        if av_data == pardon_options.AVERAGE_FAIL_DEFAULT_VALUE:
                            raise ValueError(f'Mode cannot be found for the column: {column}. Specify a specific value using the fill_empty argument.')
                    else:
                        # get the date format for the value specified - this will raise an error if fails
                        av_data = pd.to_datetime(fill_non_datetime, format=format, infer_datetime_format=True, dayfirst=day_first, yearfirst=year_first)

                    # fill the na values
                    data[column].fillna(value=av_data, inplace=True)

                    # retain a record of date conversion
                    if column not in self._convert_date:
                        self._convert_date[column] = av_data

        return data

    @__function_unavailable_after_data_clear
    def sort_by(self, columns:list, desc:bool=False, apply_to_test:bool=True):
        """
        Sort data by the columns specified.

            Args:
                columns : list
                    A list containing the columns to be sorted by.
                desc : bool, default False
                    Sort in a descending order.
                apply_to_test : bool, default True
                    Apply the sort to your test dataset.
        """
        utility.assert_item_type(item=columns, item_types=[str, list])
        utility.assert_item_type(item=desc, item_types=[bool])
        utility.assert_item_type(item=apply_to_test, item_types=[bool])

        if not columns:
            raise ValueError('Add at least one column to be sorted by and try again.')

        # get the column list
        columns = utility.single_to_list(item=columns)

        # apply the function
        self.__convert_data_using_func(convert_func=self._sort_by, apply_convert_to_train=True, apply_convert_to_test=apply_to_test, columns=columns, desc=desc)

    @__retain_transformation
    def _sort_by(self, *, data, columns:list, desc:bool=False) -> pd.DataFrame:

        data.sort_values(by=columns, inplace=True, ascending=not desc)

        return data
      
    @__function_unavailable_after_data_clear
    def convert_to_numeric(self, columns:list, fill_non_numeric='median'):
        """
        Converts the columns specified in the columns parameter to a numeric datatype. Specify how to deal with non-numeric or empty rows. If no numeric data is found when determining an average, every row will be set to pardon.pardon_options.AVERAGE_FAIL_DEFAULT_VALUE by default.

            Args:
                columns : list
                    A list containing the columns to be converted to a numeric datatype.
                fill_non_numeric : str, int, float, func, default 'median' {'mean', 'median', 'mode'}
                    Fill non-numeric values with the column average, pass a number or a function.
        """ 
        # get lower case
        if isinstance(fill_non_numeric, str):
            fill_non_numeric = fill_non_numeric.lower()

        # check the correct average was used
        if isinstance(fill_non_numeric, str) and fill_non_numeric not in statics.AVERAGES:
            raise ValueError(f'The fill_non_numeric argument must contain one of the following: {statics.AVERAGES} or pass a float, integer, or function.')
        
        # get the column list
        columns = utility.single_to_list(item=columns)

        # apply the function
        self.__convert_data_using_func(convert_func=self._convert_to_numeric, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, fill_non_numeric=fill_non_numeric)

    @__retain_transformation
    def _convert_to_numeric(self, *, data, columns:list, fill_non_numeric='median') -> pd.DataFrame:

        # function used to ensure only digits are kept
        for column in columns:
            # if the column is valid, replace any N/A or null with the replacement value
            if column in data.columns:
                # get all the numbers from raw data
                data[column] = pd.to_numeric(data[column], errors='coerce').fillna(np.nan)
                # if we have seen this before, get the fill value
                if column in self._convert_numeric:
                    av_data = self._convert_numeric.get(column)
                else:
                    if isinstance(fill_non_numeric, str):
                        # get the average from raw numbers
                        av_data = self.__get_average(data=data[column], average_type=fill_non_numeric)
                        # if the ave val for some reason is not numeric, set it to 0
                        if not isinstance(av_data, (int, float)):
                            av_data = pardon_options.AVERAGE_FAIL_DEFAULT_VALUE
                    else:
                        av_data = fill_non_numeric

                # convert to numeric and all non numeric will be set to av_data
                if callable(fill_non_numeric):
                    data[column] = data[column].apply(fill_non_numeric)
                else:
                    data[column].fillna(value=av_data, inplace=True)

                data[column] = pd.to_numeric(data[column])

                # retain a record of numerical conversion
                if column not in self._convert_numeric and not callable(fill_non_numeric):
                    self._convert_numeric[column] = av_data

        return data

    @__function_unavailable_after_data_clear
    def convert_to_string(self, columns:list):
        """
        Converts the columns specified in the columns parameter to an object/string datatype.

            Args:
                columns : str, list
                    A single column string or a list containing the columns to be converted to an object/string datatype.
        """ 
        # get the column list
        columns = utility.single_to_list(item=columns)
        # apply the function
        self.__convert_data_using_func(convert_func=self._convert_to_string, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns)

    @__retain_transformation
    def _convert_to_string(self, *, data, columns:list) -> pd.DataFrame:

        for column in columns:
            if column in data.columns:
                data[column] = data[column].astype(str)
                
        return data
    
    def __validate_column_argument(self, columns:list, return_target:bool=False, check_invalid:bool=True) -> list:
        # if the columns arg is not a list, convert it
        columns = utility.single_to_list(item=columns)
        # ensure all columns are valid
        if check_invalid:
            columns = self.__invalid_columns(columns=columns)
        # if no columns are specified, use all columns
        columns = self.__check_for_all_columns(columns=columns)
        # remove the target column if necessary
        if not return_target and self.target in columns:
            columns.remove(self.target)

        return columns
    
    @__function_unavailable_after_data_clear
    def find_outliers(self, columns=[], z_threshold=3.0, apply_to_test:bool=True, return_as='values', ignore_target=False) -> dict:
        """
        Returns a dictionary object containing the column name as a key, and then the outlier values as the value.

            Args:
                columns : list, default [] (empty list)
                    The columns to check for outliers. An empty list means all numeric columns will be checked for outliers.
                z_threshold : int, float, default 3.0
                    The z score determining an outlier. A z score of 3.0 means the value is 3 standard deviations or more away from the column mean.
                apply_to_test: bool, default True
                    Find outliers for the train and test data.
                return_as : str, default 'values' {'values', 'index'}
                    The format to return the outliers. Values means the actual values are returned. This is the recommended format. If not set to values, a pandas.Series object containing the associated indexes will be returned.
                ignore_target : bool, default False
                    Specify if you want to ignore the target column when finding outliers in the data. This only applies if no columns are supplied to the columns argument. ignore_target=False means that unless columns are specified, the target column will also be searched and have any outliers removed.

            Returns:
                (dict, pd.Series) : A dictionary object containing the column name as keys and the relevant outlier values as the values, or if using index, a pandas.Series object containing the relevant row indexes containing outliers. 
        """
        # if an integer is not provided raise an error
        utility.assert_item_type(item=z_threshold, item_types=[float, int])
        
        columns = self.__validate_column_argument(columns=columns, return_target=not ignore_target)

        data = self.data if apply_to_test else self.train_data
                
        return self.__find_outliers(data=data, columns=columns, z_threshold=z_threshold, return_as=return_as)
        
    def __find_outliers(self, data, columns, z_threshold=3.0, return_as='values') -> dict:
        # set the object for returning
        output_dict = {}
        columns_containing_nulls = []
        
        # reset the index so we use row numbers
        data.reset_index(drop=True, inplace=True)
        
        for column in columns:
            if column in data.columns:
                if is_numeric_dtype(data[column]):
                    if data[column].isna().sum() == 0:
                        # get the z scores for the column
                        z = np.abs(stats.zscore(data[column]))
                        outliers = np.where(z > z_threshold)
                        # return the rows that exceed the z threshold
                        if return_as == 'values':
                            outliers = data[column].iloc[outliers].unique()
                        # set the items to the dict
                        output_dict[column] = outliers
                    else:
                        columns_containing_nulls.append(column)

        # nulls mean z score cannot be determined
        if columns_containing_nulls:
            raise Exception(f'Z Score cannot be found for columns: {columns_containing_nulls} because they contain null values. Remove these using the fill_nulls or convert_to_numeric functions and try again. No outliers have been removed.')
                
        return output_dict
    
    def __check_for_all_columns(self, columns) -> list:
        # if the user has specified columns use them else use all calls
        return columns if columns else self.columns
    
    def __invalid_columns(self, columns) -> list:
        # ensure all columns are valid
        if columns:
            invalid_columns = [col for col in columns if col not in self.columns]
            # if columns are present they are invalid so raise an error
            if invalid_columns:
                raise ValueError(f'The following columns are not present in the data: {columns}')
        
        return columns
    
    @__function_unavailable_after_data_clear
    def remove_outliers(self, columns=[], z_threshold=3.0, apply_to_test:bool=True, ignore_target=False):
        """
        Removes the outliers from the model's training data only. Test data remains unchanged.

            Args:
                columns : list, default [] (empty list)
                    The columns to remove outliers. An empty list means all numeric columns will be checked for outliers.
                z_threshold : int, float, default 3.0
                    The z score determining an outlier. A z score of 3.0 means the value is 3 standard deviations or more away from the column mean.
                apply_to_test: bool, default True
                    Remove outliers from the train and test data.
                ignore_target : bool, default False
                    Specify if you want to ignore the target column when finding outliers in the data. This only applies if no columns are supplied to the columns argument. ignore_target=False means that unless columns are specified, the target column will also be searched and have any outliers removed.
        """        
        # if an integer is not provided raise an error
        utility.assert_item_type(item=z_threshold, item_types=[float, int])
        utility.assert_item_type(item=ignore_target, item_types=[bool])

        # only remove outliers for train data NOT test data - so we set apply_convert_to_test=False
        self.__convert_data_using_func(convert_func=self._remove_outliers, apply_convert_to_train=True, apply_convert_to_test=apply_to_test, columns=columns, z_threshold=z_threshold, ignore_target=ignore_target)

    @__retain_transformation
    @__ignore_function_in_transforms
    def _remove_outliers(self, *, data, columns, z_threshold=3.0, ignore_target=False) -> pd.DataFrame:
        # we keep ignore_target for the sake of the data script for visibility of if this was included

        # reset the index so we use row numbers
        data.reset_index(drop=True, inplace=True)

        # get columns if none-specified
        columns = self.__validate_column_argument(columns=columns, return_target=not ignore_target)

        # return the outliers as their index position
        outliers = self.__find_outliers(data=data, columns=columns, z_threshold=z_threshold, return_as='values')

        # iterate through the column and values
        for col, values in outliers.items():
            # remove the values from each column
            data = data[data[col].isin(values) == False]

        return data
    
    @__function_unavailable_after_data_clear
    def drop_nulls(self, columns=[]):
        """
        Drops rows containing nulls in the columns specified.

            Args:
                columns : list, default [] (empty list)
                    The columns to check for null values. An empty list means all columns will be checked for nulls.
        """
        columns = self.__validate_column_argument(columns=columns, return_target=True)
    
        if not columns:
            raise ValueError('No valid columns specified, please try again.')
        
        # apply the function
        self.__convert_data_using_func(convert_func=self._drop_nulls, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns)

    @__retain_transformation
    @__ignore_function_in_transforms
    def _drop_nulls(self, *, data, columns=[]) -> pd.DataFrame:

        # if an empty list is present, make it None
        columns = None if not columns else columns
        # make sure we only attempt to drop columns that exist
        columns = [col for col in columns if col in data.columns] if columns is not None else None
        
        # drop rows that contain nulls
        data.dropna(axis=0, how='any', subset=columns, inplace=True)
        
        return data

    @__function_unavailable_after_data_clear
    def fill_nulls(self, columns=[], fill_text_with='Unknown', fill_numeric_with='mean', by_col_name:dict={}):
        """
        Fill null values in the columns specified with the values specified.

            Args:
                columns : list, default [] (empty list)
                    The columns to check for null values. An empty list means all columns will be checked.
                fill_text_with : str, default 'Unknown'
                    The value to replace null values with, in text columns.
                fill_numeric_with : str, float, int, default 'mean'
                    The value to replace null values with, in numeric columns. This can be a numeric value or mean, median, mode to fill nulls with an average from the column.
                by_col_name : dict, default {} (empty dict)
                    A dictionary containing the column name as a key and the value to replace nulls with. If this argument is used, all other arguments will be ignored.
        """
        # asset item types        
        utility.assert_item_type(item=by_col_name, item_types=[dict])
        
        columns = self.__validate_column_argument(columns=columns, return_target=False)

        if not columns:
            raise ValueError('No valid columns specified, please try again.')
            
        # apply the function
        self.__convert_data_using_func(convert_func=self._fill_nulls, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, fill_text_with=fill_text_with, fill_numeric_with=fill_numeric_with, by_col_name=by_col_name)

    @__retain_transformation
    def _fill_nulls(self, *, data, columns, fill_text_with='Unknown', fill_numeric_with='mean', by_col_name:dict={}) -> pd.DataFrame:

        # if the user has specified specific values for a column, use them
        if by_col_name:
            for col, value in by_col_name.items():
                # if the column is valid fill the nulls
                if col in data.columns:
                    data = self.__filling_col_nulls(data=data, column=col, fill_val=value)
        else:
            # get the column list
            columns = self.__check_for_all_columns(columns=columns)
            # for each col, if numeric, use fill numeric, else use fill text
            for col in columns:
                if col in data.columns:
                    if is_numeric_dtype(data[col]):
                        data = self.__filling_col_nulls(data=data, column=col, fill_val=fill_numeric_with)
                    else:
                        data = self.__filling_col_nulls(data=data, column=col, fill_val=fill_text_with)

        return data

    def __get_average(self, data, average_type):

        # try and get the average from the data as per the average type
        try:
            average_type = str(average_type).lower()
            if average_type == 'median':
                output = data.median()
            elif average_type == 'mode':
                output = data.mode()[0]
            else:
                output = data.mean()
        # if there is an error, use the default average value for fails
        except Exception:
            output = pardon_options.AVERAGE_FAIL_DEFAULT_VALUE

        # series with single rows and null will return nan as the average so these need to be replaced with the default average
        if str(output) == 'nan':
            output = pardon_options.AVERAGE_FAIL_DEFAULT_VALUE
        
        return output

    def __filling_col_nulls(self, data, column, fill_val) -> pd.DataFrame:

        # determine if average required
        if str(fill_val).lower() in statics.AVERAGES or not isinstance(fill_val, (int, float)):
            use_avg = True
        else:
            use_avg = False

        # see if this column has been done before
        if column in self._null_fills:
            fill_val = self._null_fills.get(column)
            if column in data.columns:
                # replace the value
                data[column].fillna(fill_val, inplace=True)
        else:
            if is_numeric_dtype(data[column]):
                # if the mean is used, add it as replacement value else use the item provided
                if use_avg:
                    fill_val = self.__get_average(data=data[column], average_type=fill_val)

            data[column].fillna(fill_val, inplace=True) 

        # retain a record of filled values
        if column not in self._null_fills:
            self._null_fills[column] = fill_val   

        return data

    @__function_unavailable_after_data_clear
    def one_hot_encode(self, columns=[], max_items_in_category=10, remove_encoded=True):
        """
        One hot encode the columns specified if they have the max_items_in_catgeory or fewer unique values.

            Args:
                columns : list, default [] (empty list)
                    The columns to one hot encode. An empty list means all columns will be checked.
                max_items_in_category : int, str, default 10 {'all', int}
                    The maximum number of unique values to be present in the column before it will be one hot encoded. For example, if the column contained the values, 'High', 'Medium', and 'Low', that would be 3 unique values. Only applied when no columns are specified.
                remove_encoded : bool, default True
                    Remove the columns that were encoded. Use False to retain the columns that were one hot encoded (not recommended).
        """
        utility.assert_item_type(item=max_items_in_category, item_types=[int, 'all'])
        # ensure we have boolean
        utility.assert_item_type(item=remove_encoded, item_types=[bool])
        # user can put all so we can set the number of the row count
        if isinstance(max_items_in_category, str):
            if max_items_in_category.lower() == 'all':
                max_items_in_category = len(self.data)
            else:
                raise ValueError(f'{max_items_in_category} is invalid for the max_items_in_category. Pleasde pass "all" or an integer and try again.')

        # if no columns are specified, use all columns
        use_columns = self.__validate_column_argument(columns=columns, return_target=False)
        # ensure we only try to one hot encode category items and those with a valid number of items
        if not columns:
            columns = [col for col in use_columns if self.train_data[col].nunique() <= max_items_in_category and self.train_data[col].nunique() > 1 and col != self.target]
        else:
            columns = [col for col in use_columns if self.train_data[col].nunique() > 1 and col != self.target]
        # if there are no valid ohe columns
        if not columns:
            # if this isn't a rapid ml call, raise an error
            if not self._is_rapid_ml:
                raise ValueError('No columns in the column list provided are valid for one hot encoding')
            else:
                # ignore this function if from rapid ml
                return

        # apply the function
        self.__convert_data_using_func(convert_func=self._one_hot_encode, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, max_items_in_category=max_items_in_category, fit=True, remove_encoded=remove_encoded)

    @__retain_transformation
    def _one_hot_encode(self, *, data, columns, max_items_in_category=10, fit=True, remove_encoded=True) -> pd.DataFrame:
        ### max_items_in_category not used here but retain so it is recorded in the script for reference ###
        # if we need to fit the data first
        if fit:
            columns = self.__validate_column_argument(columns=columns, return_target=False, check_invalid=False)
            # create ohe object
            ohe = preprocessing.OneHotEncoder(handle_unknown='ignore', sparse=False)
            # fit the data
            self._ohe_encoder = ohe.fit(data[columns])
            # retain the input column names
            self._ohe_encoded_column_input_names.extend(columns)
            # get the column names
            self._ohe_encoded_column_new_names = list(self._ohe_encoder.get_feature_names_out())
            # # transform data to ohe
            transformed_data = ohe.transform(data[columns])
            # # # the above transformed_data is an array so convert it to dataframe
            encoded_data = pd.DataFrame(transformed_data, columns=self._ohe_encoded_column_new_names, index=data.index)
            # get the columns to keep, we remove the ohe columns if requested by the user
            non_ohe_columns = [col for col in data.columns if col not in columns] if remove_encoded else [col for col in data.columns]
            # now concatenate the original data and the encoded data
            data = pd.concat([data[non_ohe_columns], encoded_data], axis=1)
        else:
            transformed_data = self._ohe_encoder.transform(data[self._ohe_encoded_column_input_names])
            # turn the transform data back into a dataframe object
            encoded_data = pd.DataFrame(transformed_data, columns=self._ohe_encoded_column_new_names, index=data.index)
            # get the columns not used in ohe
            non_ohe_columns = [col for col in data.columns if col not in self._ohe_encoded_column_input_names] if remove_encoded else [col for col in data.columns]
            # now concatenate the original data and the transformed data
            data = pd.concat([data[non_ohe_columns], encoded_data], axis=1)

        return data

    def __check_for_type(self, *, data, columns:list, dtype) -> list:
        # only return the columns matching the specified data type

        # keep the valid columns
        columns = self.__keep_valid_columns(columns=columns)

        dtypes = utility.single_to_list(item=dtype)
        use_cols = []

        # iterate through
        for dtype in dtypes:
            if dtype == 'numeric':
                cols = [col for col in columns if col in data.columns and is_numeric_dtype(data[col])]
            elif dtype in ['date', 'datetime']:
                cols = [col for col in columns if col in data.columns and is_datetime(data[col])]
            else:
                cols = [col for col in columns if col in data.columns and data[col].dtype == dtype]
            # add the columns
            if cols:
                use_cols.extend(cols)  

        return list(set(use_cols))

    @__function_unavailable_after_data_clear
    def frequency_encode(self, columns=[]):
        """
        Frequency encode the columns specified.

            Args:
                columns : list, default [] (empty list)
                    The columns to frequency encode. An empty list means all columns will be checked.
        """
        # validate the columns
        columns = self.__validate_column_argument(columns=columns, return_target=False)

        # apply the function
        self.__convert_data_using_func(convert_func=self._frequency_encode, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, fit=True)

    @__retain_transformation
    def _frequency_encode(self, *, data, columns, fit=True) -> pd.DataFrame:

        # only retain columns that are object data type
        columns = self.__check_for_type(data=data, columns=columns, dtype='object')

        if not columns:
            raise ValueError('No columns of correct type for frequency encoding, please try again with a valid set of columns.')
        
        if fit:
            # create dict for frequency encoder object
            freq_encoded_dict = {}

            for column in columns:
                if column in data.columns:
                    # set the frequency encoder
                    fenc = category_encoders.CountEncoder()
                    # fit the frequency encoder
                    data[column] = fenc.fit_transform(data[column])
                    # set the encoder dict
                    freq_encoded_dict.update(fenc.mapping)

            # retain the fit frequency encoder
            self._frequency_encoder = freq_encoded_dict
            self._frequency_encoded_column_input_names.extend(columns)
        else:
            for column in columns:
                if column in data.columns:
                    # get the next value in the training data to apply to the test dataset during encoding
                    rep_val = self._frequency_encoder_new_item_value
                    # get the relevant mapping items from the encoder for the column specified
                    cur_dict = self._frequency_encoder.get(column, None)

                    if cur_dict is None:
                        raise KeyError(f'The column: {column}, has not been encoded, please add this column to the encoded list and try again.')
                    
                    # assign the encoded values
                    data[column] = data[column].apply(lambda x: cur_dict.get(x, rep_val))
        
        return data

    @__function_unavailable_after_data_clear
    def __adjust_columns_from_select_best(self, data) -> list:
        # will check to ensure columns havent since been removed because of select best features call
        
        # only use the items that still exist
        only_valid = [col for col in data.columns if col in self.train_data.columns]
        
        return only_valid

    @__function_unavailable_after_data_clear
    def ordinal_encode(self, columns:list=[], order_by='value', include_target=False):
        """
        Ordinal encode the columns specified.

            Args:
                columns : list, default [] (empty list)
                    The columns to Ordinal encode. An empty list means all columns will be checked.
                order_by : str, dict, list, function, default 'value', {'value', 'frequency', dict, list, func}
                    How to order the values in a column prior to encoding. Specify a dictionary containing the column name as key and how to order that column. Functions will be applied to the entire column as a list to specify the order. Frequency means the most frequently occurring item will have the highest encoded value and so on. Values not seen in training will be given the value 0.
                include_target : bool, default False
                    Include the target when not specifying columns to ordinal encode. Typically, the target should be encoded with the label encoder. 
        """
        utility.assert_item_type(item=include_target, item_types=[bool])

        if not callable(order_by):
            utility.assert_item_type(item=order_by, item_types=[str, dict, list])

        if isinstance(order_by, list) and (not columns or len(utility.single_to_list(columns)) > 1):
            raise ValueError(f'When specifying a list for ordinal encoding, a single column must be provided.')

        # validate the columns
        columns = self.__validate_column_argument(columns=columns, return_target=include_target)
        # only retain columns that are object data type
        columns = self.__check_for_type(data=self.data, columns=columns, dtype=['object', 'date'])
        # if no columns it means none will need to be label encoded
        if columns:
            # apply the function
            self.__convert_data_using_func(convert_func=self._ordinal_encode, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, order_by=order_by, fit=True)

    @__retain_transformation
    def _ordinal_encode(self, *, data, columns, order_by='value', fit=True) -> pd.DataFrame:
        """ordinal encode the columns specified"""
        # only retain columns that are object data type
        columns = self.__check_for_type(data=data, columns=columns, dtype=['object', 'date'])
        # if no columns it means none will need to be ordinal encoded
        if not columns:
            return data

        # only to be applied if the fit is occurring
        if fit:
            order_by = order_by.lower() if isinstance(order_by, str) else order_by
            # create dict for ordinal encoder object
            ordinal_encoded_dict = {}
            convert_cols = self.string_columns(data=data)
            # we ensure all object columns are fully converted to string
            # this gets recorded so we do not need to do this in the non-fit section
            self.convert_to_string(columns=convert_cols)
            # iterate through the columns
            for column in columns:
                if column in data.columns:
                    order = order_by.get(column) if isinstance(order_by, dict) else order_by
                    if order is None:
                        raise ValueError(f'The column: {column} was not found in the order_by dict. Ensure all columns are included when suing a dictionary argument and try again.')
                    
                    zipped_label_values = pardon_encode._ordinal_encoding_values(data=data[column], order_by=order_by)
                    data[column] = pd.to_numeric(data[column].apply(lambda x: zipped_label_values[x]))
                    # sort the labelled values
                    zipped_label_values = utility.sort_dictionary(zipped_label_values)
                    # set the label encoded values for that column
                    ordinal_encoded_dict[column] = zipped_label_values

                # if the target column was labelled, add it to auto ml class labels
                if column == self.target:
                    # swap the key value pairing to mimic normal encoding
                    ml_targets = {v: k for k, v in zipped_label_values.items()}
                    # sort the classes by their labelled number
                    self.class_labels = ml_targets

            # retain the fit frequency encoder
            self._ordinal_encoder = ordinal_encoded_dict
            # retain the input column names
            self._ordinal_encoded_column_input_names.extend(columns)
        else:
            for column in columns:
                # if the column is not in the training data, just replace as 1 because it was removed during k_best
                if column in data.columns:
                    # get the relevant mapping items from the encoder for the column specified
                    cur_dict = self._ordinal_encoder.get(column, None)
                    # if the cur dict isn't found, the coloumn was never encoded
                    if cur_dict is None:
                        raise KeyError(f'The column: {column}, has not been encoded, please add this column to the encoded list and try again.')
                    # values not seen in training will be given the value 0
                    rep_val = 0

                    # assign the encoded values and give the rep_val to those not found
                    data[column] = pd.to_numeric(data[column].apply(lambda x: cur_dict.get(x, rep_val)).astype(int))

        return data

    @__function_unavailable_after_data_clear
    def label_encode(self, columns=[]):
        """
        Label encode the columns specified.

            Args:
                columns : list, default [] (empty list)
                    The columns to label encode. An empty list means all columns will be checked.
        """
        # validate the columns
        columns = self.__validate_column_argument(columns=columns, return_target=True)

        # only retain columns that are object data type
        columns = self.__check_for_type(data=self.data, columns=columns, dtype=['object', 'date'])

        # if no columns it means none will need to be label encoded
        if columns:
            # apply the function
            self.__convert_data_using_func(convert_func=self._label_encode, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, fit=True)

    @__retain_transformation
    def _label_encode(self, *, data, columns, fit=True) -> pd.DataFrame:
        """label encode the columns specified"""

        # only retain columns that are object data type
        columns = self.__check_for_type(data=data, columns=columns, dtype=['object', 'date'])

        # if no columns it means none will need to be label encoded
        if not columns:
            return data

        # only to be applied if the fit is occurring
        if fit:
            # create dict for label encoder object
            label_encoded_dict = {}
            convert_cols = self.string_columns(data=data)
            # we ensure all object columns are fully converted to string
            # this gets recorded so we do not need to do this in the non-fit section
            self.convert_to_string(columns=convert_cols)
            # iterate through the columns
            for column in columns:
                if column in data.columns:
                    # set encoder
                    lenc = preprocessing.LabelEncoder()
                    # fit the encoder
                    data[column] = lenc.fit_transform(data[column])
                    # zip the classes and their corresponding transformation together
                    zipped_label_values = dict(zip(lenc.classes_, lenc.transform(lenc.classes_)))
                    # sort the labelled values
                    zipped_label_values = utility.sort_dictionary(zipped_label_values)
                    # set the label encoded values for that column
                    label_encoded_dict[column] = zipped_label_values

                # if the target column was labelled, add it to auto ml class labels
                if column == self.target:
                    # swap the key value pairing to mimic normal encoding
                    self.class_labels = {v: k for k, v in zipped_label_values.items()}

            # retain the fit frequency encoder
            self._label_encoder = label_encoded_dict
            # retain the input column names
            self._label_encoded_column_input_names.extend(columns)
        else:
            for column in columns:
                # if the column is not in the training data, just replace as 1 because it was removed during k_best
                if column in data.columns:
                    # get the relevant mapping items from the encoder for the column specified
                    cur_dict = self._label_encoder.get(column, None)
                    # if the cur dict isn't found, the coloumn was never encoded
                    if cur_dict is None:
                        raise KeyError(f'The column: {column}, has not been encoded, please add this column to the encoded list and try again.')
                    # if values were label encoded, get the max for the next item
                    if cur_dict.values():
                        # get the next value in the training data to apply to the test dataset if not found during encoding
                        rep_val = max(cur_dict.values()) + 1
                    else:
                        # if not, set to 1
                        rep_val = 1

                    # assign the encoded values and give the rep_val to those not found
                    data[column] = data[column].apply(lambda x: cur_dict.get(x, rep_val))

        return data
            
    @__function_unavailable_after_data_clear
    def columns_with_nulls(self) -> list:
        """
        Return a list of columns that contain null values.

            Returns:
                (list) : Returns a list of strings with the column names that contain null values.
        """
        nulls = utility.columns_with_nulls(data=self.train_data)
        
        return nulls
    
    @__function_unavailable_after_data_clear
    def numeric_columns(self) -> list:
        """
        Return a list of columns that have a numeric data type.

            Returns:
                (list) : Returns a list of strings with the column names that have a numeric data type.
        """
        # get the numeric columns
        numerics = utility.numeric_columns(data=self.train_data)

        return numerics
    
    @__function_unavailable_after_data_clear
    def string_columns(self, data=None) -> list:
        """
        Return a list of columns that have an object data type.

            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame, default None
                    The data to check for columns with for text/object data types. If no data is specified, the training data will be used.

            Returns:
                (list) : Returns a list of strings with the column names that have an object data type.
        """
        
        data = self.train_data if data is None else data
        
        return data.select_dtypes(include='object').columns.tolist()
    
    @__function_unavailable_after_data_clear
    def remove_rows_containing(self, column_items:dict):
        """
        Remove rows that contain a specific value in the specified columns.

            Args:
                column_items : dict
                    A dictionary object with the column name as a key and the value to look for as the value. Rows in the column specified containing that value will be dropped. Multiple values can be specified in the form of a list. To remove rows with non-numeric values, pass 'non-numeric'. You can also pass a function that if returns a value or True, that row will be dropped.
        """        
        utility.assert_item_type(item=column_items, item_types=[dict])
        
        if not column_items:
            raise ValueError('Please pass a dictionary item containing the rows you wish to remove')
        
        invalid = [col for col in column_items.keys() if col not in self.columns]
        
        if invalid:
            raise KeyError(f'the columns: "{", ".join([str(x) for x in invalid])}" do not exist in the dataset. Please confirm your column choices and try again.')
            
        # remove rows for training and test data and the x, y split occurred at instantiation
        self.__convert_data_using_func(convert_func=self._remove_rows_containing, apply_convert_to_train=True, apply_convert_to_test=True, column_items=column_items)

    @__retain_transformation 
    @__ignore_function_in_transforms
    def _remove_rows_containing(self, *, data, column_items:dict) -> pd.DataFrame:

        for col, value in column_items.items():
            # if value not a list, make it a single item list
            value = utility.single_to_list(item=value)
            
            if col in data.columns:
                # iterate and remove all values to be removed for specified column
                for val in value:
                    # if removing non numeric
                    if val == 'non-numeric':
                        data = data[pd.to_numeric(data[col], errors='coerce').notnull()]
                    elif callable(val):
                         data = data[data[col].apply(lambda x: utility._InvalidFunction(function='Callable') if val(x) else x).map(type) != utility._InvalidFunction]
                    else:
                        data = data[data[col] != val]            
        return data

    @__function_unavailable_after_data_clear
    @__retain_transformation
    @__ignore_function_in_transforms
    @__non_data_func
    def create_class_labels(self, class_labels:dict):
        """
        Create string class labels for numeric classes in data. This means you can rename your classes something more relevant while retaining the specific numeric values during model training. Note, this is only applicable for classification models.

            Args:
                class_labels : dict
                    A dictionary containing the current, numeric class names as the dictionary  keys, and the new string class label as the value. You must ensure every numeric class item is included and all new string class labels are unique.
        """
        # not available to regression tasks
        if self._is_regression:
            raise Exception('This function is only available for classification models.')

        utility.assert_item_type(item=class_labels, item_types=[dict])
        
        if not class_labels:
            raise ValueError('Please pass a dictionary item containing the columns you wish to encode, and the values to encode with.')

        # get the class keys
        class_keys = class_labels.keys()

        # check that all classes are numeric
        if not utility.all_numeric(data_list=class_keys) or not utility.all_numeric(data_list=self.classes()):
            raise ValueError('This function is for creating string labels for numeric classes. Ensure all your classes are numeric before using this feature.')

        # get the classes
        classes = self.classes()
        # check if all classes are accounted for
        result = all(x in class_keys for x in classes)

        # if all items are not present and the 2 lists are the same, raise an error
        if not result or (len(classes) != len(class_keys)):
            raise ValueError(f'Ensure you include a class label for every class in the {self.target} column. Check each class is present and that you do not have any extra classes that are not in the data in your class_labels dictionary keys.\nYou have the following classes in your data: {classes}')

        # ensure the values are strings
        class_labels = {k: str(v) for k, v in class_labels.items()}
        # update the class labels dictionary
        self.class_labels = class_labels

    @__retain_transformation
    def _custom_encode(self, *, data, encode_items:dict) -> pd.DataFrame:
        
        # if the mapping items is not a dict, ignore the function
        if not isinstance(encode_items, dict) or not encode_items:
            return data

        # map the column with the new values
        for column, encode_dict in encode_items.items():
            if column in self.columns:
                data[column] = data[column].apply(lambda x: encode_dict.get(x))
                
        return data
    
    @__function_unavailable_after_data_clear
    def map_column_values(self, mapping_items:dict):
        """
        Map values in a specified column to a new value. All values must be present in the mapping items value else null will be returned. Think of this as equivalent to Excel's vlookup function.
            
            Args:
                mapping_items : dict
                    A dictionary object with the column name as a key and the value as another dictionary object containing how you want values to be mapped.
        """
        utility.assert_item_type(item=mapping_items, item_types=[dict])
        utility.assert_item_type(item=list(mapping_items.values())[0], item_types=[dict])
        
        if not mapping_items:
            raise ValueError('Please pass a dictionary item containing the values you wish to map')
        
        # apply the mapping
        self.__convert_data_using_func(convert_func=self._map_column_values, apply_convert_to_train=True, apply_convert_to_test=True, mapping_items=mapping_items)
    
    @__retain_transformation
    def _map_column_values(self, *, data, mapping_items:dict) -> pd.DataFrame:
        
        # if the mapping items is not a dict, ignore the function
        if not isinstance(mapping_items, dict) or not mapping_items:
            return data

        # map the column with the new values
        for column, map_dict in mapping_items.items():
            if column in self.columns:
                data[column] = data[column].apply(lambda x: map_dict.get(x))
                
        return data  
    
    @__function_unavailable_after_data_clear
    def replace_values(self, replace_columns:dict):
        """
        Replace values in the column specified with another value.
            
            Args:
                replace_columns : dict
                    A dictionary object with the column name as a key and the value as a dictionary containing the key as the value to find and the value as the value to replace with.
        """
        utility.assert_item_type(item=replace_columns, item_types=[dict])
        # check that the values part is too a dictionary
        utility.assert_item_type(item=list(replace_columns.values())[0], item_types=[dict])
        # ensure replace columns contains values
        if not replace_columns:
            raise ValueError('Please pass a dictionary item containing the columns you wish to replace values')
        
        self.__convert_data_using_func(convert_func=self._replace_values, apply_convert_to_train=True, apply_convert_to_test=True, replace_columns=replace_columns)

    @__retain_transformation
    def _replace_values(self, *, data, replace_columns:dict) -> pd.DataFrame:
        for column, replacing_items in replace_columns.items():
            # if the column exists in the data
            if column in data.columns:
                # for each item in the dictionary, replace
                for replace, replace_with in replacing_items.items():
                    # if using a function, apply it to the relevant rows
                    if callable(replace):
                        if callable(replace_with):
                            data[column] = data[column].apply(lambda x: replace_with(x) if replace(x) else x)
                        else:
                            # this will replace the item if it meets the requirements as per the lambda
                            data[column] = data[column].apply(lambda x: replace_with if replace(x) else x)
                    elif callable(replace_with):
                        data[column] = data[column].apply(lambda x: replace_with(x) if x == replace else x)
                    else:
                        data[column] = data[column].replace([replace], [replace_with])
        return data
    
    def __keep_valid_columns(self, columns) -> list:
        
        #  keep valid columns only
        columns = self.columns if not columns else columns
        # get valid
        valid = [col for col in columns if col in self.columns]
        # remove duplicates
        valid = list(set(valid)) if valid else valid
        
        return valid
    
    @__function_unavailable_after_data_clear
    def remove_columns(self, columns:list):
        """
        Remove the columns specified.

            Args:
                columns : list
                    A list of the columns to be removed.
        """
        # only try this if columns have been passed through
        utility.assert_item_type(item=columns, item_types=[list])

        if not columns:
            raise ValueError('Please provide at least 1 column and try again.')

        # get valid columns
        columns = self.__validate_column_argument(columns=columns, return_target=False)

        if not columns:
            raise KeyError('The columns provided are invalid')
        
        # keep the valid columns only
        valid_columns = self.__keep_valid_columns(columns=columns)
        # get the invalid items
        any_invalid = list(set(columns).difference(set(valid_columns)))

        # remove the columns from the datasets 
        self.__convert_data_using_func(convert_func=self._remove_columns, apply_convert_to_train=True, apply_convert_to_test=True, columns=valid_columns)
        
        if any_invalid:
            print(f'WARNING: The following columns were invalid and ignored in removal: {", ".join([str(x) for x in any_invalid])}')
    
    @__retain_transformation
    def _remove_columns(self, *, data, columns) -> pd.DataFrame:
        """remove any columns specified"""  
        # ensure only valid columns are passed
        columns = self.__validate_column_argument(columns=columns, return_target=False, check_invalid=False)
        # ensure only columns that exist will be dropped
        columns = [col for col in columns if col in  data.columns]
        
        return data.drop(labels=columns, axis='columns')

    @__function_unavailable_after_data_clear
    def rename_columns(self, column_names:dict):
        """
        Rename the columns specified.

            Args:
                column_names : dict
                    A dictionary object with the key as the old column name and the value as the new column name.
        """
        utility.assert_item_type(item=column_names, item_types=[dict])
        
        # get any incorrect or invalid columns
        any_invalid = [col for col in column_names.keys() if col not in self.columns]
        
        if any_invalid:
            # delete any invalid items
            for col in any_invalid:
                del column_names[col]
        
        # rename the columns
        self.__convert_data_using_func(convert_func=self._rename_columns, apply_convert_to_train=True, apply_convert_to_test=True, column_names=column_names)

        # if the target column was renamed, rename the target attribute
        if self.target in column_names.keys():
            self.target = column_names[self.target]

         # warn the user if any invalid column names were found
        if any_invalid:
            print(f'WARNING: The following columns were not found and ignored in renaming: {", ".join([str(x) for x in any_invalid])}')
    
    @__retain_transformation
    def _rename_columns(self, *, data, column_names:dict) -> pd.DataFrame:
        """specify the column current name and new name to be renamed"""

        # use pandas rename method
        data = data.rename(columns=column_names)

        # update the cluster column
        if self._cluster_column_name in column_names:
            self._cluster_column_name = column_names[self._cluster_column_name]

        return data

    @__function_unavailable_after_data_clear
    def create_bins(self, column:str, interval, min_value='auto', max_value='auto', new_column:str=None, fill_empty='mode'):
        """
        Create bins from the column specified. This means a group value for each number, such as 0-5, 5-10, 10-15 and so on. Please note, the bins are inclusive of the max value for each bin, so a value of 5, would be placed into the 0-5 bin.

            Args:
                column : str
                    The numeric column to create your bins from.
                interval : int, float
                    The interval between bins. For example, 5 would produce bins 5, 10, 15, 20 and so on.
                min_value : str, int, float, default 'auto' {'auto' , int, float}
                    The minimum value of your group for bins. For example, if you specified 5, intervals would start from 5 and increase by the interval. Using auto will take the minimum value from the column.
                max_value : str, int, float, default 'auto' {'auto' , int, float}
                    The maximum value of your group for bins. For example, if you specified 100, intervals would increase to 100 from the min_value by the interval. Using auto will take the maximum value from the column.
                new_column : str, None, default None
                    The name of the column to be created with the bins. Leaving this as None will mean the column in the column argument will be overwritten.
                fill_empty : str, int, float, default 'mode' {'mean', 'median', 'mode', int, float}
                    Nulls cannot be binned and so must be filled. Use this argument to determine the value to fill nulls with should they be encountered. This is required even if your column contains no nulls as a defence against future data containing nulls and resulting in an error.
        """

        # assert data types
        utility.assert_item_type(item=column, item_types=[str])
        utility.assert_item_type(item=min_value, item_types=[str, float, int])
        utility.assert_item_type(item=max_value, item_types=[str, float, int])
        utility.assert_item_type(item=interval, item_types=[float, int])
        utility.assert_item_type(item=new_column, item_types=[str, None])
        utility.assert_item_type(item=fill_empty, item_types=[str, int, float])

        # overwrite the column if new column is none
        if new_column is None:
            new_column = column

        if isinstance(fill_empty, str):
            fill_empty = fill_empty.lower()
            if fill_empty not in statics.AVERAGES:
                raise ValueError(f'Specify a numeric value to fill nulls or use one of the following: {statics.AVERAGES}')

        # check if users have passed strings for min or max
        for check_value in [min_value, max_value]:
            if isinstance(check_value, str):
                check_value = check_value.lower() 
                if check_value != 'auto':
                    raise ValueError(f'Specify a numeric value or use "auto" to use all available values from the column.')

        # ensure the column is valid
        if column not in self.columns:
            raise ValueError(f'The column: {column} is not in the available columns. Please choose from the following and try again: {[col for col in self.columns if col != self.target]}')
        if column == self.target:
            raise ValueError(f'You cannot create bins for the target column: {column}. Change the column and try again.')
        
        # ensure the column is numeric
        if not is_numeric_dtype(self.data[column]):
            raise TypeError(f'The column: {column} is not numeric. Choose from the following numeric columns: {self.numeric_columns()}')   

        # get the min and max values if user selected auto
        if isinstance(min_value, str):
            min_value = np.nanmin(self.data[column].values)
        if isinstance(max_value, str):
            max_value = np.nanmax(self.data[column].values) + 1

        # check interval doesn't take min to over max in 1 jump
        if min_value + interval >= max_value:
            raise ValueError(f'The interval: {interval} is too large for a min value of {min_value} and a max_value of {max_value}. Change the min and max or interval and try again.')

        # check the integer levels
        int_check = (max_value - min_value) / interval

        # if too many intervals will be created, fail
        if int_check > 100:
            raise ValueError(f'{round(int_check)} bins will be created which is too many. Please increase your interval size and try again.')

        # fill nulls so there is a record of it in case predictions contain nulls
        self.fill_nulls(columns=column, fill_numeric_with=fill_empty)
        # set the intervals and labels
        intervals = utility.create_intervals(start=min_value, end=max_value, interval=interval)
        labels = utility.create_interval_labels(intervals=intervals)
        # we need to reduce the min so it gets picked up
        # for example, unless we do -1, 0 would not fall into the 0-10 bin
        less_value = 1 if isinstance(interval, int) else interval
        intervals[0] = intervals[0] - less_value
        # always set the final interval to be inf to deal with larger values
        intervals[-1] = np.inf
        # assign the data
        self.__convert_data_using_func(convert_func=self._create_bins, apply_convert_to_train=True, apply_convert_to_test=True, column=column, intervals=intervals, labels=labels, new_column=new_column)

    @__retain_transformation
    def _create_bins(self, *, data, column, intervals, labels, new_column) -> pd.DataFrame:
        """create bins for a numeric column"""
        # round up any values that aren't integers
        test_col_name = f'{column}_temp_for_max_ceil_val'
        data[test_col_name] = np.ceil(data[column]).astype(int)
        # assign the bins and add labels
        data[new_column] = pd.cut(data[test_col_name], bins=intervals, labels=labels)
        # make the columns str
        data = data.astype({f'{new_column}': str})
        # drop the temp column
        data.drop(labels=[test_col_name], axis='columns', inplace=True)
        # set the output attribute
        return data

    @__function_unavailable_after_data_clear
    def make_upper_case(self, columns=[]):
        """
        Make the values in the columns specified upper case.

            Args:
                columns : list
                    A list of the columns to make the values in upper case. If no columns are supplied, all text columns will be made upper case.
        """
        
        # validate the columns argument - this ensure all columns are given if none are specified
        columns = self.__validate_column_argument(columns=columns, return_target=False)
        
        # retain only valid columns
        columns = self.__keep_valid_columns(columns=columns)

        # only retain columns that are object data type
        columns = self.__check_for_type(data=self.data, columns=columns, dtype='object')

        # if there are valid columns
        if columns:
            # set the data
            self.__convert_data_using_func(convert_func=self._make_upper_case, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns)

    @__retain_transformation    
    def _make_upper_case(self, *, data, columns) -> pd.DataFrame:
        # make all columns upper case   
        for col in columns:
            # ensure the data is object type
            if data[col].dtype == 'object':
                data[col] = data[col].str.upper()
                
        # return formatted data        
        return data
    
    @__function_unavailable_after_data_clear
    def pca(self, n_components=2):
        """
        Use Principal Component Analysis to reduce the number of features in the dataset through dimensionality reduction. Note, this will only be applied to data just before model training and the underlying data will not be permanently transformed.

            Args:
                n_components : int, default 2
                    An integer of the number of components to reduce the data columns to. 2 means 2 columns will remain in your data.
        """
        
        # ensure the n_components is an integer value
        utility.assert_item_type(item=n_components, item_types=[int])
        
        # ensure n components is 1 or more
        if n_components < 1:
            raise ValueError('n_components for PCA cannot be less than 1, please change this value and try again.')
        
        # set the flag that pca will be performed
        self._perform_pca = True
        self._pca_components = n_components
    
    def _pca(self, X_data, fit=True) -> pd.DataFrame:

        #perform the pca
        # check that if a transform has been called, that a pca exists
        if self._pca is None and not fit:
            raise ValueError('Cannot use PCA until the PCA object is created. Use fit=True before using fit=False')
        
        # only transform when required
        if fit:
            # create the pca object
            pca = PCA(n_components=self._pca_components)
            # set the scaler so it can be reused
            self._pca_encoder = pca.fit(X_data)

        # pca the data 
        X_data = self._pca_encoder.transform(X_data)
        
        # set the pca column names
        pca_columns = [f'pca_{i}' for i in range(1, self._pca_components + 1)]
        
        # set the data back into a datadframe
        X_data = pd.DataFrame(X_data, columns=pca_columns)

        return X_data

    # not decorating this as it can just return None
    def get_sample_rows(self, n_rows=1, include_target=False, as_json=False) -> pd.DataFrame:
        """
        Return a random row from the raw input data.

            Args:
                n_rows : int, default 1
                    The number of sample rows to return. If n_rows is more than the number of available rows, all rows will be returned.
                include_target : bool, default False
                    Include the target column in the returned sample row.
                as_json : bool, default False
                    Return the data in json format.

            Returns:
                (pandas.DataFrame, str) : pandas.DataFrame or str in json format, containing n number of rows as requested.
        """
        # if there is no raw data, return none
        if not hasattr(self, 'raw_data') or self.raw_data is None or len(self.raw_data) == 0:
            return None

        # ensure argument types
        utility.assert_item_type(item=n_rows, item_types=[int, str])
        utility.assert_item_type(item=include_target, item_types=[bool])
        utility.assert_item_type(item=as_json, item_types=[bool])

        # if a string supplied, ensure it is only all
        if isinstance(n_rows, str):
            n_rows = n_rows.lower()
            if n_rows != 'all':
                raise ValueError(f'The n_rows argument only takes an integer or "all". {n_rows} is invalid.')

        # check the total number of rows
        total_rows = len(self.raw_data)
        # set n_rows to be the total number if n_rows is more
        n_rows = total_rows if n_rows == 'all' or n_rows > total_rows else n_rows
        # return a sample row from the raw data
        data = self.raw_data.sample(n=n_rows).copy()
        # reset the index
        data.reset_index(inplace=True, drop=True)

        # if we are not including target, return a row without
        if not include_target:
            data = data.loc[:, data.columns != self.target]

        # if user requested json, convert to json
        if as_json:
            data = utility.to_json(object_to_json=data)

        return data

    def __scalers(self) -> dict:
        # return the available scalers
        scalers = {'standard_scaler': preprocessing.StandardScaler(),
                   'min_max_scaler': preprocessing.MinMaxScaler(),
                   'max_abs_scaler': preprocessing.MaxAbsScaler(),
                   'robust_scaler': preprocessing.RobustScaler()}

        return scalers

    @__function_unavailable_after_data_clear
    def scale_data(self, columns=[], scaler_type='standard_scaler'):
        """
        Scale the data.

            Args:
                columns : str, list, default [] (empty list)
                    The name(s) of the column(s) to scale. If left empty all columns (excluding target) will be scaled.
                scaler_type : str, default 'standard_scaler' {'standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'robust_scaler'}
                    The type of scaler to use. Can use standard_scaler, min_max_scaler, or max_abs_scaler.
        """
        utility.assert_item_type(item=scaler_type, item_types=[str])

        scaler_type = scaler_type.lower() 

        if self.target is not None and self.target not in self.columns:
            raise KeyError(f'Target column: {self.target} not found in the column list, please ensure when columns are renamed you update the target column parameter using class.target=<new name> and try again')
                    
        # remove the target column from the column lists and the ohe columns
        numeric_cols = [col for col in self.numeric_columns() if col not in self._ohe_encoded_column_input_names and col != self.target]
        all_cols = [col for col in self.columns if col not in self._ohe_encoded_column_input_names and col != self.target]   
        
        # if using columns, only check the ones that are being scaled
        if columns:
            numeric_cols = [col for col in numeric_cols if col in columns]
            all_cols = columns

        # if the lists don't match it means some columns are not numeric
        if sorted(numeric_cols) != sorted(all_cols):
            raise Exception('All data columns (excluding target) must be numeric before scaling. Please encode columns and try again.')

        # check the correct scaler is being used
        if scaler_type not in self.__scalers().keys():
            raise ValueError(f'Invalid scaler_type. Please use one of the following and try again: {list(self.__scalers().keys())}')

        # if no columns are given, use all columns, else ensure no columns are invalid
        columns = numeric_cols if not columns else self.__validate_column_argument(columns=columns, return_target=False)
        
        # scale the data
        self.__convert_data_using_func(convert_func=self._scale_data, apply_convert_to_train=True, apply_convert_to_test=True, scaler_type=scaler_type, columns=columns, fit=True)
    
    @__retain_transformation
    def _scale_data(self, *, data, scaler_type, columns, fit=True) -> pd.DataFrame:

        # check that if a transform has been called, that a scaler exists
        if self._scaler is None and not fit:
            raise ValueError('Cannot scale data before the scaler is created. Use fit=True before using fit=False')

        # set the text to lower case
        scaler_type = str(scaler_type).lower()
        # double check the columns
        columns = self.__validate_column_argument(columns=columns, return_target=False, check_invalid=False)
        # only transform when required
        if fit:
            # get the scaler
            scaler = self.__scalers()[scaler_type]
            # log the scaler we used
            self.scaler_used = scaler_type
            # set the scaler so it can be reused
            self._scaler = scaler.fit(data[columns])

        # scale the data 
        data[columns] = self._scaler.transform(data[columns])
        # if columns have not been present for the scaler, they will return as nan, set them to 0
        data[columns] = data[columns].fillna(value=0)

        return data
        
    def _X_y_values(self, data=None, dataset='train_data'):
        
        # get the data set
        data = getattr(self, dataset).copy() if data is None else data.copy()

        # if the data contains the target column, return that else pick the last column as it wont be used
        if self.target is None and self._holder_target is None:
            self._holder_target = data.columns[-1]

        target_col = self.target if self.target is not None else self._holder_target
        X = data.loc[:, data.columns != target_col]
        # if y is present, take it else return null - it is likely that during the predict method, this will not be present
        y = data[target_col] if target_col in data.columns else None

        return X, y

    def _process_can_start(self, on_error:str, check_rows=True):

        if check_rows:
            # ensure there is some data
            if len(self.train_data) == 0:
                raise ValueError(f'The training data contains 0 rows. Please ensure you retain training data and try again.')

        # ensure all columns are numeric
        if sorted(self.numeric_columns()) != sorted(self.columns):
            raise ValueError(f'{on_error}')

    @__function_unavailable_after_data_clear
    def apply_func(self, *, func, column=None, new_column=None, func_name=None, **kwargs):
        """
        Create a new column or overwrite a column by applying a lambda expression or a custom function to an existing column. This function is applied to every row individually in the specified column.

            Args:
            func : lambda expression, function
                    The lambda expression or function to apply to every row in the column argument. If using a function, supply it in an uninstantiated format.
                column : str, None, default None
                    The name of the column to apply the lambda expression or custom function. If None, all columns will be passed in the function.
                new_column : str, None, default None
                    The name of new column to be created by applying the lambda expression or function to the column. If left as None, the original column will be overwritten. If not specifying a column argument, a new_column must be provided.
                func_name : str, default None
                    Give a custom name to your transformation for reference in the Model Script and Model Diagram.
                **kwargs : kwargs
                    Any keyword arguments required for your function.
        """
        utility.assert_item_type(item=column, item_types=[str, None])
        utility.assert_item_type(item=new_column, item_types=[str, None])

        # ensure no reserved keyword arguments are being used
        pardon_transforms._validate_kwargs_reserved_words(kwargs)

        if column is None and new_column is None:
            raise ValueError(f'If not providing a column name argument, the new_column name argument must be provided.')

        # ensure the func argument is callable and therefore a function
        if not callable(func):
            raise TypeError('You must pass a lambda expression or function into the func argument to use this method.')
        
        if column is not None and column not in self.train_data.columns:
            raise ValueError(f'The column: {column} does not appear in the dataset. Please choose a valid column from the following: {self.columns}')

        # set the new column to be the column if it is None
        new_column = column if (new_column is None and column is not None) else new_column

        # add the func name
        func_name = func_name if func_name is not None else str(func.__name__)

        # apply the lambda function to all of the datasets
        self.__convert_data_using_func(convert_func=self._apply_func, apply_convert_to_train=True, apply_convert_to_test=True, column=column, new_column=new_column, func=func, func_name=func_name, kwargs=kwargs)

    @__retain_transformation
    def _apply_func(self, *, data, column, func, new_column, func_name, **kwargs) -> pd.DataFrame:
        # func_name is used by retain_transformation
        # get any kwargs
        kwargs = kwargs.get('kwargs')
        # create new column using specified lambda
        if column is not None:
            data[new_column] = data[column].apply(func, **kwargs)
        else:
            data[new_column] = data.apply(func, axis=1, **kwargs)

        return data
    
    @__function_unavailable_after_data_clear
    def add_func(self, *, func, apply_to_train=True, apply_to_test=True, reconcile=True, func_name=None,**kwargs):
        """
        Add a customised function to your entire dataset. This will apply your function to the dataset as a whole, giving you entire flexibility over the output. The function must take a pandas.DataFrame as its first argument, and must return a pandas.DataFrame. If making significant changes such as removing columns etc, it is strongly recommended to do this last to prevent contention and use the in-built methods available where possible.

            Args:
                func : lambda expression, function
                    The lambda expression or function to apply to the dataset.
                apply_to_train : bool, default True
                    Apply the function to the training dataset.
                apply_to_test : bool, default True
                    Apply the function to the testing dataset.
                reconcile : bool, default True
                    Test and reconcile the function. This means it will be run and tested and will take longer but ensures it is valid.
                func_name : str, default None
                    Give a custom name to your transformation for reference in the Model Script and Model Diagram.
                **kwargs : kwargs
                    Any keyword arguments required for your function.
        """
        # assert function
        utility.assert_item_type(item=apply_to_train, item_types=[bool])
        utility.assert_item_type(item=apply_to_test, item_types=[bool])
        utility.assert_item_type(item=reconcile, item_types=[bool])

        # ensure no reserved keyword arguments are being used
        pardon_transforms._validate_kwargs_reserved_words(kwargs)

        # ensure the result gets applied to both datasets
        if all([not apply_to_train, not apply_to_test]):
            raise ValueError('Both apply_to_train and apply_to_test are set to False so this function will not do anything. Change one of these and try again.')

        # ensure the func argument is callable and therefore a function
        if not callable(func):
            raise TypeError('You must pass a lambda expression or function into the func argument to use this method.')

        # get a value back from the function
        if reconcile:
            pre_rows = len(self.train_data)
            test_func = func(self.train_data.copy(), **kwargs)
             # ensure it is a data frame
            if not isinstance(test_func, pd.DataFrame):
                raise TypeError('Your function does not return a pandas DataFrame and so is invalid. Please ensure your function accepts and returns a pandas dataframe and try again.')
            # get post row count for reconcilliation
            post_rows = len(test_func)
            # error if the rows do not match as this means rows were removed during the function
            if pre_rows != post_rows:
                raise Exception(f'The function removes rows and is therefore invalid because it could remove rows in prediction data causing errors. {pre_rows - post_rows} were removed. Remove rows using inbuilt Pardon methods or apply this function prior to Pardon instantiation.')
        
        # add the func name
        kwargs['func_name'] = func_name if func_name is not None else str(func.__name__)

        # apply the function result to all of the datasets
        if apply_to_train:
            self.__convert_data_using_func(convert_func=self._add_func, apply_convert_to_train=True, apply_convert_to_test=False, func=func, **kwargs)
        if apply_to_test:
            self.__convert_data_using_func(convert_func=self._add_func, apply_convert_to_train=False, apply_convert_to_test=True, func=func, **kwargs)

    @__retain_transformation
    def _add_func(self, *,  data, func, func_name, **kwargs) -> pd.DataFrame:
        # func name is used by retain_transformation
        # create new column using specified function
        data = func(data, **kwargs)

        return data

    @__function_unavailable_after_data_clear
    def split_column(self, split_column:str, new_columns:list, sep=',', drop_split_column:bool=False):
        """
        Split the data by a separator into new columns.

            Args:
                split_column : str
                    The name of the column containing the values you wish to split.
                new_columns : list
                    The names of the new columns you wish to create from the split values. Note, there must be at least the number of new columns as there are separators. For example, if the row with the most separators contains 3 separators, this would mean 4 new columns are required to place the split data.
                sep : str, default ','
                    The separator used to split the values in the split column.
                drop_split_column : bool, default False
                    Drop the split column after the new columns have been created.
        """
        # ensure data types
        utility.assert_item_type(item=new_columns, item_types=[list])
        utility.assert_item_type(item=split_column, item_types=[str])
        utility.assert_item_type(item=sep, item_types=[str])
        utility.assert_item_type(item=drop_split_column, item_types=[bool])
        
        # ensure we're not creating new columns from the target column to avoid errors during predictions
        if self.target == split_column:
            raise KeyError(f'The target column {self.target} cannot be used in this transformation as it may not be present during predictions.')

        if split_column not in self.data.columns:
            raise KeyError(f'The split column {split_column} is not in the data. Please choose from the following columns and try again:\n{list(self.data.columns)}')
        
        # get the occurrences of the sep in the column - + 1 as a single instance of the separator requires 2 columns
        counts = max(self.data[split_column].str.count(sep)) + 1

        # ensure the separator exists
        if counts == 1:
            raise ValueError(f'The separator {sep} does not appear in the column: {split_column}. Please specify as new separator using the sep argument and try again.')

        # if the split will create more columns than specified, raise an error
        if counts > len(new_columns):
            raise ValueError(f'The split will create {counts} new columns but you have only supplied column names for {len(new_columns)} new columns. Ensure there are at least {counts} column names in the new_columns parameter and try again.')

        # apply the transformation to each dataset
        self.__convert_data_using_func(convert_func=self._split_column, apply_convert_to_train=True, apply_convert_to_test=True, split_column=split_column, new_columns=new_columns, sep=sep)

        # if requested, drop the split column
        if drop_split_column:
            self.remove_columns(columns=[split_column])

    @__retain_transformation
    def _split_column(self, *, data, split_column, new_columns, sep=',') -> pd.DataFrame:
        
        # get the max counts
        counts = max(data[split_column].str.count(sep)) + 1

        # if there are fewer than the number of columns, take the first n cols and set the others to null
        if counts < len(new_columns):
            # get the first columns
            use_columns = new_columns[:counts]
            null_columns = new_columns[counts:]
            # set the columns and null columns
            data[use_columns] = data[split_column].str.split(sep, expand=True)
            # this sets values to none
            data[null_columns] = np.nan
            # this sets values to nan
            data[null_columns].fillna(value=np.nan)
        else:
            # create new column as a concatenation
            data[new_columns] = data[split_column].str.split(sep, expand=True)
            # ensure any Nones are replaced with nan
            data[new_columns].fillna(value=np.nan)

        return data

    @__function_unavailable_after_data_clear
    def combine_columns(self, column_1, column_2, new_column, sep=','):
        """
        Create a new column by combining the values in column_1 and column_2 with a given separator.

            Args:
                column_1 : str
                    The name of the first column to combine values from.
                column_2 : str
                    The name of the second column to combine values from.
                new_column : str
                    The name of the column to be created as a combination of values in column_1 and column_2.
                sep : str, default ','
                    The separator used to separate the values in column_1 and column_2.
        """
        # ensure we're not creating new columns from the target column to avoid errors during predictions
        if self.target in [column_1, column_2]:
            raise KeyError(f'The target column {self.target} cannot be used in this transformation as it may not be present during predictions.')
        
        # apply the transformation to each dataset
        self.__convert_data_using_func(convert_func=self._combine_columns, apply_convert_to_train=True, apply_convert_to_test=True, column_1=column_1, column_2=column_2, new_column=new_column, sep=sep)

    @__retain_transformation
    def _combine_columns(self, *, data, column_1, column_2, new_column, sep=',') -> pd.DataFrame:
        # create new column as a concatenation
        data[new_column] = data[column_1].astype(str) + str(sep) + data[column_2].astype(str)
        
        return data

    @__function_unavailable_after_data_clear
    def remove_stop_words(self, columns=[]):
        """
        Removes “stop words” from text. These are words that are typically filtered prior to processing of natural language, such as: “a”, “the”, “is”, “are”.

            Args:
                columns : list, default [] (empty list)
                    The columns to remove stop words from. An empty list means all string columns will be checked for stop words.
        """
        # validate the columns argument - this ensure all columns are given if none are specified
        columns = self.__validate_column_argument(columns=columns, return_target=False)
        # retain only valid columns
        columns = self.__keep_valid_columns(columns=columns)
        # only retain columns that are object data type
        columns = self.__check_for_type(data=self.data, columns=columns, dtype='object')

        # if there are valid columns
        if columns:
            # apply the transformation to each dataset
            self.__convert_data_using_func(convert_func=self._remove_stop_words, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns)

    @__retain_transformation
    def _remove_stop_words(self, *, data, columns) -> pd.DataFrame:
        # remove stop words
        for column in columns:
            if column in data.columns:
                data[column] = data[column].astype(str).apply(nfx.remove_stopwords)

        return data

    @__function_unavailable_after_data_clear
    def drop_duplicates(self, columns=[]):
        """
        Drop duplicate rows. If columns are specified, only duplicates occurring across those columns will be included.

            Args:
                columns : list, default [] (empty list)
                    A list of the columns to compare for duplicates. If no columns are supplied, all columns will be included when looking for duplicates.
        """
        # validate the columns argument - this ensure all columns are given if none are specified
        columns = self.__validate_column_argument(columns=columns, return_target=True)
        # retain only valid columns
        columns = self.__keep_valid_columns(columns=columns)

        # apply the transformation to each dataset
        self.__convert_data_using_func(convert_func=self._drop_duplicates, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns)

    @__retain_transformation
    @__ignore_function_in_transforms
    def _drop_duplicates(self, *, data, columns) -> pd.DataFrame:
        # drop duplicates
        data.drop_duplicates(subset=columns, inplace=True)

        return data

    def __default_required(self) -> bool:
        # check to see if the default model is the same as the default of that model class

        # get the default model so we can compare
        default_model = self.__default_model(set_params=True) 
        # get the model objects
        model_objects = self.__rapid_ml_models().keys()

        # iterate through all the models
        for mod in model_objects:
            # if the model has the same parameters as the default model, return false as there is no point to train the same model twice
            if mod.__dict__ == default_model.__dict__:
                return False

        return True

    def __get_rapid_ml_test_vals(self, model_performance, score_metric) -> dict:

        output = {k: v['model_test_scores'][score_metric] for k, v in model_performance.items() if score_metric in v['model_test_scores'].keys()}

        return output

    @__function_unavailable_after_data_clear
    @__block_null_target
    def __train_multiple_models(self, models=[], ignore_models=[], find_best_model_parameters=False, eval_metric='accuracy', max_n_iterators=None, scale_imbalanced=True, score_metric='accuracy', cross_validation=True, n_splits=10, n_repeats=1, model_params:dict=None):
        # check to see if the default will be included
        include_default = self.__default_required()
        ignore_models = [str(mod).lower() for mod in ignore_models]
        # set a dictionary to capture performance of all the models
        model_performance = collections.defaultdict(dict)
        # get all the models
        all_models = list(self.__rapid_ml_models().keys())
        all_model_names = [type(x).__name__ for x in all_models]

        # if the user has specified all or a single item list with all, set all models
        if isinstance(models, str):
            if models.lower() == 'all':
                models = all_model_names
        # if all was in the list, or models was empty, set it to all models 
        elif isinstance(models, list):
            if 'all' in [str(x).lower() for x in models] or not models:
                models = all_model_names

        # ensure the item is a list
        models = utility.single_to_list(item=models)

        if models:
            # set all to be lower case to account for case
            models = [mod.lower() for mod in models]
            # get a lidst of invalid models
            invalid = [mod.lower() for mod in models if mod.lower() not in [type(m).__name__.lower() for m in all_models] and mod.lower() != 'default']
            # if any are invalid, ignore them
            if invalid:
                models = [mod.lower() for mod in models if mod.lower() not in invalid]
            # if the user specified invalid models ignore them
            if not models:
                raise KeyError(f'No valid model types have been specified or are applicable for this dataset. Only use the following types: {self.available_models()} or pass a model directly into the Pardon.train_model.model parameter.')

            # set the models from the all models as that key is the model object
            val_models = [mod for mod in all_models if type(mod).__name__.lower() in models]

            # append default if exists or if user specified specfically
            if 'default' in models and (include_default or len(models) == 1):
                val_models.append('default')

            # set the final model output
            models = val_models
        else:
            # if no models were specified, use them all
            models = all_models

        # if using all models, include the default providing it is different
        if models == all_models and include_default and 'default' not in models:
            models.append('default')

        # get the type of the default model
        default_model_type = type(self.__default_model(set_params=True)).__name__.lower()

        for model in models:
            # set the model
            model_type = type(model).__name__ if model != 'default' else model

            # ignore models as requested
            if model_type.lower() in ignore_models or (model_type == 'default' and default_model_type in ignore_models):
                continue

            # if the user asked for best parameters run find best params
            # ignore if we are running default
            if find_best_model_parameters and model_type != 'default':
                
                print(f'\nFinding best parameters for model: {model_type}...\n')

                self.find_best_model_parameters(model=model_type, max_n_iterators=max_n_iterators, eval_metric=eval_metric, n_splits=n_splits, n_repeats=n_repeats)

            print(f'\nTraining model: {model_type}...\n')
            # we use this so we never overwrite the user's model params
            extra_params = {}
            # check to see if we should add max n iterators to model params
            if max_n_iterators is not None:
                # get the object type for the model being used
                if model_type == 'default':
                    check_model_attrs = self._default_model()
                else:
                    all_models_checking = pardon_models._models_and_names()
                    check_model_attrs = all_models_checking.get(model_type.lower())
                # if we returned a valid model object
                if check_model_attrs is not None:
                    # be sure that no older keys exist that will cause error
                    for param in self.__ITER_KEYS:
                        if hasattr(check_model_attrs, param):
                            extra_params[param] = max_n_iterators

            # get all the params what the user has passed in
            all_params = model_params.copy() if model_params is not None else {}
            # if extra params were found, add them
            if extra_params:
                for k, v in extra_params.items():
                    # we only add the key if it does not already exist so we do not overwrite
                    if k not in all_params:
                        all_params[k] = v

            # run the training process, ignore best parameters but balance imbalanced class data - just do 1 repeat during validation
            tm = self.train_model(model=model_type, use_best_parameters=True, scale_imbalanced=scale_imbalanced, eval_metric=eval_metric, cross_validation=cross_validation, n_splits=n_splits, n_repeats=n_repeats, model_params=all_params)

            # if the model fails, skip to the next model
            if isinstance(tm, utility.InvalidModel):
                # append the failed model to the failed models list    
                self.failed_models.append(tm)
                # skip to the next model
                continue

            # set the model as the key and the accuracy score
            model_performance[self.model_unique_identifier]['model'] = self.model
            model_performance[self.model_unique_identifier]['model_train_scores'] = self.model_train_scores
            model_performance[self.model_unique_identifier]['model_test_scores'] = self.model_test_scores
            model_performance[self.model_unique_identifier]['train_date'] = self.model_trained_date
            model_performance[self.model_unique_identifier]['train_time'] = self.model_training_time_mins  
            model_performance[self.model_unique_identifier]['train_time'] = self.model_training_time_mins  
            model_performance[self.model_unique_identifier]['model_type'] = self.model_type
            model_performance[self.model_unique_identifier]['eval_metric'] = self.model_eval_metric
            
        # if a model was successfully trained
        if model_performance: 
            # get the test scores
            test_vals = self.__get_rapid_ml_test_vals(model_performance=model_performance, score_metric=score_metric)
            # if no models were able to be evaluated on the score metric used, set to accuracy
            if not test_vals:
                old_metric = score_metric
                score_metric = pardon_options.SKLEARN_CLASSIFIER_DEFAULT if not self._is_regression else pardon_options.SKLEARN_REGRESSION_DEFAULT
                print(f'*** WARNING: Changing score_metric from "{old_metric}" to "{score_metric}" because no models were able to be scored using {old_metric}.')
                test_vals = self.__get_rapid_ml_test_vals(model_performance=model_performance, score_metric=score_metric)

            # if we are using error scores, we want the lowest error
            if score_metric in pardon_options.REDUCTION_SCORE_ON:
                # get the model that reduces the error
                best_model = min(test_vals, key=test_vals.get)
            else:
                # get the best performing model based on the score_metric
                best_model = max(test_vals, key=test_vals.get)

            # set the attirbutes of the best perfoming model
            self.model_unique_identifier = best_model
            self.model = model_performance[best_model]['model']
            self.model_train_scores = model_performance[best_model]['model_train_scores']
            self.model_test_scores = model_performance[best_model]['model_test_scores']
            self.model_trained_date = model_performance[best_model]['train_date']
            self.model_training_time_mins = model_performance[best_model]['train_time']
            self.model_type = model_performance[best_model]['model_type']
            self.model_eval_metric = model_performance[best_model]['eval_metric']
            self.rapid_ml_score_metric = score_metric
            # retain the score metric for every item
            for model_item in model_performance.keys():
                model_performance[model_item]['score_metric'] = score_metric
            # retain the scores from model performance
            self.rapid_ml_scores = model_performance
        else:
            # raise an error
            errors_found = [x.error for x in self.failed_models]
            errors_found = '\n--> '.join(errors_found)
            raise ValueError(f'No models could be trained without error. Change your input model types or check your data is valid and try again. The following errors were encountered:\n--> {errors_found}')

    def _validate_scoring_metric(self, scoring_metric) -> str:
        # get the recognised scoring metric label
        scoring_metric = scoring_metric.lower()
        # swap any values
        scoring_metric = 'roc_auc' if scoring_metric == 'auc' else scoring_metric
        scoring_metric = 'log_loss' if scoring_metric == 'logloss' else scoring_metric

        # if the default was left, change it to the regression default
        if scoring_metric == pardon_options.SKLEARN_CLASSIFIER_DEFAULT and self._is_regression:
            print(f'*** WARNING: Changing score_metric from "{pardon_options.SKLEARN_CLASSIFIER_DEFAULT}" to "{pardon_options.SKLEARN_REGRESSION_DEFAULT}" as this is a regression task.')
            return pardon_options.SKLEARN_REGRESSION_DEFAULT

        if scoring_metric not in self.available_scoring_metrics():
            raise ValueError(f'The score_metric of {scoring_metric} is invalid. Please select from the following and try again: {self.available_scoring_metrics()}')

        return scoring_metric

    @__function_unavailable_after_data_clear
    def rapid_ml(self, model_fullpath:str=None, models:list=[], ignore_models:list=[], eval_metric:str='accuracy', drop_duplicates:bool=False, max_features='all', use_ohe:bool=False, ordinal_encode:bool=False, ordinal_encoding_order_by='value', label_encode:bool=True, pca_n_components:int=None, min_feature_contribution_score=None, output_model_explanation:bool=False, output_model_script:str=None, make_text_upper_case:bool=False, find_best_model_parameters:bool=False, max_n_iterators:int=None, scale_data:bool=True, scaler_type:str='standard_scaler', cleanse_data:bool=True, drop_nulls:bool=False, train_models:bool=True, scale_imbalanced:bool=False, remove_unhelpful_columns:bool=True, max_null_ratio:float=0.5, max_correlation:float=None, remove_outliers:bool=False, z_threshold:float=3.0, ignore_target_outliers:bool=True, clear_data:bool=False, n_clusters:int=3, cluster_column_name:str=None, cluster_model:str='KMeans', score_metric:str='accuracy', cross_validation:bool=True, n_splits:int=10, n_repeats:int=1, **kwargs):
        """
        Automatically clean, encode, and scale data before training and saving a model.

            Args:
                model_fullpath : str, default None
                    The fullpath to where the model will be saved. If not supplied, the model will not be saved.
                models : list, default [] (empty list)
                    Specify which type of models to try. Leaving this blank will try all available models.
                ignore_models : list, default [] (empty list)
                    Specify which type of models to ignore.
                eval_metric : str, default 'accuracy'
                    Specify which evaluation metric is to be used when using cross validation. Check the available metrics using the available_evaluation_metrics method. The default for a regression model is 'r2'. The default for classifiers can be changed using the XGBCLASSIFIER_DEFAULT, XGBCLASSIFIER_BINARY_DEFAULT, SKLEARN_CLASSIFIER_DEFAULT, and SKLEARN_REGRESSION_DEFAULT attributes. Refer to the SKLearn documentation and XGBoost documention for more information.
                drop_duplicates : bool, default False
                    Drop duplicate rows.
                max_features : int, float, default 'all'
                    The maximum number of columns to keep in the dataset. If an integer is supplied, the top n performing columns will be retained. If a float is supplied, that proportion of the columns will be retained. For example, max_features=0.5 will retain the top 50% best performing features.
                use_ohe : bool, default False
                    Perform one hot encoding on all viable, string-based columns.
                ordinal_encode: bool, default False
                    Perform ordinal encoding on all viable, string-based columns using the ordering specified in the ordinal_encoding_order_by argument.
                ordinal_encoding_order_by: str, dict, list, function, default 'value', {'value', 'frequency', dict, list, func}
                    How to order the values in a column prior to encoding. Specify a dictionary containing the column name as key and how to order that column. Functions will be applied to the entire column as a list to specify the order. Frequency means the most frequently occurring item will have the highest encoded value and so on. Items not seen during training will be given the value 0.
                label_encode : bool, default True
                    Perform label encoding on all viable, string-based columns. If set to False and text data remains, the model will fail during training.
                pca_n_components : int, default None
                    Perform Principal Component Analysis and reduce the columns to n components.
                min_feature_contribution_score : int, float, default None
                    Only retain columns that have a minimum specified feature contribution score.
                output_model_explanation : bool, str, default False
                    Display an output showing model summary and model explanations. True will show a summary, passing a .png file fullpath will also save the output to the fullpath specified.
                output_model_script : None, str, default None
                    Output the model script to the path specified. If None the model script will not be saved.
                make_text_upper_case : bool, default False
                    Make all text in columns upper case as per the make_upper_case method. This is helpful when matching data as matches are case sensitive.
                find_best_model_parameters : bool, default False
                    Use Grid Search Cross Validation to find the best model hyperparameters. Please note, running this method can take several hours and will consume significant compute so caution advised if running on a cloud platform. Note, if 'default' is passed to the 'models' argument, the default model will not have the best parameters searched. This is because the same model type will be searched without default parameters already set.
                max_n_iterators : int, None, default None
                    The maximum number of iterations to run through for each validation when using find_best_parameters or model training. A higher number will take longer to complete but will increase the likelihood of the objective converging.
                scale_data : bool, default True
                    Perform data scaling. Unless performed manually, this will only be performed if cleanse_data is set to True.
                scaler_type : str, default 'standard_scaler' {'standard_scaler', 'min_max_scaler'}
                    Scale the data.
                cleanse_data : bool, default True
                    Perform data cleansing and format the data so it can be used to train the machine learning models.
                drop_nulls : bool, default False
                    Drop null rows from your input dataset as per the default drop_nulls method. If False, nulls will be filled as per the default settings in the fill_nulls method. 
                    Note, the drop_nulls will not be applied during any predictions and nulls found during prediction will be filled as per the default settings in the fill_nulls method.
                train_models : bool, default True
                    Train the models after any data transformations. If set to False, the train_model method will not be performed.
                scale_imbalanced : bool, default False
                    If imbalanced class distribution is found, scale using under or over sampling to balance class distribution before training.
                remove_unhelpful_columns : bool, default True
                    Remove columns that are deemed unhelpful as per the remove_unhelpful_columns method.
                max_null_ratio int, float, None, default 0.5
                    The max proportion of the column that contains null values. 0.5 would mean that if more than 50% of the column values are null, the column will be deemed as unhelpful and removed. None means this will not be checked.
                max_correlation : int, float, None, default None
                    Remove columns that are correlated by more than the max_correlation. A correlation of 1 means columns that are 100% correlated are allowed. This calls the remove_correlated_columns method. None means this will not be checked.
                clear_data : bool, default False
                    Clear the retained input data from the model before saving to help significantly reduce the model object file size. If this is used many of the model's methods will no longer be available and the model can no longer be changed or updated.
                remove_outliers : bool, default False
                    Remove outliers from your dataset based on the z_threshold.
                z_threshold :  int, float,  default 3.0
                    Rows with a z score more than that specified will be determined as an outlier and removed using the remove_outliers method. A z score of 3.0 means the value is 3 standard deviations or more away from the column mean. This will only be performed if remove_outliers=True.
                ignore_target_outliers :  bool, default True
                    Specify if you want to ignore the target column when finding outliers in the data. ignore_target_outliers=True means the target column will not be searched and will not have any outliers removed.
                n_clusters :  int, None, default 3
                    The number of clusters to create. Each row will be assigned a cluster group. This option triggers the create_clusters method. None means this will not be performed.
                cluster_column_name :  str, None, default None
                    The name of the column to add the clustered group to. This option triggers the create_clusters method. None means this will not be performed.
                cluster_model : str, default 'KMeans'
                    The clustering model to use to create your clusters.
                score_metric : str, default 'accuracy'
                    Specify which metric is to be used when determining the best performing model in testing. You can see the available scoring metrics using the available_scoring_metrics method. The default for regression models is 'r2'. The best performing model will be that with the highest test score unless using scores of errors (such as 'neg_mean_squared_error') in which case the lowest score will be considered best. You can view the score metrics that get minimised at the pardon.pardon_options.REDUCTION_SCORE_ON attribute.
                cross_validation : bool, default True
                    Perform cross validation during model training. This should only ever be switched off if you simply testing an idea and want to reduce training time. It is advised you always perform cross validation.
                n_splits : int, default 10
                    The number of splitting iterations during cross validation.
                n_repeats : int, default 1
                    The number of times to repeat the cross validation.
                **kwargs : keyword parameters
                    This allows the user to tweak certain arguments used. Presently the only valid arguments are model_params, fill_text_with, and fill_numeric_with.
        """
        # if the model is just one, make it a list of one
        models = utility.single_to_list(item=models)
        ignore_models = utility.single_to_list(item=ignore_models)

        # ensure the parameters are valid
        utility.assert_item_type(item=models, item_types=[list])
        utility.assert_item_type(item=ignore_models, item_types=[list])
        utility.assert_item_type(item=drop_duplicates, item_types=[bool])
        utility.assert_item_type(item=max_features, item_types=[int, str])
        utility.assert_item_type(item=min_feature_contribution_score, item_types=[int, float, None])
        utility.assert_item_type(item=pca_n_components, item_types=[int, None])
        utility.assert_item_type(item=max_n_iterators, item_types=[int, None])
        utility.assert_item_type(item=eval_metric, item_types=[str])
        utility.assert_item_type(item=cleanse_data, item_types=[bool])
        utility.assert_item_type(item=use_ohe, item_types=[bool])
        utility.assert_item_type(item=ordinal_encode, item_types=[bool])
        utility.assert_item_type(item=label_encode, item_types=[bool])
        utility.assert_item_type(item=train_models, item_types=[bool])
        utility.assert_item_type(item=clear_data, item_types=[bool])
        utility.assert_item_type(item=find_best_model_parameters, item_types=[bool])
        utility.assert_item_type(item=drop_nulls, item_types=[bool])
        utility.assert_item_type(item=output_model_script, item_types=[str, None])
        utility.assert_item_type(item=make_text_upper_case, item_types=[bool])
        utility.assert_item_type(item=scale_imbalanced, item_types=[bool])
        utility.assert_item_type(item=remove_unhelpful_columns, item_types=[bool])
        utility.assert_item_type(item=max_null_ratio, item_types=[int, float, None])
        utility.assert_item_type(item=max_correlation, item_types=[int, float, None])
        utility.assert_item_type(item=scale_data, item_types=[bool])
        utility.assert_item_type(item=scaler_type, item_types=[str])
        utility.assert_item_type(item=remove_outliers, item_types=[ bool])
        utility.assert_item_type(item=z_threshold, item_types=[int, float, None])
        utility.assert_item_type(item=ignore_target_outliers,item_types=[bool])
        utility.assert_item_type(item=n_clusters, item_types=[int])
        utility.assert_item_type(item=cluster_column_name, item_types=[str, None])
        utility.assert_item_type(item=cluster_model, item_types=[str])
        utility.assert_item_type(item=score_metric, item_types=[str])
        utility.assert_item_type(item=cross_validation, item_types=[bool])
        utility.assert_item_type(item=n_splits, item_types=[int])
        utility.assert_item_type(item=n_repeats, item_types=[int])
 
        # check the model hasnt already been trained, if it has raise an error
        if self.model is not None and cleanse_data:
            raise Exception('The data has already been formatted and a model trained so this function is unavailable. Set clean_data=False or create a new Pardon object to use this function.')  
        # ensure users know when they have contradicting items
        # if the user has target set to none, we can allow a save
        if model_fullpath and not train_models and self.target:
            print('*** WARNING: You have set a model_fullpath but have set train_model=False. This means you are saving an untrained Model. ***')
        # warn users they have set the method to do nothing
        if not train_models and not cleanse_data:
            raise ValueError('You have both cleanse_data=False and train_model=False which means this method will not do anything. Update one of these values and try again.')

        # check that n_clusters is 2 or more
        if cluster_column_name is not None:
            if n_clusters < 2:
                raise ValueError(f'n_clusters must be 2 or more. A value of {n_clusters} is invalid. Please change this and try again.')

        # if this is a clustering model, set the train model to False
        if self.target is None:
            if train_models == True:
                train_models = False
                print('Note: The train_models argument was set to False as a model cannot be trained with no target column.')

        # get the eval metric
        eval_metric = self._validate_eval_metric(model=None, eval_metric=eval_metric)
        # get the score on metric
        score_metric = self._validate_scoring_metric(scoring_metric=score_metric)

        # get the directory from the fullpath
        # do this first so if the path is wrong, we haven't wasted time training
        # users do not have to save the model
        if model_fullpath:
            model_fullpath = utility._check_save_parameters(fullpath=model_fullpath, filetype='.pkl')
        
        # set the object as a rapid ml version
        self._is_rapid_ml = True
                
        # if the user wants data cleansing, run all the data cleansing
        if cleanse_data:
            print('Preparing data for training...\n')

            print('Cleaning column names...\n')
            # clean columns
            self.clean_column_names()

            if drop_duplicates:
                print('Dropping duplicates...\n')
                # drop duplicates
                self.drop_duplicates()

            if remove_unhelpful_columns:
                print('Removing unhelpful columns...\n')
                # remove any columns that appear to not be helpful
                self.remove_unhelpful_columns(max_null_ratio=max_null_ratio)

            # if specified to drop nulls, drop, else fill nulls
            fill_text_with = kwargs['fill_text_with'] if 'fill_text_with' in kwargs else 'Unknown'
            fill_numeric_with = kwargs['fill_numeric_with'] if 'fill_numeric_with' in kwargs else 'mean'

            if drop_nulls:
                print('Removing nulls...\n')
                self.drop_nulls()
                # this is added so there is a record of a fill null in case needed for the prediction
                self.fill_nulls(fill_text_with=fill_text_with, fill_numeric_with=fill_numeric_with)
            else:
                print('Replacing nulls...\n')
                self.fill_nulls(fill_text_with=fill_text_with, fill_numeric_with=fill_numeric_with)

            # remove outliers for all numeric columns with a value > the z_threshold sd from the mean
            if z_threshold is not None and remove_outliers:
                print('Removing outliers...\n')
                self.remove_outliers(z_threshold=z_threshold, ignore_target=ignore_target_outliers)

            if make_text_upper_case:
                print('Making all text upper case...\n')
                self.make_upper_case()

            if use_ohe:
                print('One hot encoding...\n')
                self.one_hot_encode()

            if ordinal_encode:
                encoding_columns = self.available_encoding_columns()
                # if we are label encoding, the target should be label encoded rather than ordinal
                include_targ = False if label_encode else True
                
                if encoding_columns:
                    print('Ordinal encoding...\n')
                    self.ordinal_encode(columns=encoding_columns, order_by=ordinal_encoding_order_by, include_target=include_targ)

            if label_encode:
                # set all the valid encoding columns / haven't been frequency or ohe
                encoding_columns = self.available_encoding_columns()
                # label encode - this has to be done regardless so the data can be trained
                if encoding_columns:
                    print('Label encoding...\n')
                    self.label_encode(encoding_columns)

            # remove correlated columns
            # we do this here because columns have to have been encoded etc first
            if max_correlation is not None:
                self.remove_correlated_columns(max_correlation=max_correlation)

            # of clustering, add the cluster
            if cluster_column_name is not None:
                print('Creating clusters...\n')
                self.create_clusters(n_clusters=n_clusters, column_name=cluster_column_name, model=cluster_model)

            # only keep the best performing 90% columns
            if (max_features is not None and max_features != 'all') or min_feature_contribution_score:
                print(f'Setting {max_features} best features...\n')
                self.set_best_features(max_features=max_features, min_contribution_score=min_feature_contribution_score)

            # this needs to always been done last to avoid scaling occurring on columns that were since removed or renamed
            if scale_data:
                # if the user has set true, set the default
                if str(scaler_type).lower() == 'default':
                    scaler_type = 'standard_scaler'

                print('Scaling data...\n')
                self.scale_data(scaler_type=scaler_type)
                
            if pca_n_components:
                print('Preparing for Principal Component Analysis...\n')
                self.pca(n_components=pca_n_components)

            print('Data preparation complete\n')

        # if the user specified they want to train the model
        if train_models:
            model_params = kwargs['model_params'] if 'model_params' in kwargs and isinstance(kwargs['model_params'], dict) else None
            # run the best auto ml model check
            self.__train_multiple_models(models=models, ignore_models=ignore_models, find_best_model_parameters=find_best_model_parameters, max_n_iterators=max_n_iterators, eval_metric=eval_metric, scale_imbalanced=scale_imbalanced, score_metric=score_metric, cross_validation=cross_validation, n_splits=n_splits, n_repeats=n_repeats, model_params=model_params)
            
            # if the user specified outputting model explanation, output
            if output_model_explanation:
                # if the output is a string check if it is a filename
                if isinstance(output_model_explanation, str): 
                    # if the filename is valid, get the output
                    if os.path.exists(os.path.dirname(output_model_explanation)):
                        # if the directory does not exist or the filename does not end .db, return invalid
                        print('Producing model prediction explanation output...\n')
                        # save the model explanation output
                        self.explain_model_predictions(refresh=False, output_fullpath=output_model_explanation)

            # set the default message to apply to all model types
            output_message = f'\n\nAuto ML Completed successfully.\nBest performing model on {self.rapid_ml_score_metric} was model ref: {self.model_unique_identifier}, a {self.model_type} model.\n{self.rapid_ml_score_metric} Test score: {self.model_test_scores[self.rapid_ml_score_metric]}\n'
            # add the test scores
            output_message += f'Train Scores: {self.model_train_scores}\n'
            output_message += f'Test Scores: {self.model_test_scores}\n'

            # remind the user that the model has not been saved
            if not model_fullpath:
                output_message += '\nNote: The model was not saved as no model_fullpath was supplied. Use the model.save_model() method to save your model.\n'
            
            # print the output message
            print(output_message)

            # if any models failed, tell the users
            if self.failed_models:
                print(f'\n{len(self.failed_models)} model(s) failed during training, these can be seen in your Pardon.failed_models attribute.\n')

        # output the model script
        if output_model_script is not None and isinstance(output_model_script, str):
            # we do the model script before we clear data because the model script runs predictions using the data
            # to ensure we record the model fullpath, we set it here first
            self.model_fullpath = model_fullpath
            self.model_script(script_fullpath=output_model_script)

        # if the user specified a model fullpath, save it
        if model_fullpath:
            print('\nSaving the model...\n')
            # save the model
            self.save_model(model_fullpath=model_fullpath, min_test_metric=score_metric, min_test_score=None, clear_data=clear_data)
                 
    def available_encoding_columns(self) -> list:
        """
        Returns a list of strings of the columns that are valid for encoding and have not yet been frequency, label, ordinal, or one hot encoded. This will only show columns with a data type of object.

            Returns:
                    (list) : list of string column names that are available for encoding.
        """
        cols = [col for col in self.columns if self.data[col].dtype == 'object' \
                and col not in self._frequency_encoded_column_input_names \
                and col not in self._ohe_encoded_column_input_names \
                and col not in self._label_encoder_ignore \
                and col not in self._binary_encoded_column_input_names \
                and col not in self._ordinal_encoded_column_input_names]
        
        return cols

    def _objective(self) -> str:
        """get the objective for classification"""
        # the objective for xgboost models needs to be multi if more than 2 classes else binary
        objective = 'multi' if self.number_of_classes() > 2 else 'binary'

        return self.__OBJECTIVE[objective]

    def __x_train_cols(self):

        if not hasattr(self, '_X_train'):
            return [col for col in self.train_data.columns if col != self.target]

        return list(self._X_train.columns)

    def __clear_data(self):
        # clears the data ready for when the model saves
        # ensure the x_train and y_train columns get retained as these are used
        if self.target is not None:
            self._X_train_columns = self.__x_train_cols()
        # if for some reason the raw data cols were not retained, add them
        if not hasattr(self, 'raw_data_columns'):
            # ensure we retain a copy of the raw data columns
            self.raw_data_columns = self.raw_data.columns

        # keep the row counts
        self._all_row_count = self.row_count(dataset='all')
        self._train_row_count = self.row_count(dataset='train')
        self._test_row_count = self.row_count(dataset='test')
        self._raw_row_count = self.row_count(dataset='raw')
        self._classes = self.classes()

        # set the data inputs to None
        self._X_train = None
        self._y_train = None
        self._X_test = None
        self._y_test = None
        self.raw_data = None
        self.train_data = None
        self.test_data = None
        # set data cleared flag to True
        self._data_cleared = True
    
    @__function_unavailable_after_data_clear
    def __set_x_y_values(self):
        
        # get the x, y values
        X_train, y_train = self._X_y_values(dataset='train_data')
        X_test, y_test = self._X_y_values(dataset='test_data')
    
        # set the variables so testing is always repeatable
        self._X_train = X_train
        self._X_test = X_test
        self._y_train = y_train
        self._y_test = y_test

        # set the x train columns, this is so they can be used even if the data gets cleared
        self._X_train_columns = self.__x_train_cols()
        
    def __default_params(self) -> dict:

        # if the default is None, it means it has not been set manually by the user
        if  self.__default_model_params is None:
            # get the defaul parameters
            params = pardon_models._default_model_params(is_regression=self._is_regression, random_state=self.__random_state)
        else:
            params = self.__default_model_params

        return params

    def set_default_model_params(self, *, reset_all_params:bool=False, **kwargs):
        """
        Set the defaul parameters for the default model.

            Args:
                    reset_all_params : bool, default False
                        Set True to reset all model hyperparameters back to the implementation default from the relevant API.
                    **kwargs : keyword arguments
                        Set the relevant hyperparameters for the default model.
        """
        utility.assert_item_type(item=reset_all_params, item_types=[bool])
        # get the default model, and default params
        model = self.__default_model(set_params=not reset_all_params)
        # if no kwargs and not reseting model params, print and finish
        if not reset_all_params and not kwargs:
            print(f'*** WARNING: No kwargs given and model parameters not reset, so no changes required to: {type(model).__name__} model. ***')
            return

        model_params = model.get_params() if hasattr(model, 'get_params') else None
        # if we can get the parameters check they are valid
        if model_params is not None:
            # if the user has given us parameters
            if kwargs:
                # check the kwargs are relevant for the default model
                invalids = [p for p in kwargs.keys() if p not in model_params.keys()]
                # raise an error anf specify the available parameters
                if invalids:
                    raise ValueError(f'Invalid parameters given ({invalids}) for model type: {type(model).__name__}. The following parameters may be set:\n{list(model_params.keys())}')
                # update the model params
                model_params.update(kwargs)
            # set kwargs to be the model params
            kwargs = model_params

        # set the defaults
        self.__default_model_params = kwargs

        print(f'Default model parameters for: {type(model).__name__} model updated successfully.')

    def get_default_model_params(self) -> dict:
        """
        Returns a dictionary object containing the model hyperparameters and their value, for the default model type.

            Returns:
                    (dict) : dict containing the model hyperparameters and their value, for the default model type.
        """
        model = self.__default_model(set_params=True)
        model_params = model.get_params() if hasattr(model, 'get_params') else None

        if model_params is None:
            raise ValueError(f'Unable to get model parameters for model type: {type(model).__name__}')

        return model_params

    def __default_model(self, set_params:bool=True):

        model = pardon_models._default_model(is_regression=self._is_regression)

        if set_params:
            model.set_params(**self.__default_params())
        
        return model

    def search_spaces(self) -> dict:
        """
        Returns a dictionary object containing each of the models and the associated parameters that are searched during the find_best_model_parameters method.

            Returns:
                (dict) : dict object containing each of the models and the associated parameters that are searched during the find_best_model_parameters method.
        """
        # get the models and search space
        models = pardon_models._regression_models() if self._is_regression else pardon_models._classification_models() 

        # change the model class for the model name
        models = {type(model).__name__: ss for model, ss in models.items()}

        return models

    def __rapid_ml_models(self) -> dict:
        # return the regression or classification models
        models = pardon_models._regression_models() if self._is_regression else pardon_models._classification_models() 
      
        return models

    @__function_unavailable_after_data_clear
    @__block_null_target
    @__retain_transformation
    @__ignore_function_in_transforms
    @__non_data_func
    def find_best_model_parameters(self, model='default', max_n_iterators:int=None, eval_metric:str='accuracy', search_space:dict=None, n_splits:int=10, n_repeats:int=3):
        """
        Find and set the best hyperparameters for the specified model using Grid Search Cross Validation. It is worth noting this process can take hours to complete.
            
            Args:
                model : str, class, default 'default'
                    The name of the model type to find the best hyperparameters for. Default means an XGBoost Classifier will be used for classification problems, and a Linear Regression model for regression. You can also pass a custom algorithm object to the model parameter, but a search_space is required when doing so.
                max_n_iterators : int, None, default None
                    The maximum number of iterations to run through for each validation. A higher number will take longer to complete but will increase the likelihood of the objective converging. None means the model's default settings will be used.
                eval_metric : str, default 'accuracy'
                    The evaluation metric determining model performance.
                search_space : dict, None, default None
                    The model parameters to use during the cross validation. If None, the parameters searched will be chosen automatically. You can see the standard search spaces for each model using the search_spaces method.
                n_splits : int, default 10
                    The number of splitting iterations during cross validation.
                n_repeats : int, default 3
                    The number of times to repeat the cross validation.
        """
        # check that all values are numeric and ready for training
        self._process_can_start(on_error='Data not ready for hyperparameter optimisation. Please encode all your data to numeric values and try again.')

        # see if the user is using their own model
        if not callable(model):
            # ensure the model being passed in is a string
            utility.assert_item_type(item=model, item_types=[str])
            cust_mod = False
        else:
            cust_mod = True
            # if using custom, user needs to define the search space
            if not isinstance(search_space, dict):
                raise ValueError(f'The search_space must be provided when using custom models. Provide a valid search space in dictionary format and try again.')

        utility.assert_item_type(item=max_n_iterators, item_types=[int, None])
        utility.assert_item_type(item=eval_metric, item_types=[str])
        utility.assert_item_type(item=search_space, item_types=[dict, None])
        utility.assert_item_type(item=n_splits, item_types=[int])
        utility.assert_item_type(item=n_repeats, item_types=[int])

        # set default to be false
        is_default = False
        space = None
        
        # set the x, y values for train, test
        self.__set_x_y_values() 

        if not cust_mod:
            # set the model type name
            model = str(model).lower()
            
            # set the defaults if using the default model
            if model == 'default':
                # set default to true as it is being used
                is_default = True
                # use the default model
                use_model = self.__default_model(set_params=True)
                # reset the model type
                model = type(use_model).__name__
            
            # check a valid model is passed in
            self.__is_valid_model(model_name=model)

            for model_name, searching_space in self.__rapid_ml_models().items():
                if type(model_name).__name__.lower() == model.lower():
                    # set the model and search space
                    use_model = model_name if not is_default else use_model
                    space = searching_space
                    break
        else:
            # get the model we are using - the search_space has to have been provided to get to this point
            use_model = model()

        # validate the eval metric
        eval_metric = self._validate_eval_metric(model=use_model, eval_metric=eval_metric)
        
        # if the user wants to set the search space, overwrite the default 
        space = search_space if search_space is not None else space

        # currently only checks one attribute, single item list
        if max_n_iterators is not None:
            for attribute in self.__ITER_KEYS:
                # change num of iterations to make n estimators
                if hasattr(use_model, attribute):
                    setattr(use_model, attribute, max_n_iterators)
                    
        # if no space, return as we have nothing to test
        if space is None:
            return

        cv = utility.get_cv_object(n_splits=n_splits, n_repeats=n_repeats, regression=self._is_regression, stratify=self._stratify, random_state=self.__random_state) 
        search = GridSearchCV(use_model, space, n_jobs=-1, cv=cv)
        # reset the model type the parameters are for, for consistent naming
        model_type = type(use_model).__name__
        start = time.time()

        # xgboost works slightly different as it has the eval on metric
        if isinstance(use_model, xgb.XGBClassifier):
            # if xgboost we used eval metric
            result = search.fit(self._X_train, self._y_train, eval_metric=eval_metric)
        else:
            # set the scoring method
            setattr(search, 'scoring', eval_metric)
            # execute search
            result = search.fit(self._X_train, self._y_train)
   
        end = time.time()
        # add _default to the name if using default
        if is_default:
            model_type += self.__DEFAULT_OPTIONS_ST__ignore_function_in_transformsR
        
        self.validation_training_time_mins[model_type] = round((end - start) / 60, 2)
        self.best_validation_score[model_type] = result.best_score_
        self.best_hyperparameters[model_type] = result.best_params_
    
    @__function_unavailable_after_data_clear 
    @__retain_transformation  
    @__block_null_target
    @__ignore_function_in_transforms
    @__non_data_func
    def _balance_classes(self):
        balance = False
        class_balance = collections.Counter(self._y_train)
        total_items = len(self._y_train)
        min_value = min(class_balance.values())
        max_value = max(class_balance.values())
        # scale down the ratio to 80% of the outcome for some tolerance
        max_ratio = (max_value / total_items) * pardon_options.BALANCE_SCALE_RATIO
        # check each of the ratios in the class balance
        for value in class_balance.values():
            # get the ratio of each class
            ratio = value / total_items
            # if the ratio is < scaled max ratio, perform re-sampling
            if ratio < max_ratio:
                balance = True
                # this determines if we do under or over sampling dependent on the available number of rows
                if min_value < pardon_options.MIN_SAMPLE_FOR_UNDERSAMPLE:
                    sampler = pardon_options.OVER_SAMPLING_MODEL
                    self._sampling_strategy = 'Over'
                else:
                    sampler = pardon_options.UNDER_SAMPLING_MODEL
                    self._sampling_strategy = 'Under'
                break
        # if balance is set, random sample the data        
        if balance:
            # add the random state if present in the model
            if hasattr(sampler, 'random_state'):
                setattr(sampler, 'random_state', self.__random_state)

            # Resample
            self._X_train, self._y_train = sampler.fit_resample(self._X_train, self._y_train)
            self._X_train_columns = self.__x_train_cols()
            self._classes_balanced = True
    
    def __is_valid_model(self, model_name:str):
        # check if the model name is valid
        # set name to be lower case for comparison
        model_name = str(model_name).lower()
        # if model name is invalid raise error
        if model_name not in [mod.lower() for mod in self.available_models()]:
            raise KeyError(f'The model type {model_name} is not available. Please choose from: {self.available_models()}')

    def available_chart_types(self) -> tuple:
        """
        Returns a tuple of the chart types for data visualisation using the Pardon.plot_data method

            Returns:
                    (tuple): tuple of string names of the available chart types.
        """

        return ('map', 'scatterplot', 'histogram', 'correlation', 'lineplot')


    def available_evaluation_metrics(self) -> list:
        
        """
        Returns a list of the available evaluation metrics used during cross validation in model training. Note, this does not include the evaluation metrics for XGBClassifier models, these can be found separately at XGBoost.

            Returns:
                    (list): list of string names of the available evaluation metrics.
        """
        # get the sklearn scoring metrics
        scoring_sklearn = self.available_scoring_metrics()
        # xgboost is classification only so return empty if regression
        scoring_xgboost = pardon_models._xgboost_eval_metrics(num_classes=self.number_of_classes()) if not self._is_regression else []
        
        output = [] 
        # append to the main list the api specific metrics
        if scoring_sklearn:
            output.extend(scoring_sklearn)
        if scoring_xgboost:
            output.extend(scoring_xgboost)

        return output

    def available_scoring_metrics(self) -> list:
        """
        Returns a list of the available scoring metrics used to determine the best performing models.

            Returns:
                    (list): list of string names of the available scoring metrics.
        """   
        # get the available items
        mets = pardon_models._scoring_metrics(is_regression=self._is_regression)
        mets = list(mets.keys()) if mets else []

        return mets 

    def _set_test_scores(self, y_preds, y_preds_proba):

        score_dict = {}
        # iterate through the test type and score methods
        for test_type, score_method in pardon_models._scoring_metrics(is_regression=self._is_regression).items():
            kwargs = {}
            # get the keyword args
            arg_spec = inspect.getfullargspec(score_method)
            # get the attributes to check
            attrs = ['args', 'varargs', 'kwonlyargs', 'kwonlydefaults']
            spec = []
            for att in attrs:
                # get the class attribute
                sp = getattr(arg_spec, att)
                # if return values
                if sp is not None and sp:
                    # the kwonlydefaults is a dictionary so we only need the keys
                    if att == 'kwonlydefaults':
                        sp = list(sp.keys())
                        if sp:
                            # append these to our list
                            spec.extend(sp)
            # set the average to macro and the multi class to ovr
            if 'average' in spec:
                kwargs['average'] = 'macro'
            # for multi class we use one vs rest
            if 'multi_class' in spec:
                kwargs['multi_class'] = 'ovr'
            # if a fail it means the measure is not valid for this model
            try:
                # set the test type and score
                score_dict[test_type] = score_method(self._y_test, y_preds, **kwargs)
            # ignore the error as we won't add the particular score metric
            except Exception:
                if y_preds_proba is not None:
                    try:
                        score_dict[test_type] = score_method(self._y_test, y_preds_proba, **kwargs)
                    except Exception:
                        pass

        # assign all the test scores
        self.model_test_scores = score_dict

    def _set_train_scores(self, train_score, score_type):
        # assign the train scores
        self.model_train_scores = {score_type: train_score}

    def _validate_eval_metric(self, model, eval_metric:str) -> str:
        # if eval is None, set it to anything to be sure one gets parsed
        if eval_metric is None:
            eval_metric = pardon_options.SKLEARN_CLASSIFIER_DEFAULT

        # get eval metrics lower case
        eval_metric = eval_metric.lower()

        # ensure the metrics are valid
        # check this first as the default is accuracy
        if eval_metric == pardon_options.SKLEARN_CLASSIFIER_DEFAULT and self._is_regression:
            print(f'\n*** WARNING: eval_metric changed from "{pardon_options.SKLEARN_CLASSIFIER_DEFAULT}" to "{pardon_options.SKLEARN_REGRESSION_DEFAULT}" because "{pardon_options.SKLEARN_CLASSIFIER_DEFAULT}" is not a valid metric for regression models. ***\n')
            return pardon_options.SKLEARN_REGRESSION_DEFAULT

        # ensure the eval metric is valid
        if eval_metric not in self.available_evaluation_metrics():
            # if this is not found, it mwans we need mlogloss as more than 2 classes
            if eval_metric == 'logloss':
                eval_metric == 'mlogloss'
            else:
                raise ValueError(f'The eval_metric: {eval_metric} is invalid, please use from the following and try again: {self.available_evaluation_metrics()}')

        # if the model is None we just return as we are assessing the general arguments
        if model is None:
            return eval_metric

        # check xgboost
        if isinstance(model, xgb.XGBClassifier):
            # get metrics
            metrics = pardon_models._xgboost_eval_metrics(num_classes=self.number_of_classes())
            # roc_auc for sklearn, we use auc for xgboost
            eval_metric = 'auc' if eval_metric == 'roc_auc' else eval_metric
            eval_metric = 'logloss' if eval_metric == 'log_loss' else eval_metric

            # if it doesn't exist, set the default to mlogloss
            if eval_metric not in metrics:
                # if binary, we need to use the binary default
                if self.number_of_classes() < 2:
                    deflt = pardon_options.XGBCLASSIFIER_BINARY_DEFAULT
                else:
                    # if the user has specified merror but this is a binary model, change it
                    deflt = pardon_options.XGBCLASSIFIER_DEFAULT

                print(f'\n*** WARNING: eval_metric set to "{deflt}" as "{eval_metric}" is not available for XGBClassifiers during training ***\n')
                # set the default
                eval_metric = deflt

        # check the eval metric and change to defaults if applicable
        else:
            eval_metric = 'roc_auc' if eval_metric == 'auc' and not self._is_regression else eval_metric
            eval_metric = 'log_loss' if eval_metric in ('logloss', 'mlogloss') and not self._is_regression else eval_metric
            
            if eval_metric not in pardon_models._scoring_metrics(is_regression=self._is_regression):
                changed_to = pardon_options.SKLEARN_CLASSIFIER_DEFAULT if not self._is_regression else pardon_options.SKLEARN_REGRESSION_DEFAULT

                print(f'\n*** WARNING: eval_metric set to "{changed_to}" as "{eval_metric}" is only available for XGBClassifiers ***\n')
                eval_metric = changed_to

        # check to see if the eval_metric needs the neg_ prefix - this is required for sklearn metrics that include median, mean, or root
        if not isinstance(model, xgb.XGBClassifier):
            REGEX = r'(^root|mean|median|log)_.+'
            # if we match the regex, add the neg prefix
            if re.match(REGEX, eval_metric, flags=re.I):
                eval_metric = 'neg_' + eval_metric

        return eval_metric

    def add_data(self, data, overwrite_existing:bool=False, train_model:bool=True):
        """
        Add new data to your Pardon model and retrain your model.

            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data to add to your model. This will be split between train and test as per the proportions when the Pardon model was created.
                overwrite_existing : bool, default False
                    Overwrite the data that currently exists in your model. If False, data will be appended.
                train_model : bool, default True
                    Train/retrain your current ML model including the new data.
        """
        utility.assert_item_type(item=overwrite_existing, item_types=[bool])
        utility.assert_item_type(item=train_model, item_types=[bool])

        data = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)

        total_rows_added = len(data)

        # confirm all necessary columns exist
        raw_data_columns = self.raw_data_columns if self.raw_data is None else self.raw_data.columns
        differences = utility.list_differences(list1=list(raw_data_columns), list2=list(data.columns))

        # differences mean columns do not match
        if differences:
            raise KeyError(f'The new data and old data does not match, check your data and try again. The column differences are: {differences}')

        # combine data if not overwriting
        if not overwrite_existing:
            data = pd.concat([self.raw_data, data], ignore_index=True)

        # assign the data
        self.__data_assign(data=data)
        # reapply the data transformations to every piece of data
        self.__update_added_data()

        print(f'{total_rows_added} rows successfully added.')

        # retrain the model
        if train_model:
            cross_validation = True if self._cross_validation_performed is None else self._cross_validation_performed
            # model will auto be set to default if it has yet to be trained
            self.train_model(model=self.model, eval_metric=self.model_eval_metric, scale_imbalanced=self._classes_balanced, cross_validation=cross_validation, n_splits=self._n_splits, n_repeats=self._n_repeats)

    def __update_added_data(self):
        apply_specific_funcs = [x['function'] for x in self.__convert_specific_funcs]
        # take a copy as we are going to pop from this to ensure we do not repeat
        convert_funcs = self.__convert_specific_funcs.copy()
        # we create a copy as this will be overwritten
        transform_list = self._transformation_list.copy()
        # reset to empty as it will be added
        self._transformation_list = []
        self.__convert_specific_funcs = []

        # iterate through the transform list
        for transform in transform_list:
            # get each function name and kwargs
            func = transform['function']
            kwargs = transform['kwargs']
            # get the bound form of the args
            convert_func = getattr(self, func)
            # a non data func is one we apply and retain soley for the purpose of the model script
            # we dont need a data argument passed so we just run this without the convert func method
            if func in self._non_data_functions:
                convert_func(**kwargs)
                continue

            # if the arg is in the convert specs list, it means we only want to apply the transfrom to test or train data
            if func in apply_specific_funcs:
                for i, s_func in enumerate(list(convert_funcs)):
                    # if the function is the one we want to do
                    if s_func['function'] == func and sorted(s_func['kwargs']) == sorted(kwargs):
                        # apply it to the relevant items
                        self.__convert_data_using_func(convert_func=convert_func, apply_convert_to_train= s_func['apply_convert_to_train'], apply_convert_to_test=s_func['apply_convert_to_test'], **s_func['kwargs'])
                        # pop the item
                        convert_funcs.pop(i)
            else:
                # perform the convert func
                self.__convert_data_using_func(convert_func=convert_func, apply_convert_to_train=True, apply_convert_to_test=True, **kwargs)

    @__function_unavailable_after_data_clear
    @__block_null_target
    def train_model(self, model='default', use_best_parameters:bool=True, eval_metric:str='accuracy', scale_imbalanced:bool=False, model_params:dict=None, cross_validation:bool=True, n_splits:int=10, n_repeats:int=3):
        """
        Train the machine learning model.

            Args:
                model : str, class, default 'default'
                    The name of the model type to train or a valid classification machine learning (ML) model class. If using a custom ML model, the model must have the fit, predict_proba (for classification) or predict (for regression), set_paramas, and score methods. Default means an XGBoost Classifier will be used for classification problems, and a Linear Regression model for regression.
                use_best_parameters : bool, default True
                    Use the best hyperparameters for the model. Will only be available if the pardon.Pardon.find_best_model_parameters method has been completed.
                eval_metric : str, default 'accuracy'
                    The evaluation metric to use during cross validation in model training. Use the available_evaluation_metrics method to see the available options. The default for regression models will be set to 'r2'. The default for classifiers can be changed using the XGBCLASSIFIER_DEFAULT, XGBCLASSIFIER_BINARY_DEFAULT, SKLEARN_CLASSIFIER_DEFAULT, and SKLEARN_REGRESSION_DEFAULT attributes. Refer to the SKLearn documentation and XGBoost documention for more information.
                scale_imbalanced : bool, default False
                    If imbalanced class distribution is found, scale using under or over sampling to balance class distribution before training.
                model_params : dict, default None
                    A dictionary object containing custom model parameters and values to apply to the model before training.
                cross_validation : bool, default True
                    Perform cross validation during model training. This should only ever be switched off if you simply testing an idea and want to reduce training time. It is advised you always perform cross validation.
                n_splits : int, default 10
                    The number of splitting iterations during cross validation.
                n_repeats : int, default 3
                    The number of times to repeat the cross validation.
        """
        utility.assert_item_type(item=use_best_parameters, item_types=[bool])
        utility.assert_item_type(item=scale_imbalanced, item_types=[bool])
        utility.assert_item_type(item=eval_metric, item_types=[str, None])
        utility.assert_item_type(item=model_params, item_types=[dict, None])
        utility.assert_item_type(item=cross_validation, item_types=[bool])
        utility.assert_item_type(item=n_splits, item_types=[int])
        utility.assert_item_type(item=n_repeats, item_types=[int])

        # check the data is ready to be trained before starting
        self._process_can_start(on_error='Data not ready for model training. Please encode all your data to numeric values and try again.', check_rows=True)

        # if the user has accidentally specified true, false or none, set the model type to default
        model = 'default' if model in (True, False, None) else model 

        # ensure the model parameter is a string or model object
        if not isinstance(model, str) and not hasattr(model, 'fit'):
            raise TypeError(f'The class passed in the model parameter is not a valid ML model. Please pass in a valid model name from {self.available_models()}, or a valid ML model class and try again.')

        # if not a string, check to ensure the model has been instantiated
        if not isinstance(model, str):
            # if the model is a type, it has not been instantiated
            if isinstance(model, type):
                # instantiate the model
                model = model()

        # get the number of rows
        data_len = len(self.data)
        # get the number of columns
        col_len = len(self.data.columns)

        # ensure there are sufficient columns to train
        if col_len < 2:
            raise ValueError(f'There are no columns available for training. The data set may be invalid or all columns (other than the target) have been removed through data transformations. Check this and try again.')

        # ensure there are at least 50 rows of data
        if data_len < pardon_options.MIN_ROW_REQ:
            raise Exception(f'There are only {data_len} labelled rows in the dataset. Please get {pardon_options.MIN_ROW_REQ} or more rows or reduce the MIN_ROW_REQ attribute using pardon.pardon_options.MIN_ROW_REQ = 10 if you wish to overwrite this.')

         # ensure there are at least 50 rows of data
        if data_len < pardon_options.MIN_ROW_REQ:
            raise Exception(f'There are only {data_len} labelled rows in the dataset. Please get {pardon_options.MIN_ROW_REQ} or more rows or reduce the MIN_ROW_REQ attribute using pardon.pardon_options.MIN_ROW_REQ = 10 if you wish to overwrite this.')

        # set the x, y values for train, test
        self.__set_x_y_values()

        # set default params
        params = {}
        use_model = None
        is_default = False

        # if the model is a string
        if isinstance(model, str):
            # set the string to be lower case
            model = model.lower()
            # check which model is to be used
            if model == 'default':
                # set the default parameters
                params = self.__default_params()
                # set the model and parameters
                use_model = self.__default_model(set_params=True)
                # set the is default flag
                is_default = True
            else:
                # check name valid
                self.__is_valid_model(model_name=model)
                # get the model selected
                for model_choice in self.__rapid_ml_models().keys():
                    # if the name is that chosen, set the model type
                    if type(model_choice).__name__.lower() == model.lower():
                        use_model = model_choice
                        break
        else:
            # use the model class provided - this gets an unfitted version
            use_model = sklearn.base.clone(model)
        
        # if the user requested best parameters and the best parameters were found, apply them
        if use_best_parameters and hasattr(self, 'best_hyperparameters'):
            # get the model name and append the _default if the default model is being used
            model_name_get = type(use_model).__name__
            # if using the default mode, add the default string
            if model == 'default':
                model_name_get += self.__DEFAULT_OPTIONS_STR
            # get the best paramas
            best_params = self.best_hyperparameters.get(model_name_get)
            # only update the parameters if they are for the same model type
            if best_params:
                # update the params dictionary to include the best parameters
                params.update(best_params)
                # remove references to verbosity
                for verb in ('verbose', 'verbosity'):
                    params.pop(verb, None)
                
        # if the user has specified their own model parameters, assign them            
        if isinstance(model_params, dict):
            params.update(model_params)

        # check if a model has been assigned
        if use_model is None:
            raise ValueError('Error assigning model, ensure you are selecting a valid model type or leave blank and try again.')

        # validate the eval metric
        eval_metric = self._validate_eval_metric(model=use_model, eval_metric=eval_metric)

        # set the parameters
        if params:
            use_model.set_params(**params)

        # if scale_imbalanced is required, determine if needs to be scaled
        # ignore multi class problems
        if scale_imbalanced and not self._is_regression:
            self._balance_classes()

        # if pca has been specified perform it on the X
        if self._perform_pca:
            X_train = self._pca(X_data=self._X_train, fit=True) 
            X_test = self._pca(X_data=self._X_test, fit=False)
            # record the pca x_train for model script
            self._X_train_pca_columns = X_train.columns
        else:
            X_train = self._X_train
            X_test = self._X_test

        # time the training
        start = time.time()
       
        # try except to catch failed models
        try:
            # train the model - if the model is xgboost, use the standard settings
            if isinstance(use_model, xgb.XGBClassifier):
                # set the object - binary or softprob - only applicable to xgboost
                use_model.set_params(objective=self._objective(), eval_metric=eval_metric)
                # using cross validation with binary classifier causes an error so only use when classes > 2
                if cross_validation and self.number_of_classes() > 2:
                    # fit the model
                    use_model.fit(X_train, self._y_train, eval_set=[(X_train, self._y_train), (X_test, self._y_test)], early_stopping_rounds=20)
                else:
                    # don't cross validate unless requested
                    use_model.fit(X_train, self._y_train)
                # get the model score and set the eval metric
                train_score = use_model.score(X_train, self._y_train)
            else:
                # if not xgboost
                if cross_validation:
                    # get the cv object
                    cv = utility.get_cv_object(n_splits=n_splits, n_repeats=n_repeats, regression=self._is_regression, stratify=self._stratify, random_state=self.__random_state) 
                    # run the model training with cv
                    cv_results = cross_validate(estimator=use_model, X=X_train, y=self._y_train, cv=cv, n_jobs=-1, return_estimator=True, scoring=eval_metric)
                    # get the scores from the training
                    train_score = np.mean(cv_results['test_score'])
                    # get the most recently trained estimator
                    use_model = cv_results['estimator'][-1]
                else:
                    # if the user has turned off cross validation, just fit the model
                    use_model.fit(X_train, self._y_train)
                
                # if for some reason the model wasnt fitted
                if not hasattr(use_model, 'predict') and not hasattr('predict_proba'):
                    # attempt to refit
                    use_model.fit(X_train, self._y_train)
                # get the score
                train_score = use_model.score(X_train, self._y_train)

        # if an exception is found, append it to failed models
        except Exception as err:
            # if using rapid ml return the invalidmodel class for retention
            if self._is_rapid_ml:
                print(f'Unable to train Model: {type(use_model).__name__}, check errors using the Pardon class failed_models attribute for more information.')
                return utility.InvalidModel(model=use_model, error=str(err))
            # if not using rapid_ml, raise the error normally
            else:
                raise err
  
        # end the train time
        end = time.time()
        # set the validation time
        self.model_training_time_mins = round((end - start) / 60, 2)
        # save the model
        self.model = use_model
        # set the model name
        self.model_type = type(self.model).__name__ + self.__DEFAULT_OPTIONS_STR if is_default else type(use_model).__name__       
        # datetime object containing current date and time
        now = datetime.now()
        # set the model unique name
        self.model_unique_identifier = f'{self.model_type}_{str(now.strftime("%Y%m%d%H%M%S%f"))}'
        # add datetime in format dd/mm/YY H:M:S of when model was trained
        self.model_trained_date = now.strftime(pardon_options.DATETIME_FORMAT)
        # get the predictions
        y_pred = use_model.predict(X_test)
        y_pred_proba = None if not hasattr(use_model, 'predict_proba') else use_model.predict_proba(X_test)
        # append if cross validation was used
        self._cross_validation_performed = cross_validation
        # specify n_splits and repeats
        self._n_splits = n_splits
        self._n_repeats = n_repeats
        # set the training and test scores
        self._set_train_scores(train_score=train_score, score_type=eval_metric)
        self._set_test_scores(y_preds=y_pred, y_preds_proba=y_pred_proba)
        # set the eval metric
        self.model_eval_metric = eval_metric
        # set the class distribution used in training
        self.train_class_distribution = self.__class_distribution(data=self._y_train.to_frame(name=self.target))
        self.test_class_distribution = self.__class_distribution(data=self._y_test.to_frame(name=self.target))
        # print a summary of the model training
        print(f'\nModel Type: {self.model_type}')
        print(f'Execution time (minutes): {self.model_training_time_mins}\n')
        print(f'Training scores:\n{self.model_train_scores}')
        print(f'Testing scores:\n{self.model_test_scores}\n')

    def get_feature_importance(self, suppress_errors:bool=False) -> dict:
        """
        Get the feature importance score for your data's columns. Note, this is only available after a model has been trained.

            Args:
                suppress_errors : bool, default False
                    If errors are suppressed, any errors will mean an empty dictionary object is returned instead of an error being raised.

            Returns:
                (dict) : Returns a dict object containing the column name and the corresponding ferature importance score.
        """
        # check this feature is available
        self.__check_model_available(func_name='get_feature_importance')

        feat_importances_series = self._get_feature_importance()

        if feat_importances_series is not None:
            output = feat_importances_series.to_dict()
            output = utility.sort_dictionary(output)
            return output

        # if the user wants to suppress errors, return empty dict
        if suppress_errors:
            # if an issue getting importances return empty
            return {}
        else:
            raise Exception('Unable to get feature importances for this dataset.')

    def _get_feature_importance(self) -> pd.Series:

        output = None
        # if not, use feature importance
        if hasattr(self.model, 'feature_importances_'):
            # get the feature importance from the model
            output = pd.Series(self.model.feature_importances_, index=self._X_train.columns)
            # get the top 20 and plot them into a model
        elif hasattr(self.model, 'coef_'):
            # use the coefficients from the model
            output = self.model.coef_[0] if not self._is_regression else self.model.coef_
        elif hasattr(self.model, 'estimators_'):
            try:
                # get the coef or feat importance from each model in the estimator
                output = np.mean([m.feature_importances_ if hasattr(m, 'feature_importances_') else m.coef_ for m in self.model.estimators_], axis=0) 
            except Exception:
                # catch any errors getting coef or features importance as set coefs to None so it won't continue
                return None

        # if no output return None
        if output is None:
            return None

        # get the output into a series
        cols = self._X_train.columns if not self._perform_pca else self._X_train_pca_columns
        output = pd.Series(abs(output), index=cols)

        return output

    def __get_shap_values(self):
        
        # get shap values
        output = None

         # if using xgboost get shap values
        if isinstance(self.model, xgb.XGBClassifier):
            # get the shap values
            # create the explainer for the model
            explainer = shap.TreeExplainer(self.model)
            output = explainer.shap_values(self._X_train)

        return output

    @__function_unavailable_after_data_clear  
    @__block_null_target
    def explain_model_predictions(self, refresh:bool=False, output_fullpath:str=None, max_features:int=20):
        """
        Show an explanation of model predictions using SHAP values or feature importance dependent on the type of model that has been trained.

            Args:
                refresh : bool, default False
                    Re-calculate the SHAP values. This happens by default if they have not already been calculated else the ones previously calculated will be used.
                output_fullpath : str, default None
                    The output fullpath to where you want your model explanations to be saved. The output fullpath should end with a reference to the filename as a png file. If None the output will be displayed but not saved.
                max_features : int, default 20
                    Maximum number of features to include in the model output.
        """
        # check a model is present
        self.__check_model_available(func_name='explain_model_predictions')

        # ensure max features is an integer
        utility.assert_item_type(item=max_features, item_types=[int])
        
        # if the user specifies to save the output, check here
        if output_fullpath:
            # if the directory does not exist or the filename does not end .db, return invalid
            output_fullpath = utility._check_save_parameters(fullpath=output_fullpath, filetype='.png')
       
        # if we are working with xgboost, print the shap values
        if isinstance(self.model, xgb.XGBClassifier):
            # get the shap values
            if refresh or not hasattr(self, '_shap_values'):
                self._shap_values = self.__get_shap_values()
            # get the readable class names
            class_names = self.classes()    
            # determine if we are showing the output or not
            show = False if output_fullpath else True
            # plot the features
            shap.summary_plot(self._shap_values, self._X_train, class_names=class_names, cmap=plt.get_cmap('tab10'), show=show, max_display=self.column_count()-1)
        else:
            # get the feature importances
            feat_importances = self._get_feature_importance()
            # if nothing means cannot be produced
            if feat_importances is None:
                print(f'Model explanation output is unavailable for the {self.model_type} Model.')
                return
            # try to plot
            try:
                # get the total number of features if less than 20, else set to 20
                totals_feats = len(self._X_train.columns) if len(self._X_train.columns) <= max_features else max_features
                # plot the feature importance up to 20tures
                feat_importances.nlargest(totals_feats).plot(kind='barh')
                # add the x label
                plt.xlabel(f'Top {totals_feats} Feature Importance')
            except Exception as err:
                # if an error occurs, print it
                print(err)
                return

        if output_fullpath:
            # avoid trimming issues
            plt.tight_layout()
            # save the model
            plt.savefig(output_fullpath)
            print(f'Model explanation for {self.model_type} successfully saved to: {output_fullpath}\n')
        else:
            plt.show()

    def __check_model_available(self, func_name=None):
        
        start_msg = f'The function: {func_name}' if func_name is not None else 'This function'

        # check if model has been trained, error if not.
        if self.model is None:
            raise KeyError(f'{start_msg} is not available until after the model has been trained. Use model.train_model() first and try again.')

    def __get_test_predictions(self):
        # use the model to make predictions
        X_test = self._pca(X_data=self._X_test, fit=False) if self._perform_pca else self._X_test
        # make a prediction
        predictions = self.model.predict(X_test)

        return predictions

    @__function_unavailable_after_data_clear
    @__block_null_target
    def model_summary(self, output_fullpath:str=None):
        """
        Display a summary of the model's performance. This will show a confusion matrix in a matplotlib diagram, and classification report printed to the terminal. This is only available to classification models.

            Args:
                output_fullpath : str, default None
                    The output fullpath to where you want your model summary to be saved. The output fullpath filename filetype should be a .png file. If None the output will be displayed but not saved.
        """
        # check a model is present
        self.__check_model_available()

        if self._is_regression:
            raise ValueError('The model_summary displays a confusion matrix which is not available for regression models.')

        # if the user specifies to save the output, check here
        if output_fullpath is not None:
            # if the directory does not exist or the filename does not end .db, return invalid
            output_fullpath = utility._check_save_parameters(fullpath=output_fullpath, filetype='.png')
        
        # get the predictions
        predictions = self.__get_test_predictions()
        # print the confusion matrix and classification report
        matrix_ = confusion_matrix(self._y_test, predictions)
        # set the class labels
        class_labels = self.classes()
        # create the figure
        fig = plt.figure()
        # add the subplot
        ax = fig.add_subplot(111)
        # create matshow
        _ = ax.matshow(matrix_, cmap=plt.cm.gray)
        # assign label values
        ax.set_xticklabels([''] + class_labels)
        ax.set_yticklabels([''] + class_labels)
        
        # this part sets the raw numbers to the grid
        for (i, j), z in np.ndenumerate(matrix_):
            ax.text(j, i, f'{z}', ha='center', va='center',
                    bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
        
        # set x and y axis
        plt.xlabel('Predicted')
        plt.ylabel('Actual')

        if output_fullpath:
            # avoid trimming issues
            plt.tight_layout()
            # save the model
            plt.savefig(output_fullpath)
            print(f'Model explanation for {self.model_type} successfully saved to: {output_fullpath}\n')
        else:
            # show the graph
            plt.show()
            
            # print classification report
            print(f'{classification_report(self._y_test, predictions, target_names=class_labels)}\n')

    def __get_feature_impact_dict(self, use_shap:bool=True) -> dict:

        # return a dict containing columns and their impact
        if isinstance(self.model, xgb.XGBClassifier) and use_shap:
            values = self.__get_shap_values()
            cols = self._X_train.columns
            classes = self.classes()
            output_items = {}
            # for each class given
            for i, class_ in enumerate(classes):
                # create a dictionary for that column
                col_dict = {}
                # for each row of data
                for x, vals in enumerate(values[i]):
                    # if there is no inner layer, just enumerate first
                    if len(values[i]) == len(self.columns) - 1:
                        # if not, set the value for that column
                        col_dict[cols[x]] = vals
                    else:
                        # for each row of data
                        for t, val in enumerate(vals):
                            # get the mean shap value
                            col_dict[cols[t]] = np.mean(np.abs(val))

                # sort the values
                col_dict = utility.sort_dictionary(col_dict)

                # add the column dictionary for that class
                output_items[class_] = col_dict
        else:
            # get the feature importance
            values = self._get_feature_importance()

            # if None return
            if values is None:
                return None

            # if the output was a series, make it a list
            if isinstance(values, pd.Series):
                values = values.tolist()

            # zip column names and values
            # if using pca, get the pca col names
            cols = self._X_train.columns if not self._perform_pca else self._X_train_pca_columns
            output_items = dict(zip(cols, values))

            # order the dict by values
            output_items = utility.sort_dictionary(output_items)

        return output_items

    def _script_details(self, use_shap:bool=True) -> list:
        # return a list containing the script details
        details = []

        lin_sep = '-----------------------------------------------------------\n'
        bullet = '\n\t--> '
        indented_bullet = '\n\t\t--> '
        # add the model unique identifier
        details.append('pardon Data Model Script\n')
        details.append(f'Script produced at: {datetime.now().strftime(pardon_options.DATETIME_FORMAT)}\n')
        details.append(lin_sep)

        # only add these details if we are doing machine learning and the model has been trained
        if self.target is not None and self.model is not None:
            details.append(f'Model Unique Identifier: {self.model_unique_identifier}\n')
            details.append(f'Model Type: {self.model_type}\n')
            details.append(f'Model Fullpath: {self.model_fullpath}\n')
            # if min scores were required before saving, add them here
            if self._model_metric_to_save is not None and self.model_fullpath is not None:
                details.append(lin_sep)
                details.append(f'Model Save Test Metric: {self._model_metric_to_save}\n')
                details.append(f'Model Save Minimum Test Score: {self._model_score_to_save}\n')
            # if the data was cleared at saving, specify that
            if self._data_cleared:
                details.append(lin_sep)
                details.append(f'Model Input Data Cleared: {self._data_cleared}\n')
            details.append(lin_sep)
            details.append(f'Model Trained Date: {self.model_trained_date}\n')
            details.append(f'Model Training Time (mins): {self.model_training_time_mins}\n')
            details.append(lin_sep)
            details.append(f'Model Predicts: {self.target}\n')
            details.append(lin_sep)
            # if we have a record of where the audits are held, print them
            if self.prediction_audit_fullpaths:
                af = bullet.join(self.prediction_audit_fullpaths)
                details.append(f'Prediction Audit Fullpath:{bullet}{af}\n')
                details.append(lin_sep)
            # add the accuracy scores
            details.append(f'Model Evaluation Metric Train: {self.model_eval_metric}\n')
            details.append(lin_sep)
            mtr = self.__dict_to_list(dict_item=self.model_train_scores)
            mtr = bullet.join(mtr)
            mts = self.__dict_to_list(dict_item=self.model_test_scores)
            mts = bullet.join(mts)
            details.append(f'Model Scores Train:{bullet}{mtr}\n')
            details.append(lin_sep)
            details.append(f'Model Scores Test:{bullet}{mts}\n')
            details.append(lin_sep)
            details.append(f'Train Split Size: {round(1 - self.test_size, 2)}\n')
            details.append(f'Test Split Size: {round(self.test_size, 2)}\n')
            details.append(lin_sep)
            # add if cross validation was performed
            if self._cross_validation_performed is not None:
                details.append(f'Cross Validation Performed: {self._cross_validation_performed}\n')
                details.append(lin_sep)
            # get the predictions
            predictions = self.__get_test_predictions() if not self._data_cleared else None
            # create the class distribution
            if not self._is_regression:
                cd = self.__dict_to_list(dict_item=self.class_distribution)
                cd = bullet.join(cd)
                details.append(f'Input Class Distribution:{bullet}{cd}\n')
                # add if class balancing occurred
                if self._classes_balanced:
                    details.append(lin_sep)
                    details.append(f'Classes Balanced Using: {self._sampling_strategy} Sampling\n')
                details.append(lin_sep)
                # add the class dfistribution used in training
                if self.train_class_distribution is not None:
                    for item in [(self.train_class_distribution, 'Train Data'), (self.test_class_distribution, 'Test Data')]:
                        cd = self.__dict_to_list(dict_item=item[0])
                        cd = bullet.join(cd)
                        details.append(f'{item[1]} Class Distribution:{bullet}{cd}\n')
                        details.append(lin_sep)
                try:
                    if predictions is not None:
                        report = classification_report(self._y_test, predictions, target_names=self.classes(), output_dict=True)
                        report = pd.DataFrame(report).transpose().to_string()
                        details.append(f'Model Test Classification Report:\n')
                        details.append(f'{report}\n')
                        details.append(lin_sep)
                        # get the proportions of output
                        props = utility.proportions(data=pd.Series(predictions), include_all=True)
                        # if we have the class labels, map them
                        if self.class_labels:
                            props = {self.class_labels.get(x): v for x, v in props.items()}

                        cd = self.__dict_to_list(dict_item=props)
                        cd = bullet.join(cd)
                        details.append(f'Model Test Predictions Class Distribution: {bullet}{cd}\n')
                        details.append(lin_sep)
                # ignore the error and just dont append it
                except:
                    pass
            else:
                # if regression model, get the averages
                train_averages = utility.get_data_averages(data=self.train_data[self.target])
                prediction_averages = utility.get_data_averages(data=predictions)
                cd = self.__dict_to_list(dict_item=train_averages)
                cd = bullet.join(cd)
                details.append(f'Target ({self.target}) Train Data Averages:{bullet}{cd}\n')
                details.append(lin_sep)
                if predictions is not None:
                    pcd = self.__dict_to_list(dict_item=prediction_averages)
                    pcd = bullet.join(pcd)
                    details.append(f'Target ({self.target}) Test Data Prediction Averages:{bullet}{pcd}\n')
                    details.append(lin_sep)
        else:
            # if no target, add the fact that no target was added
            message = '*** No Target column added so no Machine Learning Model was produced ***\n' if self.target is None else '*** Machine Learning Model not yet trained. ***\n'
            details.append(message)
            details.append(lin_sep)
            if self.model_fullpath is not None:
                details.append(f'Model Fullpath: {self.model_fullpath}\n')
                details.append(lin_sep)

        # add the data row counts
        if self.input_data_fullpath is not None:
            details.append(f'Input Data Fullpath: {self.input_data_fullpath}\n')
            details.append(lin_sep)
        train_rows = self.row_count(dataset="train")
        test_rows = self.row_count(dataset="test")

        if self.target is not None:
            details.append(f'Train Data Row Count: {train_rows}\n')
            details.append(f'Test Data Row Count: {test_rows}\n')
            details.append(f'Total Train and Test Data Row Count: {train_rows + test_rows}\n')
            details.append(lin_sep)

        details.append(f'Raw Data Row Count: {self.row_count(dataset="raw")}\n')
        details.append(f'Raw Data Column Count: {len(self.raw_data_columns)}\n')
        details.append(lin_sep)
        
        if self.target is not None:
            details.append(f'Raw Data Stratified: {self._stratify}\n')
            details.append(lin_sep)
            # if applicable add which scaler was used
            if self.scaler_used is not None:
                details.append(f'Data Scaler: {self.scaler_used.title().replace("_", " ")}\n')
                details.append(lin_sep)
        # get the raw data columns
        raw_cols_list = [col if col in self.columns else f'{col} **removed or renamed in data transformations**' for col in self.raw_data_columns]
        raw_columns = bullet.join(raw_cols_list)
        details.append(f'Raw Data Input Columns: {bullet}{raw_columns}\n')
        details.append(lin_sep)
        # add the columns used in the model
        if self.model is not None:
            cols_list = [f'{col} **created or renamed in data transformations**' if col not in self.raw_data_columns else col for col in self.columns if col != self.target]
            columns = bullet.join(cols_list)
            details.append(f'Model Input Columns: {bullet}{columns}\n')
            details.append(lin_sep)
            details.append(f'Model Input Column Count: {len(cols_list)}\n')
            # append a line separator
            details.append(lin_sep)
        # if pca was performed, confirm and add columns
        if self._perform_pca:
            pca_cols = bullet.join(self._X_train_pca_columns)
            details.append(f'Principal Component Analysis Columns: {bullet}{pca_cols}\n')
            details.append(lin_sep)
            # add the column counts
            details.append(f'Principal Component Analysis Column Count: {len(self._X_train_pca_columns)}\n')
            details.append(lin_sep)
        # get the classes
        classes = self.classes()
        # ensure the classes are in string format
        classes = [str(cls_) for cls_ in classes]
        # append them to a string
        if classes:
            classes = bullet.join(classes)
            details.append(f'Model Predicted Classes:{bullet}{classes}\n')
            # append a line separator
            details.append(lin_sep)
        
        if self.target is not None and self.model is not None:
            # get the model parameters
            params = self.model_parameters()
            # if they have been returned
            if params is not None:
                param_list = [f'{k}: {v}' for k, v in params.items()]
                param_list = bullet.join(param_list)
                details.append(f'Model Parameters: {bullet}{param_list}\n')
                # append a line separator
                details.append(lin_sep)
                # set message for best parameters searched
                msg = f'Best Parameters Searched:'
                # check if the best parameters were found
                if self.best_hyperparameters:
                    details.append(f'{msg} True\n')
                    # get the best parameters
                    best_params = self.best_hyperparameters.get(self.model_type)
                    if best_params is not None:
                        details.append(lin_sep)
                        best_params = [f'{k}: {v}' for k, v in best_params.items()]
                        best_params = bullet.join(best_params)
                        details.append(f'Best Model Parameters Found: {bullet}{best_params}\n')
                else:
                    details.append(f'{msg} False\n')
                # append a line separator
                details.append(lin_sep)

        # specify if the user used the Rapid ML Function
        details.append(f'Rapid ML Function Used: {self._is_rapid_ml}\n')
        details.append(lin_sep)

        # set the empty transforms
        transforms = []
        # set i to 0 in case no transformation are performed
        i = 0
        # less count is how many items we skipped to remove from the total count
        less_count = 0
        # functions to check
        MODEL_PARAM_FUNC_NAME = 'Find Best Model Parameters'
        # iterate through the transformation list
        for i, transformation in enumerate(self._transformation_list, start=1):
            func_name = transformation['function'] if transformation['func_name'] is None else transformation['func_name']
            func_name = self.__clean_func_name(func_name=func_name)

            function_name = f'Function: {func_name}'
            # get the args, print lambda source if found
            arg_list = [str(arg) if not callable(arg) else inspect.getsource(arg).strip() for arg in transformation['args']]
            args = f'Arguments: {arg_list}'
            # get the kwargs, print lambda source if found
            kwarg_list = [{k: v} if not callable(v) else {k: inspect.getsource(v).strip()} for k, v in transformation['kwargs'].items()]
            kwargs = f'Keyword Arguments: {kwarg_list}'
            # when adding best model parameters, only keep a record of when this was done for the current model
            # get the argument list, plus the values from every dictionary object in the keywords list
            if func_name == MODEL_PARAM_FUNC_NAME:
                # just get the values from the lists and list of dicts
                args_kwargs = arg_list + [v for d in kwarg_list for v in d.values() if v is not None]
                # if model type in the values, we want to keep this line
                keep = True if self.model_type in args_kwargs else False
            else:
                # a saftey net to true just in case func names are missed
                keep = True
            # remove items that we dont want to keep
            if not keep:
                less_count += 1
                continue

            # add the output
            output = bullet + function_name + indented_bullet + args + indented_bullet + kwargs
            transforms.append(output)

        # if pca was performed, add it to the transformation list as it is not retained in the standard format
        if self._perform_pca:
            transforms.append(f"{bullet}Function: PCA (Principal Component Analysis){indented_bullet}Arguments: []{indented_bullet}Keyword Arguments: [{{'n_components': {len(self._X_train_pca_columns)}}}]")

        # get the transforms into a list
        if i:
            # reduce i by the amount we skipped if any
            i -= less_count
            transforms = '\n'.join(transforms)
            details.append(f'Data Transformations ({i} Recorded):{transforms}\n')
        else:
            # if no data transformations performed, add that
            details.append(f'*** No Data Transformations Performed ***\n')

        # append a line separator
        details.append(lin_sep)

        # get which columns were filled with what values
        null_fills = self.__dict_to_list(dict_item=self._null_fills)

        # if null fills were found, put the list into a string
        if null_fills:
            null_fills = bullet.join(null_fills)
            # set the title and values
            details.append(f'[If Present] Nulls Filled with: {bullet}{null_fills}\n')
            # append a line separator
            details.append(lin_sep)

        # if the user added fail on, log them here
        if self.fail_ons:
            fail_ons = []
            # iterate through the fail ons and get the FailOn class details
            for item in self.fail_ons:
                fo = item['fail_on']
                fail_ons.append(f'Column: {fo.column}, Operator: {fo.operator}, Value: {fo.value}, Calculation: {fo.calculation}')
            # add them to the correct format
            fail_ons = bullet.join(fail_ons)
            # append the output
            details.append(f'Fail Ons Added: {bullet}{fail_ons}\n')
            # append a line separator
            details.append(lin_sep)

        # dont perform this if data has been cleared
        if not self._data_cleared and hasattr(self, '_X_train') and self.target is not None:
            feat_contribution = self.get_feature_contribution()
            # create a list
            feat_contribution = self.__dict_to_list(dict_item=feat_contribution)
            # put the list into a string
            feat_contribution = bullet.join(feat_contribution)
            # set the title
            title = f'Feature Contribution to {self.target}: '
            # append the output
            details.append(f'{title}{bullet}{feat_contribution}\n')
            # append the line sep
            details.append(lin_sep)
            # create a dict with features and their impacts
            feature_impact = self.__get_feature_impact_dict(use_shap=use_shap)
            # ensure feature impact is not none
            if feature_impact is not None:
                if self.classes() == list(feature_impact.keys()):
                    output_item = []
                    # for each class, create the feature importances
                    for key, val in feature_impact.items():
                        class_impact = self.__dict_to_list(dict_item=val)
                        class_impact = f'{indented_bullet}{indented_bullet.join(class_impact)}'
                        output_item.append(f'{key}:{class_impact}')

                    # make the final output
                    feature_impact = bullet.join(output_item)
                    # set the title
                    title = f'Feature Importance (SHAP Values) for Prediction of {self.target}: '
                else:
                    # create a list
                    feature_impact = self.__dict_to_list(dict_item=feature_impact)
                    # put the list into a string
                    feature_impact = bullet.join(feature_impact)
                    # set the title
                    title = f'Feature Importance for Prediction of {self.target}: '

                # append the output
                details.append(f'{title}{bullet}{feature_impact}\n')
                # append the line sep
                details.append(lin_sep)

        # if multiple models were tried, show them here
        if self.target is not None and self.model is not None:
            if self.rapid_ml_scores:
                models = [f"{x['model_type']} ({self.rapid_ml_score_metric}: {x['model_test_scores'].get(self.rapid_ml_score_metric, 'Unable to evaluate')})" for x in self.rapid_ml_scores.values()]
                models = bullet.join(models)
            elif self.target is not None:
                models =  bullet.join([self.model_type])
            # append the output
            details.append(f'Rapid ML Models Tested Successfully:{bullet}{models}\n')
            # append the line sep
            details.append(lin_sep)

        # check if any models failed, show them here
        if self.failed_models and self.target is not None:
            model_types = [x.model_type for x in self.failed_models]
            model_types = bullet.join(model_types)
            # append the output
            details.append(f'Models Failed during Training:{bullet}{model_types}\n')

        return details

    def __dict_to_list(self, dict_item) -> list:
        # turn the dict into a list
        return [f'{k}: {v}' for k, v in dict_item.items()]

    def __arrow(self, diagram, direction:str='down'):
        # adds arrows to the model diagram
        arrow = flow.Arrow(headwidth=0.75, headlength=0.75)

        if direction == 'down':
            return arrow.down(diagram.unit/2)
        elif direction == 'right':
            return arrow.right(diagram.unit/2)
        elif direction == 'left':
            return arrow.left(diagram.unit/2)

    def __clean_func_name(self, func_name:str) -> str:
        """
        Cleans the function name if it is a Pardon internal function that starts with an underscore
        """
        # if using an internal method, clean it
        if hasattr(self, func_name):
            clean_reg = r'^_+'
            func_name = re.sub(clean_reg, '', func_name, flags=re.I)

        return func_name

    def model_diagram(self, diagram_fullpath:str=None, fontsize:int=10):
        """
        Produces a diagram of the model data flow.

            Args:
                diagram_fullpath : str, default None {None, '.svg', '.eps', '.png', '.pdf' ,'.jpg'}
                    The fullpath to an output where you want to save the model diagram. The recommended filetype is '.svg'. If None the output will be displayed but not saved.
                fontsize : int, default 10
                    The size of the font to be used in the diagram.
        """
        # check if want to be saved
        if diagram_fullpath is not None:
            diagram_fullpath = utility._check_save_parameters(fullpath=diagram_fullpath, filetype=['.svg', '.eps', '.png', '.pdf', '.jpg'])

        # empty list to retain function names
        added = []
        # get counts of the function names in counter
        # we turn into a dict here so the update function below works correctly
        instance_counts = dict(collections.Counter([transformation['function'] for transformation in self._transformation_list]))
        # the lists of keys we only use and count once
        singles = self._SINGLE_INSTANCE_FUNCTIONS + self._FIT_TRANSFORM_FUNCS
        # update values of single instance keys
        instance_counts.update({k: 1 for k in singles if k in instance_counts.keys()})
        # set the total number of transformations
        num_transforms = sum(instance_counts.values())
        # set the first direction to be right
        right = True
        goes = 0

        try:
            with Drawing(file=diagram_fullpath) as d:
                d.config(fontsize=fontsize)
                # get the data name
                data_name = os.path.basename(self.input_data_fullpath) if self.input_data_fullpath is not None else 'data'
                # start the flow with the data
                d += (h := flow.Start(w=11, h=3.9).label(data_name))
                # iterate through the transformations
                for i, transformation in enumerate(self._transformation_list):
                    func_name = transformation['function'] if transformation['func_name'] is None else transformation['func_name']
                    func_name_clean = self.__clean_func_name(func_name=func_name)
                    # dont re-add functions that have a fit method or single instance, avoids duplicates
                    if func_name in singles and func_name in added:
                        continue
                    # this determines if we need to go horizontal to fit transforms
                    if (num_transforms > 6 and goes < 5) and i > 0:
                        direction = 'right' if right else 'left'
                        d += self.__arrow(diagram=d, direction=direction)
                        goes += 1
                    else: 
                        # create the arrow object
                        d += self.__arrow(diagram=d, direction='down')
                        # flip the right flag
                        right = not right
                        goes = 0

                    d += (h := flow.Decision(w=11, h=3.9).label(func_name_clean))
                    # add those that have been added
                    added.append(func_name)

                # if a model has been trained, add it here
                if self.model is not None:
                    d += self.__arrow(diagram=d, direction='down')
                    # check if rapid ml models were used
                    rapid_models = len(self.rapid_ml_scores)
                    # if so add the loop arrow
                    if rapid_models > 1:
                        d += (h := flow.Decision(w=10, h=4).label(f'Train models\n({rapid_models} tested)'))
                        d += flow.Wire('c', k=5, arrow='->').to(h.E).label(f'{rapid_models}')
                    else:
                        d += (h := flow.Decision(w=10, h=3.9).label('Train model'))
                    
                    # specify the model that was added
                    d += self.__arrow(diagram=d, direction='down').at(h.S)
                    d += (h := flow.Box(w=11, h=3.9).label(f'Model produced:\n{self.model_type}'))

                    # if audits are saved, add a reference
                    if self.prediction_audit_fullpaths:
                        d += self.__arrow(diagram=d, direction='right').at(h.E)
                        d += (h := flow.Decision(w=11, h=3.9).label(f'Predictions Saved'))

                # if a model was saved, add it
                if self.model_fullpath is not None:
                    d += self.__arrow(diagram=d, direction='down').at(h.S)
                    d += flow.Box(w=11, h=3.9).label(f'Model saved:\n{os.path.basename(self.model_fullpath)}')

        except Exception as err:
            # there is a bug here causing a tkinter error in the source code
            # if the error is different to the tkinter one, raise it
            if type(err).__name__ != 'TclError':
                raise err
            if diagram_fullpath is not None:
                print(f'\nModel diagram successfully saved to: {diagram_fullpath}\n')

    @__function_unavailable_after_data_clear
    def correlations(self, columns:list=[]):
        """
        Produce a correlation plot.

            Args:
                columns : str, list, default []
                    The columns to include in your correlation plot. Leave this to include all columns.

        """
        columns = self.__validate_column_argument(columns=columns, return_target=True)
        self.plot_data(show_as='correlation', columns=columns)

    @__function_unavailable_after_data_clear
    def histogram(self, column:str):
        """
        Produce a histogram plot.

            Args:
                column : str
                    The column to produce a histogram of.

        """
        if column not in self.data.columns:
            raise KeyError(f'The column: {column} does not exist. Please checking the column name and try again.')  

        try:
            visuals._plot_hist(data=self.data, x=column, n_bins='auto', as_prediction=False, target=self.target)
        except TypeError:
            raise TypeError(f'Error creating histogram for {column}. Fill or remove Null values and try again.')

    def model_script(self, script_fullpath:str, use_shap_values:bool=False):
        """
        Produces an output txt file containing the model details and data transformation script.

            Args:
                script_fullpath : str
                    The fullpath to where you want to save the model script. Needs to end with a file name with a .txt filetype.
                use_shap_values : bool, default False
                    If applicable, use SHAP values when generating feature importance. This will take significantly longer to run.
        """
        # check the save path is valid
        script_fullpath = utility._check_save_parameters(fullpath=script_fullpath, filetype='.txt')
        utility.assert_item_type(item=use_shap_values, item_types=[bool])
 
        print('Generating script...\n')

        # get all the details in a list
        details = self._script_details(use_shap=use_shap_values)

        # write the output of details to the file
        with open(script_fullpath, 'w') as f:
            f.writelines(details)

        print(f'Script successfully written to: {script_fullpath}\n')
    
    @__block_null_target
    def model_parameters(self) -> dict:
        """
        Return the trained model parameters.

            Returns:
                (dict) : dict object containing the model parameters
        """
        # check a model is present
        self.__check_model_available()

        # get the model params if available else return None
        try:
            model_params = self.model.get_params()
        except AttributeError:
            model_params = None

        return model_params
    
    def save_model(self, model_fullpath:str, min_test_metric:str='accuracy', min_test_score:float=None, clear_data:bool=False):
        """
        Save the model to the specified model fullpath. 

            Args:
                model_fullpath : str
                    The model fullpath to where you want your model to be saved. The output fullpath should end with a reference to the filename as a pkl file.
                min_test_metric : str, default 'accuracy'
                    The scoring metric to determine if the model has met the minimum required accuracy.
                min_test_score : float, int, default None
                    The minimum required model test score for the min_test_metric. The model will only be saved if the model has min_test_metric score HIGHER than the min_test_score. For error metrics as per the pardon.pardon_options.REDUCTION_SCORE_ON attribute, the model will only be saved if the error was LOWER than min_test_score.
                clear_data : bool, default False
                    Clear the retained input data from the model before saving to help significantly reduce the model object file size. If this is used many of the model's methods will no longer be available and the model can no longer be changed or updated.
        """
        utility.assert_item_type(item=model_fullpath, item_types=[str])
        utility.assert_item_type(item=min_test_metric, item_types=[str])
        utility.assert_item_type(item=min_test_score, item_types=[int, float, None])
        utility.assert_item_type(item=clear_data, item_types=[bool])

        # get the directory from the fullpath
        model_fullpath = utility._check_save_parameters(fullpath=model_fullpath, filetype='.pkl') 
        
        # these items are model specific so only required if a target column is present
        if self.target is not None and min_test_score is not None:
            # set the metric
            validated_metric = self._validate_scoring_metric(scoring_metric=min_test_metric)
            # if validated is different, it means it was changed, so raise an error to inform the user
            # this will only be present if the user has specified a min score
            if validated_metric != min_test_metric:
                raise ValueError(f'The min_test_metric of {min_test_metric} is invalid for this type of model. The recommended metric would be {validated_metric}. Check the min_test_metrics and try again.')

            # if the score is more than 1 and no an error metric, raise an error
            if  min_test_score > 1 and min_test_metric not in pardon_options.REDUCTION_SCORE_ON:
                raise ValueError(f'Please ensure all your min_test_score is less than 1 and try again.')

            # get the score achieved for the selected metric
            test_score = self.model_test_scores[min_test_metric]

            # for the error metrics, we want the scores to be below
            if min_test_metric in pardon_options.REDUCTION_SCORE_ON:
                if test_score > min_test_score:
                    raise Exception(f'The test score for {min_test_metric} was {test_score}, which is greater than the min_test_score of {min_test_score}, so the model has NOT been saved. This is because the following metrics aim to be reduced: {pardon_options.REDUCTION_SCORE_ON}')
            else:
                # if the test score wasn't achieved, raise an error
                if test_score < min_test_score:
                    raise Exception(f'The test score for {min_test_metric} was {test_score}, which is below the min_test_score of {min_test_score}, so the model has NOT been saved.')

            # run the pre deployment checks and make 20 predictions to see if any error
            if not self._data_cleared:
                self.__test_deployment(test_iterations=20)

            # if min test score, record what and where
            if min_test_score is not None:
                self._model_metric_to_save = min_test_metric
                self._model_score_to_save = min_test_score

        # if the user wants to clear out the data
        if clear_data:
            # clear out the raw data
            self.__clear_data()
        
        # save the class instance
        pickles.save_pickle(object=self, output_fullpath=model_fullpath)
  
        # log where the model is saved to    
        self.model_fullpath = model_fullpath

        mt = self.model_type if self.model_type is not None else 'Untrained'
            
        print(f'{mt} Model successfully saved to: {self.model_fullpath}\n')
        
    def __test_deployment(self, test_iterations=20):
        # double check the raw data has not been cleared
        if self.raw_data is not None:
            # iterate the specified number of times
            for _ in range(test_iterations):
                # get a random row for predictions
                data = self.get_sample_rows(n_rows=1)
                # get a prediction object
                # don't check the fail ons when testing the deployment
                p = self.predict(data=data, audit_fullpath=None, check_fail_ons=False)
                # if any predictions are invalid, raise an error and stop execution
                if p.error:
                    raise ValueError(f'{p.error} and the model was not saved.')
                
    def required_columns(self) -> list:
        """
        Return a list of the columns required for the model to be able to make a prediction from input data.

            Returns:
                (list) : a list of string column names that are required for the model to make a prediction.
        """
        # get those columns from the raw data still present in the training columns
        columns = [col for col in self.columns if col in self.raw_data_columns]
        
        return columns

    @__retain_transformation
    @__ignore_function_in_transforms
    @__non_data_func
    def remove_correlated_columns(self, max_correlation:float=0.9):
        """
        Remove columns with a greater correlation than the max_correlation argument. Of the 2 correlated columns, the column with the lower feature_contribution will be removed.

            Args:
                max_correlation : float, default 0.9
                    The maximum allowed correlation between 2 columns. Note, 1 is a perfect correlation. This accounts for both positive and negative correlations.
        """
        # check the variables
        utility.assert_item_type(item=max_correlation, item_types=[int, float])

        # get the correlated columns from the training data
        corr_cols = self.correlated_columns(max_correlation=max_correlation)

        # if we found correlated columns, remove them
        if corr_cols:
            # this will add these items to the script
            self.remove_columns(columns=corr_cols)

    @__block_null_target
    def correlated_columns(self, max_correlation:float=0.9) -> list:
        """
        Return a list of columns with a greater correlation than the max_correlation argument. Of the 2 correlated columns, the column with the lower feature_contribution will be returned.
            
            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame , default None
                    The data source used to train a machine learning model. Can be a file path or an object. If None the train_data data set will be used.
                max_correlation : float, default 0.9
                    The maximum allowed correlation between 2 columns. Note, 1 is a perfect correlation. This accounts for both positive and negative correlations.

            Returns:
                (list) : A list of string column names of the correlated columns. Of the 2 correlated columns, the column with the lower feature_contribution will be returned.
        """
        # check the variables
        utility.assert_item_type(item=max_correlation, item_types=[int, float])

        # ensure all values are numeric so we can get the correlation
        self._process_can_start(on_error='Data not ready to determine correlated columns. Please encode all your data to numeric values and try again.', check_rows=True)

        # remove the target col from the data 
        data = self.train_data.iloc[:].loc[:, self.train_data.columns != self.target].copy()
        # get the correlations
        corr = data.corr()
        # get the feature contribution for the columns
        feature_contribution = self.get_feature_contribution(suppress_errors=True)

        # get the columns - target has already been removed above
        columns = data.columns

        # get a list to append correlations too
        correlated = []

        # get those correlated more than the max
        for i in range(corr.shape[0]):
            for j in range(i+1, corr.shape[0]):
                if abs(corr.iloc[i,j]) > max_correlation:
                    # list of paired lists of columns
                    correlated.append([columns[i], columns[j]])

        # create a list for items to be removed
        items_for_removal = []

        # iterate through the correlated
        for pair in correlated:
            x, y = pair[0], pair[1]

            # skip where an item has already been removed
            if x in items_for_removal or y in items_for_removal:
                continue

            # get the min feature contribution score of the pair
            min_score = min(feature_contribution.get(x, 0), feature_contribution.get(y, 0))
            # remove the col with the lower contribution score
            remove_col = list(feature_contribution.keys())[list(feature_contribution.values()).index(min_score)]
            # add the column to remove
            items_for_removal.append(remove_col)

        return items_for_removal

    def __apply_data_transformations(self, data, ignore_functions:list=[], only_functions:list=[], caller_overwrite=None, verbose=False) -> pd.DataFrame:
        
        # the caller overwrite means we can also call the ignored functions if we want to
        caller = inspect.stack()[1][3] if caller_overwrite is None else caller_overwrite

        # the ignore function allows us to perform specific transformations when it suits us
        for transformation in self._transformation_list.copy():
            # get the function used, the args, and kwargs
            func = getattr(self, transformation['function'])
            args = transformation['args']
            kwargs = transformation['kwargs']
            # adjust the args and kwargs so only valid transformations take place
            args, kwargs = self.__check_args_kwargs_valid(func=func, args=args, kwargs=kwargs, data=data, caller=caller)

            # if ignore or only functions, test these
            if only_functions:
                if transformation['function'] not in only_functions:
                    continue
            if ignore_functions:
                if transformation['function'] in ignore_functions:
                    continue
            
            # only run if the above hasn't returned _InvalidFunction object
            if not isinstance(args, utility._InvalidFunction):
                if verbose:
                    print(f'[{datetime.now().strftime("%H:%M:%S")}] Running: {func.__name__}')
                # apply the transformation, if args is present, data would have been assigned during __check_args_kwargs_valid
                data = func(*args, **kwargs) if args else func(**kwargs)

        return data

    def __train_data_columns(self):
        # return the columns required for training
        cols = [col for col in self.columns if col != self.target]

        return cols

    @__block_null_target
    def predict(self, data, audit_fullpath:str=None, check_fail_ons:bool=True):
        """
        Returns a pardon.pardon_predict.Prediction class object containing a prediction for the input data.

            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data source used to train a machine learning model. Can be a file path or an object.
                audit_fullpath : str, default None
                    The fullpath to an output where you want to save a record of all predictions made by the model. This will output a sqlite database which will store all predictions. If the file does not exist one will be created, else the one specified will be used. A fullpath with a filename of type db is required.
                check_fail_ons : bool, default True
                    Check the data for any FailOns added to the model. If False, the Fail Ons will not be checked.

            Returns:
                (pardon.pardon_predict.Prediction) : Returns a pardon.pardon_predict.Prediction class object containing prediction data.
        """
        # check item types
        utility.assert_item_type(item=audit_fullpath, item_types=[str, None])
        utility.assert_item_type(item=check_fail_ons, item_types=[bool])

        # check the data is not none and 1 row is available
        if data is None:
            p = pardon_predict.Prediction()
            p._error_code = 400
            p.error = 'There is no input data. Please check the data input is not None and try again.'
            return p

        # check if the model has the model attribute, if not it's because the model has yet to be trained
        if self.model is None:
            p = pardon_predict.Prediction()
            p._error_code = 404
            p.error = 'This function is not available until after the model has been trained. Use class.train_model() first and try again.'
            return p

        # try except so we always will return a prediction object so no errors in production
        try:
            # ensure the input data is in the correct format - pd.DataFrame
            data = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)
            # ensure we have at least 1 row
            if len(data) < 1:
                p = pardon_predict.Prediction()
                p._error_code = 400
                p.error = 'No data has been found for prediction. Please check your input data and try again.'
                return p

            # check to ensure all necessary columns are present, ignore the target column as it is not required
            missing_columns = [col for col in self.required_columns() if col not in data.columns and col != self.target]

            # if all the columns are not present, raise a key error
            if missing_columns:
                p = pardon_predict.Prediction()
                p._error_code = 400
                p.error = f'The following columns are missing from your input data: {", ".join([str(x) for x in missing_columns])}'
                return p
            
            # perform fail on tests if required
            if self.__fail_ons and check_fail_ons:
                self.apply_fail_ons(data=data)

            # keep a record of the raw data before transformations if required for audit
            if audit_fullpath is not None:
                # make a copy if necessary
                raw_data_copy = data.copy()
                # turn into dict to keep in database
                raw_data_copy = raw_data_copy.to_dict(orient="records")
            else:
                raw_data_copy = None

            # apply the data transformations
            data = self.__apply_data_transformations(data=data)

            # set y to None so it gets passed to the prediction even when we don't have the correct value
            y = None

            # get the x, y so we can predict
            X, y = self._X_y_values(data=data)

            # if the x_train_columns does not exist, the user will have added their own model manually with no transformations so just get the input columns
            if not hasattr(self, '_X_train_columns'):
                cols = self.__train_data_columns()
            else:
                cols = self._X_train_columns

            # set the X value based on whether or not PCA was used
            X = self._pca(X_data=X[cols], fit=False) if self._perform_pca else X[cols]

            # set probabilities flag
            has_probabilties = True

            # get the predictions, probability for classification
            if hasattr(self.model, 'predict_proba'):
                predictions = self.model.predict_proba(X) 
            else:
                predictions = self.model.predict(X)
                # turn off probabiltiies class
                has_probabilties = False

            # get the class labels
            if not self._is_regression:
                # set the classes from the model
                model_classes = self.model.classes_

                if self.class_labels:
                    # set the class labels to be auto ml
                    class_labels = self.class_labels
                else:
                    # create a dictionary object in an attempt to get class output
                    class_labels = {x: x for x in self.classes()}
            else:
                # regression does not use this so set to None
                model_classes = None
                class_labels = None   

            # instantiate the prediction object
            p = pardon_predict.Prediction(target=self.target, model_identifier=self.model_unique_identifier, features=raw_data_copy, model_classes=model_classes, class_labels=class_labels, predictions=predictions, y=y, has_probabilties=has_probabilties)

            # if the prediction returned np.inf, this is likely because a scaler was used on the model but the input prediction data was not scaled.
            # this can happen if the user overwrites or adds a model manually using class.model = manual_model
            if p._has_infs:
                print('***WARNING:***\nThe prediction returned a numpy.inf value which cannot be used.\nThis may be because you are using a model that was trained on scaled data and the input data for the prediction has not been scaled.\nCheck to ensure the model was not added manually and ensure prediction data is scaled if appropriate and try again.')

            ## called automatically if audit set to true and the prediction object isn't invalid
            if audit_fullpath and p.error is None and p.predicted is not None:
                # check the audit fullpath is valid - do not error though so suppress error
                audit_fullpath = utility._check_save_parameters(fullpath=audit_fullpath, filetype='.db', suppress_error=True) 
                # create audit object and pass prediction
                p.audit = audits.Audit(prediction=p, fullpath=audit_fullpath)
                # print the error to inform users an error occurred but do not fail
                if p.audit._error is not None:
                    print(f'***WARNING:*** ERROR OCCURRED DURING AUDIT AND THE PREDICTION WAS NOT SAVED. DETAILS:\n\n{p.audit._error}')
                # retain a log of where the predictions have been audited
                elif audit_fullpath not in self.prediction_audit_fullpaths:
                    self.prediction_audit_fullpaths.append(audit_fullpath)

        # catch exceptions and log them    
        except Exception as err:
            raise err
            p = pardon_predict.Prediction()
            p._error_code = 500
            p.error =  f'{err}'

        return p

    def __get_dataset_for_plots(self, n_predictions=None, data=None, as_pca:bool=False, include_clusters:bool=False, as_transform:bool=False, include_scaling:bool=False, include_pred_raw:bool=False) -> pd.DataFrame:
        
        # if we are including clusters, check the model is ready
        if include_clusters:
            self.__cluster_model_available()

        # assign the data
        data_set = self.raw_data.copy() if data is None else data.copy() 

        if (n_predictions is not None and n_predictions) or include_pred_raw:
            # get predictions
            n_predictions = self.__get_n_predictions(n_predictions=n_predictions, data=data_set)
            # reset the index
            data_set.reset_index(drop=True, inplace=True)
            # get the row numbers randomly
            rows = np.random.choice(data_set.index.values, n_predictions, replace=False)
            # create a dataframe using the index
            plot_data = data_set.iloc[rows].loc[:, data_set.columns != self.target].copy()
            # get the predictions
            predictions = self.predict(data=plot_data.copy(), check_fail_ons=False)
            # check predictions were made
            if not predictions.predicted:
                raise Exception(f'No valid predictions could be made, the latest prediction gave the following error: {predictions.error}')
            
            # this means we want to include both target and predicted target
            if include_pred_raw:
                # add the predicted column as a new column rather than overwrite
                plot_data[f'{self.target}{pardon_options.PREDICTED_COL_SUFFFIX}'] = predictions.predicted
                # merge the old prediction column
                plot_data = pd.concat([plot_data, data_set[self.target]], axis=1)
            else:
                # add the predictions
                plot_data[self.target] = predictions.predicted

            # push plot back into dataset variable
            data_set = plot_data

        # if required, do the transformations
        if as_transform:
            data_set = self.__apply_data_transformations(data=data_set, ignore_functions=self._PLOT_SPLIT_COLS)

        # if we need clusters or pca, we need to get the transformations done
        if as_pca or include_clusters:
            if not as_transform:
                build_data = self.__apply_data_transformations(data=data_set.copy())
                # make sure we only keep rows that were not dropped
                data_set = data_set[data_set.index.isin(build_data.index)]
            else:
                build_data = self.__apply_data_transformations(data=data_set.copy(), only_functions=self._PLOT_SPLIT_COLS)

            # if required get pca columns
            if as_pca and self._X_train_pca_columns is not None:
                # get the cols
                cols = [col for col in data_set.columns if col != self.target]
                # add the pca cols to the dataset so they can be plotted
                data_set[self._X_train_pca_columns] = self._pca(X_data=build_data[cols].copy(), fit=False)
            # add the clusters to the dataset if required
            if include_clusters and self._cluster_column_name is not None:
                data_set[self._cluster_column_name] = build_data[self._cluster_column_name]
        # if required, include the scaling in the output
        elif include_scaling:
            data_set = self.__apply_data_transformations(data=data_set, only_functions=self._PLOT_SPLIT_COLS)
        
        return data_set

    def __get_n_predictions(self, n_predictions, data=None) -> int:
        
        # get the total rows
        total_rows = self.row_count(dataset='all') if data is None else len(data)

        if isinstance(n_predictions, str):
            # if n_predictions is not all, return none
            n_predictions = total_rows if n_predictions.lower() == 'all' else None
            # if none, the user input a string that was not all and is therefore invalid
            if n_predictions is None:
                raise ValueError('The n_predictions argument must be an integer or pass "all" to include all rows in your input dataset.')

        # set prediction to be total row if more than total rows
        n_predictions = total_rows if n_predictions > total_rows else n_predictions

        # check at least 1 prediction is requested
        if n_predictions < 1:
            raise ValueError('You have n_predictions set to less than 1. 1 or more predictions are required to use this feature.')

        return n_predictions

    def __validate_plot_data(self, data):

        # check if using input data or new data
        if data is not None:
            data = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)
            # if there is still an issue raise an error
            if len(data) == 0:
                raise ValueError('Error reading input data. Check your data source and try again or remove this argument for the raw input data to be used.')
        elif data is None and self._data_cleared == True:
            raise ValueError('The data in this model has been cleared so this function is unavailable unless you provide a valid dataset using the data argument.')

    def __validate_plot_args(self, data, **kwargs):
         # get valid columns for plotting
        valid_cols = [col for col in data.columns]
        # get all the column values to check
        all_col_values = list(kwargs.values())
        # get an empty list to use
        full_items = []
        # iterate through
        for item in all_col_values:
            # we don't want to include None
            if item is None:
                continue
            # if a list, we want to extend the list items
            if isinstance(item, list):
                full_items.extend(item)
            else:
                # if not a list, just append
                full_items.append(item)

        # get the columns that are not None and are not in valid cols
        invalid = [col for col in full_items if col not in valid_cols]

        # raise an error if any are invalid
        if invalid:
            raise ValueError(f'The column(s): {invalid} are invalid. Use any of the following columns and try again:\n-> {valid_cols}')

    @__function_unavailable_after_data_clear
    def plot_data(self, x:str=None, y:str=None, c:str=None, size:str=None, lat:str=None, lon:str=None, n_predictions='all', include_trendline:bool=True, show_as:str='scatterplot', data=None, as_prediction:bool=False, n_bins='auto', columns:list=[], randomise_columns:list=[], randomise_strategy:str='normal_distribution', include_original:bool=True, lineplot_estimator:str='count', apply_transformations:bool=True, remove_outliers:bool=False, z_threshold:float=3.0, outlier_columns:list=[]):
        """
        Plots your data onto a chart. Note, if using your target column, each prediction will be unique as rows are only used once for each prediction. The max n_predictions is therefore the number of rows in your input dataset.
            
            Args:
                x : str, None, default None
                    The column to plot on the x axis of the scatterplot.
                y : str, None, default None
                    The column to plot on the y axis of the scatterplot.
                c : str, None, default None
                    The column to use as data colours on the scatterplot, lineplot, or map.
                size : str, None, default None
                    The column to use as data marker size on the scatterplot, lineplot, or map.
                lat : str, None, default None
                    The column to use as the latitude data for the map. Only used when show_as = 'map'.
                lon : str, None, default None
                    The column to use as the longitude data for the map. Only used when show_as = 'map'.
                n_predictions : int, str, default 'all' {int, 'all'}
                    The number of predictions to plot on your scatterplot. Pass 'all' if you want to include the prediction for every row from your input dataset. Will only be relevant when including the target in one of your columns as predictions will not be made otherwise.
                include_trendline : bool, default True
                    Include a trendline on your scatterplot.
                show_as : str, default 'scatterplot' {'scatterplot', 'map', 'histogram', 'correlation', 'timeseries'}
                    The type of chart to display the data.
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame, default None
                    The data you want to get a plot. If not specified, data from the original raw input data will be used. 
                as_prediction : bool, default False
                    If including the target column on your chart, as_prediction=True means the predicted values will be used. as_prediction=False means the raw data from the target column will be used.
                n_bins : int, str, default 'auto' {int, 'auto'}
                    The number of bins to split the histogram. Note, if not using a numeric column, n_bins will be set to the number of unique items.
                columns : list, default [] (empty list)
                    Only used when displaying correlations. Specify which columns to include in the correlation heatmap.
                randomise_columns : list, default [] (empty list)
                    Choose columns to be randomised to test the impact of changing values on your model's predictions. 
                randomise_strategy : str, default 'normal_distribution' {'normal_distribution' , 'normal_distribution_in_range', 'random'}
                    The strategy determining how random values will be chosen. If normal distribution is selected, for numerical columns, a random value based on a normal distribution will be chosen. If normal distribution in range is selected, the minimum and maximum values allowed in the normal distribution will be the minimum and maximum values found in the column. For random, a random number between the minimum and maximum values will be chosen. For text columns, one item will be chosen from all items in the column, meaning that items that appear more often in the dataset, are more likely to be chosen for a more realistic choice. Note, this is only available for the scatterplot chart type.
                include_original : bool, default True
                    When using randomise_columns, include_original=True means a scatterplot will be produced both for your randomised data set, as well as the original data set.
                lineplot_estimator : str, default 'mean' {'mean', 'median', 'mode', 'sum', 'count', 'min', 'max', 'z_score'}
                    When using a lineplot chart, specify the type of aggregation to perform on the y axis. For text columns, this will automatically be set to 'count'. When using z_score, the max z_score for each data point will be used.
                apply_transformations : bool, default True
                    Apply the transformations to the data passed to the data parameter. If apply_transformations=False, none of the transformations from the script will be applied to your data. Use this if you have already applied the transformations manually to the data passed to the data parameter. If data=None and apply_transformations=False, the model's transformed training and test data will be used. If apply_transformations=True and data=None, the raw input data will be used as though it is a new, unseen dataset, and all transformations will be applied. If using randomised, apply_transformations will be set to True for the dataset regardless as a prediction needs to be made.
                remove_outliers : bool, default False
                    Remove any outliers in your dataset. Outliers are determined by the z_threshold.
                z_threshold : int, float, default 3.0
                    Rows with a z score  more than that specified will be determined as an outlier and removed using the remove_outliers method. A z score of 3.0 means the value is 3 standard deviations or more away from the column mean.
                outlier_columns : list, default [] (empty list)
                    Choose columns to be checked for outliers. If this is empty and ignore_outliers=True, all columns will be checked for outliers.
        """
        utility.assert_item_type(item=x, item_types=[str, None])
        utility.assert_item_type(item=y, item_types=[str, None])
        utility.assert_item_type(item=c, item_types=[str, None])
        utility.assert_item_type(item=size, item_types=[str, None])
        utility.assert_item_type(item=lat, item_types=[str, None])
        utility.assert_item_type(item=lon, item_types=[str, None])
        utility.assert_item_type(item=n_predictions, item_types=[int, str])
        utility.assert_item_type(item=include_trendline, item_types=[bool])
        utility.assert_item_type(item=show_as, item_types=[str])
        utility.assert_item_type(item=as_prediction, item_types=[bool])
        utility.assert_item_type(item=n_bins, item_types=[int, str])
        utility.assert_item_type(item=columns, item_types=[list])
        utility.assert_item_type(item=randomise_columns, item_types=[list, str])
        utility.assert_item_type(item=randomise_strategy, item_types=[str])
        utility.assert_item_type(item=include_original, item_types=[bool])
        utility.assert_item_type(item=lineplot_estimator, item_types=[str])
        utility.assert_item_type(item=apply_transformations, item_types=[bool])
        utility.assert_item_type(item=remove_outliers, item_types=[bool])
        utility.assert_item_type(item=z_threshold, item_types=[int, float])
        utility.assert_item_type(item=outlier_columns, item_types=[list, str])

        # set the valid chart types
        valid_charts = self.available_chart_types()

        # ensure the strategy is lower case
        randomise_strategy = randomise_strategy.lower()

        # the valid randomise strategies
        randomise_strat = ('random', 'normal_distribution', 'normal_distribution_in_range')

        # lower case 
        show_as = show_as.lower()

        # raise error if not valid
        if show_as not in valid_charts:
            raise ValueError(f'{show_as} is not a valid chart type. Please use one of the following and try again: {valid_charts}')

        # check the randomise strategy is valid
        if randomise_strategy not in randomise_strat and randomise_columns:
            raise ValueError(f'The randomise strategy: {randomise_strategy} is invalid, please choose one of the following and try again: {randomise_strat}')

        # get the chosen columns
        required_cols = [col for col in (x, y, c, size) if col is not None]

        # determine if we need both predicted target, and raw target in the data
        # if the user has selected the target for both x and y, or x or y = target_predicted, we know to retain both
        predicted_col_name = f'{self.target}{pardon_options.PREDICTED_COL_SUFFFIX}'

        # check to see if we need the predicted col and raw target
        if predicted_col_name in required_cols:
            include_pred_raw = True
        else:
            include_pred_raw = False

        # check if target column and predictions are required
        if (self.target in required_cols and as_prediction) or randomise_columns or (predicted_col_name in required_cols):
            # check the model has been trained before starting
            self.__check_model_available(func_name='plot_data (using predictions)')
            if randomise_columns:
                # if a string, change to a list
                if isinstance(randomise_columns, str):
                    randomise_columns = [randomise_columns]
                    randomise_columns = self.__keep_valid_columns(columns=randomise_columns)
                    if not randomise_columns:
                        raise ValueError(f'Your randomise columns are invalid. Please check you have supplied the correct column names and try again.')
                # randomise only available for a scatterplot
                if show_as != 'scatterplot':
                    show_as = 'scatterplot'
                    print('\n\n*** WARNING: show_as changed to "scatterplot" as this is the only valid type when using randmised columns. ***\n\n')
        else:
            # if we are not using the target column, set predictions to not required
            n_predictions = False

        # check if using input data or new data - will raise an error if invalid
        self.__validate_plot_data(data=data)
        # by default users do not want pca columns
        as_pca = False
        # check if pca columns are requested
        if self._X_train_pca_columns is not None:
            pca_cols = list(self._X_train_pca_columns)
            # if x or y is pca columns, get them
            if x in pca_cols or y in pca_cols:
                as_pca = True

        # determine if we need the clusters column
        include_clusters = True if (self._cluster_column_name in required_cols) or (self._cluster_column_name is not None and show_as == 'correlation') else False
        # create the object as we may need to use it
        randomised_data_set = None

        # if randomised columns, we need to get a random selection of data points for the columns specified
        if randomise_columns:
            # get the random data set, we keep the original as well as a random one
            data_set, randomised_data_set = self.__get_dataset_for_random(n_predictions=n_predictions, data=data, as_pca=as_pca, include_clusters=include_clusters, as_transform=apply_transformations, randomise_columns=randomise_columns, randomise_strategy=randomise_strategy, as_prediction=as_prediction, include_pred_raw=include_pred_raw)
        else:
            # if data is none, we just use the data from the model given
            if data is None:
                # if we are not applying any transformations, use the data in its already applied form - which is self.data
                # if we are applying transformations, we leave data as None as the function will then use the raw data
                # this is why this sets the data to be self.data if data is None and not apply_transformation
                if not apply_transformations:
                    data = self.data
            # get the data set for the plots
            data_set = self.__get_dataset_for_plots(n_predictions=n_predictions, data=data, as_pca=as_pca, include_clusters=include_clusters, as_transform=apply_transformations, include_scaling=False, include_pred_raw=include_pred_raw)

        # this validates that all arguments that pass columns in, that the columns exist and are valid
        # it ignores values set to the default of None
        self.__validate_plot_args(data=data_set, x=x, y=y, c=c, size=size, lat=lat, lon=lon, columns=columns)
        # check what we are attempting to plot and validate all arguments
        if show_as == 'map':
            if lon is None or lat is None:
                raise ValueError('When plotting to a map, please ensure you have included the lat, lon, and c for the column determining the colours.')
        elif show_as == 'scatterplot':
            if x is None or y is None:
                raise ValueError('Both x and y are required to plot a scatterplot.')
        elif show_as == 'histogram':
            if x is None:
                raise ValueError('You must supply an x value to create a histogram.')
        elif show_as == 'correlation':
            # if columns specified, use them
            if columns:
                if len(columns) < 2:
                    raise ValueError(f'More than 1 column is required for a correlation. Please add 2 or more columns from the column list and try again.')
        elif show_as == 'lineplot':
            lineplot_estimator = lineplot_estimator.lower()
            # check the estimator
            if lineplot_estimator not in visuals._LINEPLOT_ESTIMATORS.keys():
                raise ValueError(f'The estimator "{lineplot_estimator}" is invaid. Please choose from the following and try again: {list(visuals._LINEPLOT_ESTIMATORS.keys())}')

        # drop any na rows as it messes up the labels
        data_set.dropna(subset=required_cols, inplace=True)
        # drop randomised dataset rows if applicable
        if randomised_data_set is not None:
            randomised_data_set.dropna(subset=required_cols, inplace=True)

        # ignore outliers
        if remove_outliers:
            # remove outliers from our dataset
            data_set = self._remove_outliers(data=data_set, columns=outlier_columns, z_threshold=z_threshold)
            # if using a randmosed dataset, do the same
            if randomised_data_set is not None:
                randomised_data_set = self._remove_outliers(data=randomised_data_set, columns=outlier_columns, z_threshold=z_threshold)

         # we need to adjust x and y names if applicable
        if include_pred_raw:
            # if they are both the same name, rename y to be the predicted
            if x == self.target and y == self.target:
                y == f'{self.target}{pardon_options.PREDICTED_COL_SUFFFIX}'
            # we do not need to include this in the title as it is in the column name
            as_prediction = False

        # randomise column charting
        if randomise_columns:
            col_title = f' [{", ".join(randomise_columns)} randomised]'
            # does the user want both charts plotted
            if include_original:
                data = data_set
                randomised_data = randomised_data_set
            else:
                # if not, set randomised to None
                data = randomised_data_set
                randomised_data = None
            # plot the data
            visuals._plot_scatter(data=data, x=x, y=y, c=c, size=size, target=self.target,  classes=self.classes(), include_trendline=include_trendline, as_prediction=as_prediction, randomised_data=randomised_data, randomised_data_title=col_title)
        else:
            # display the plots
            if show_as == 'scatterplot':
                visuals._plot_scatter(data=data_set, x=x, y=y, c=c, size=size, target=self.target, classes=self.classes(), include_trendline=include_trendline, as_prediction=as_prediction, randomised_data=None, randomised_data_title=None)
            elif show_as == 'map':
                visuals.plot_map(data=data_set, target=self.target, lat=lat, lon=lon, c=c, size=size, as_prediction=as_prediction)
            elif show_as == 'histogram':
                visuals._plot_hist(data=data_set, x=x, n_bins=n_bins, as_prediction=as_prediction, target=self.target)
            elif show_as == 'correlation':
                visuals.plot_corr(data=data_set, columns=columns)
            elif show_as == 'lineplot':
                visuals._plot_lineplot(data=data_set, x=x, y=y, c=c, size=size, target=self.target, as_prediction=as_prediction, lineplot_estimator=lineplot_estimator)

    def __get_dataset_for_random(self, n_predictions, data, as_pca, include_clusters, as_transform, randomise_columns, randomise_strategy, as_prediction, include_pred_raw):

        # get the dataset to plot randomise
        if data is not None:
            data, data_set_random = data.copy(), data.copy()
        else:
            # if we are transforming, get raw data
            if as_transform:
                data = self.raw_data.copy()
            else:
                # if no transformations, take the normal data
                data = self.data.copy()
            # dataset random always needs to be
            data_set_random = self.raw_data.copy()

        # reset the index
        data.reset_index(inplace=True, drop=True)
        data_set_random.reset_index(inplace=True, drop=True)

        # determine weather or not to return predictions
        if as_prediction:
            use_n = n_predictions
        else:
            # if not using predictions, we need all predictions for the randomiser
            use_n = False
            n_predictions = 'all'

        # first get the dataset in numeric format - n predictions is either needed for the raw or not depending on whether we need predictions or not
        data_set_raw = self.__get_dataset_for_plots(n_predictions=use_n, data=data.copy(), as_pca=as_pca, include_clusters=include_clusters, as_transform=as_transform, include_scaling=False, include_pred_raw=include_pred_raw)

        # for each col, get the random values
        for col in randomise_columns:
            if is_numeric_dtype(data_set_random[col]):
                # get the min and max values
                min_ = min(data_set_random[col])
                max_ = max(data_set_random[col])
                # get the values depending on strategy
                if randomise_strategy in ('normal_distribution_in_range' , 'normal_distribution'):
                    # get the mean and std
                    mean_ = data_set_random[col].mean()
                    sd = np.std(data_set_random[col])
                    # if using normal distribution, just get random within distribution, if not, ensure the min and max values are never exceeded
                    if randomise_strategy == 'normal_distribution':
                        laf = lambda _: np.random.normal(mean_, sd) 
                    else:
                        laf = lambda _: utility.normal_dist_in_range(mean=mean_, sd=sd, min=min_, max=max_)
                else:
                    # if all integers, use rand int, else use floats
                    if np.array_equal(data_set_random[col], data_set_random[col].astype(int)):
                        laf = lambda _: utility.normal_dist_in_range(mean=mean_, sd=sd, min=min_, max=max_)
                    else:
                        laf = lambda _: np.random.uniform(min_, max_)
            else:
                # if not numeric, we just get a random item from the column
                laf = lambda _: np.random.choice(data_set_random[col])

            # select a random choice for each row
            data_set_random[col] = data_set_random[col].apply(laf)

        # for this one we use n predictions as we want new predictions following randmising
        data_set_random = self.__get_dataset_for_plots(n_predictions=n_predictions, data=data_set_random.copy(), as_pca=as_pca, include_clusters=include_clusters, as_transform=True, include_scaling=not as_transform, include_pred_raw=False)

        return data_set_raw, data_set_random

    def output_data(self, output_fullpath:str=None, n_predictions='all', data=None, as_prediction:bool=True, as_transform:bool=False, apply_fail_ons:bool=False) -> pd.DataFrame:
        """
        Outputs your data to a pandas.DataFrame as well as a new file if requested.

            Args:
                output_fullpath: str, None, default None {'.csv', '.txt', None}
                    The output fullpath you want the predictions to be saved to. If None the output will be printed to the terminal. Only .csv or .txt outputs are supported.
                n_predictions : int, str, default 'all' {int, 'all'}
                    The number of predictions to plot. Pass 'all' if you want to include the prediction for every row from your input dataset. This is only relevant if as_prediction=True.
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame, default None
                    The data you want to output. If not specified, data from the original raw input data will be used. 
                as_prediction : bool, default True
                    If including the target column on your chart, as_prediction=True means the predicted values will be used. as_prediction=False means the raw data from the target column will be used.
                as_transform : bool, default False
                    Output the data including all the data transformations that were applied through the model's script.
                apply_fail_ons: bool, default False
                    Apply any FailOns to your data prior to output. Equivalent to running the apply_fail_ons method.        
        """
        utility.assert_item_type(item=output_fullpath, item_types=[str, None])
        utility.assert_item_type(item=n_predictions, item_types=[str, int])
        utility.assert_item_type(item=as_prediction, item_types=[bool])
        utility.assert_item_type(item=as_transform, item_types=[bool])
        utility.assert_item_type(item=apply_fail_ons, item_types=[bool])

        if as_prediction and self.target is not None:
            # check the model has been trained before starting
            self.__check_model_available(func_name='output_data')
        else:
            n_predictions = False

        if output_fullpath is not None:
            output_fullpath = utility._check_save_parameters(fullpath=output_fullpath, filetype=['.txt', '.csv']) 

        # check if using input data or new data - will raise an error if invalid
        self.__validate_plot_data(data=data)

        # if the user has specified data, read it into a dataframe
        if data is not None:
            data = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)

        # if requested, apply the fail on tests
        if apply_fail_ons and self.__fail_ons:
            self.apply_fail_ons(data=data)

        include_clusters = True if self._cluster_column_name is not None else False

        # get the dataset - we do not want the transforms as we are plotting against the input raw data
        data_set = self.__get_dataset_for_plots(n_predictions=n_predictions, data=data, as_pca=False, include_clusters=include_clusters, as_transform=as_transform, include_scaling=as_transform, include_pred_raw=False)

        if output_fullpath is not None:
            self._save_dataframe(data=data_set, output_fullpath=output_fullpath)

        return data_set

    def _save_dataframe(self, data:pd.DataFrame, output_fullpath:str):
        # save a dataframe to a file
        if output_fullpath.endswith('.csv') or output_fullpath.endswith('.txt'):
            data.to_csv(output_fullpath, index=False)
            print(f'File successfully saved to: {output_fullpath}\n')
        else:
            raise TypeError(f'The file type in {output_fullpath} is invalid, please use .csv or .txt and try again.')

    def __cluster_model_available(self):
        # check to see if the cluster model is created
        if self._cluster_model is None:
            raise Exception('You cannot use this function until the cluster has been created. Use the create_clusters method first to create the clusters and try again.')

    def __cluster_models(self) -> dict:
        models = pardon_models._cluster_models()
        models = {str(model.__name__).lower(): model for model in models}

        return models

    @__function_unavailable_after_data_clear
    def apply_sentiment(self, columns:list=[], return_as='text'):
        """
        Apply sentiment analysis to the text in the columns specified using the nltk library. The sentiment analysis will be placed in a new column called <original column name>_sentiment.

            Args:
                columns : str, list, default [] (empty list)
                    The name(s) of the columns to apply the sentiment analysis to.
                return_as: str, dict, default 'text'
                    Define the output of your sentiment analysis. If 'text', each string will have a sentiment analysis determined to be 'positive', 'neutral', or 'negative'. You can supply a dictionary object outlining what value to return for each sentiment type. For example, return_as=dict('positive'=3, 'neutral'=2, 'negative'=1).
        """
        utility.assert_item_type(item=return_as, item_types=[str, dict])

        if isinstance(return_as, str):
            return_as = return_as.lower()

        # ensure the valid options are set
        if not isinstance(return_as, dict) and return_as != 'text':
            raise ValueError(f'{return_as} is not a valid return_as option. Pease supply a dictionary containing postive, neutral, negative and the values to return for each, else return_as="text" and try again.')

        # validate the columns argument - this ensure all columns are given if none are specified
        columns = self.__validate_column_argument(columns=columns, return_target=False)
        # retain only valid columns
        columns = self.__keep_valid_columns(columns=columns)
        # only retain columns that are object data type
        columns = self.__check_for_type(data=self.data, columns=columns, dtype='object')

        if columns:
            self.__convert_data_using_func(convert_func=self._apply_sentiment, apply_convert_to_train=True, apply_convert_to_test=True, columns=columns, return_as=return_as)

    @__retain_transformation
    def _apply_sentiment(self, *, data, columns, return_as='text') -> pd.DataFrame:
        # apply the sentiment analysis
        for column in columns:
            # do not try sentiment analysis on numeric columns
            if not is_numeric_dtype(data[column]):
                # get the new column name
                col_name = f'{column}_sentiment'
                # apply sentiment
                data[col_name] = data[column].apply(lambda x: utility.get_sentiment(text=x, return_as=return_as))

        return data

    @__function_unavailable_after_data_clear
    def create_clusters(self, column_name:str, n_clusters:int=3, model:str='KMeans'):
        """
        Cluster data into n number of groups. Select from the available clustering models.

            Args:
                column_name: str
                    The name of the column you want to add the clustered groups to.
                n_clusters : int, default 3
                    The number of clusters to create for the dataset. Each row will be assigned one of the clustered groups.
                model : str, default 'KMeans'
                    The clustering model used to create your clusters.
        """
        # ensure all values are numeric so we can perform clustering
        self._process_can_start(on_error='Data not ready to create clusters. Please encode all your data to numeric values and try again', check_rows=True)
        utility.assert_item_type(item=column_name, item_types=[str])
        utility.assert_item_type(item=n_clusters, item_types=[int])
        utility.assert_item_type(item=model, item_types=[str])
        # get the cluster models
        models_dict = self.__cluster_models()
        model = model.lower()

        # ensure the correct model is available.
        if model not in models_dict.keys():
            raise ValueError(f'The model {model} is not valid for this function. The available cluster models are: {list(models_dict.keys())}')

        # ensure the column name does not already exist
        if column_name in self.columns:
            raise ValueError(f'The column name: {column_name} is invalid because it already appears in the data columns. Please change this to a unique name and try again.')

        if self.model is not None:
            raise Exception('Clusters cannot be appended to data after your model has been trained. Use this method before training your model.')
        
        # create the clustering model
        use_model = models_dict.get(model)
        # if the model hasn't been found, error
        if use_model is None:
            raise Exception(f'Error getting model {model}, please try a new model or ignore the argument and try again.')
        # create the model object
        use_model = use_model()
        # attempt to add the random state and n_clusters
        if 'random_state' in use_model.get_params().keys():
            use_model.set_params(random_state=self.__random_state)
        if 'n_clusters' in use_model.get_params().keys():
            use_model.set_params(n_clusters=n_clusters)
        # remove the target column
        cols = [col for col in self.train_data.columns if col != self.target]
        # fit the Model on all train data
        use_model.fit(self.train_data[cols])
        # save the model and retain meta data
        self._cluster_model = use_model
        self._cluster_column_name = column_name
        self._n_clusters = n_clusters
        # create the data for train, test
        self.__convert_data_using_func(convert_func=self._add_clusters, apply_convert_to_train=True, apply_convert_to_test=True, column_name=column_name, model=model)

    @__retain_transformation
    def _add_clusters(self, *, data, column_name, model='KMeans') -> pd.DataFrame:
        # model parameter not used but we retain it for the sake of the script
        predictions = self._get_cluster_predictions(data=data)
        # add to the dataframe as a new column
        data[column_name] = predictions

        return data

    def _get_cluster_predictions(self, data):

        cols = [col for col in data.columns if col != self.target and col != self._cluster_column_name]
        # dbscan has fit_predict
        if hasattr(self._cluster_model, 'fit_predict'):
            predictions = self._cluster_model.fit_predict(data[cols])
        else:
            predictions = self._cluster_model.predict(data[cols])

        return predictions

    def transform(self, data, include_ignored_transformations:bool=False, verbose:bool=False) -> pd.DataFrame:
        """
        Apply the model script data transformations to a data set.

            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data to apply the model's data transformations.
                include_ignored_transformations : bool, default False
                    Include transformations that are ignored in predictions.
                verbose : bool, default False
                    Show which transformations are being applied.

            Returns:
                (pandas.DataFrame) : Returns your input data after the model's script of data transformations have been applied.
        """
        # ensure the data is pushed to a dataframe
        data = utility.data_reader(data=data, encoding=self._encoding, sep=self._sep, error_bad_lines=self._error_bad_lines)
        # setting the caller to be transform means it will run even ignored transformations - setting to apply_data_transformations mean they will be ignored
        caller_overwrite = 'transform' if include_ignored_transformations else '__apply_data_transformations'
        data = self.__apply_data_transformations(data=data, caller_overwrite=caller_overwrite, verbose=verbose)

        return data

    @property
    def fail_ons(self) -> list:
        # so it cannot be amended
        return self.__fail_ons

    def delete_fail_on(self, fail_on_id:int):
        """
        Delete a FailOn class item from your model.

            Args:
                fail_on_id : int
                    The FailOn object ID that you added using the pardon.Pardon.add_fail_on method. You can check the fail_on_ids using the pardon.Pardon.fail_ons attribute.
        """
        if not self.__fail_ons:
            raise Exception('No FailOns have been added.')

        found = False

        for i, fail_on_item in enumerate(self.__fail_ons):
            if fail_on_item['fail_on_id'] == fail_on_id:
                self.__fail_ons.pop(i)
                found = True
                break
        
        if found:
            print(f'FailOn id: {fail_on_id} deleted successfully.\n') 
        else:
            raise ValueError(f'The fail_on_id: {fail_on_id} is not found in the FailOns. The valid fail on ids are: {self.__fail_ons}.\n')

    def add_fail_on(self, fail_on:make_rules.FailOn, strategy:str='fail', warn_fullpath=None):
        """
        Add a FailOn class item to your model. FailOns will be applied to the input dataset before a prediction unless explicitly requested not to.

            Args:
                fail_on : FailOn class
                    The FailOn object that will be applied to your data.
                strategy: str, default 'fail' {'fail', 'warn'}
                    How to react to a FailOn invoking a failure. Fail will raise an error and all processing will stop. Warn means a warning will be printed to the terminal. A line will be written in the warn_fullpath file if provided.
                warn_fullpath: str, None, default None
                    When using the strategy of warn, where to output the FailOn errors.
        """
        STRATEGIES = ('fail', 'warn')

        utility.assert_item_type(item=fail_on, item_types=[make_rules.FailOn])
        utility.assert_item_type(item=strategy, item_types=[str])

        strategy = strategy.lower()

        if strategy not in STRATEGIES:
            raise ValueError(f'The strategy: {strategy}, is invalid. Please use one of the following: {STRATEGIES}, when determining the FailOn starategy.')

        if warn_fullpath is not None:
            # if the user has provided a full path but left the strategy, warn them and error to ensure they know
            if strategy == 'fail':
                raise ValueError(f'The strategy is set to {strategy} but you have provided a warn_fullpath. Remove the warn fullpath or set strategy="warn" and try again.')

            warn_fullpath = utility._check_save_parameters(fullpath=warn_fullpath, filetype=['.txt', '.csv']) 
  
        if fail_on.column not in self.columns:
            raise ValueError(f'The column: {fail_on.column} in your Fail On is not present in the data columns. The valid data columns are as follows: {self.columns}')

        # if it's the first failon, the id is 1 else get the max id that already exists
        if len(self.__fail_ons) == 0:
            fail_on_id = 1
        else:
            keys = [fail_on_item['fail_on_id'] for fail_on_item in self.__fail_ons]
            fail_on_id = max(keys) + 1
        
        new_fail_on_dict = {'fail_on_id': fail_on_id, 'fail_on': fail_on, 'strategy': strategy, 'warn_fullpath': warn_fullpath}

        # inform the user if they are using the target column this will result in error if used during a prediction
        if fail_on.column == self.target or (isinstance(fail_on.subset, dict) and self.target in fail_on.subset.keys()):
            print(f'\n*** WARNING: The target column {self.target} is used in the FailOn fail_on_id: {fail_on_id}. If used in a Prediction, THIS WILL CAUSE AN ERROR. ***\n')

        # add the rule to the rule ditc
        self.__fail_ons.append(new_fail_on_dict)

        print(f'FailOn id: {fail_on_id} was added successfully.\n')

    def apply_fail_ons(self, data):
        """
        Apply the FailOn items to the specified dataset.

            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data to apply the FailOn to.
        """
        if not self.__fail_ons:
            raise Exception('No FailOns have been added. Use the add_fail_on method to add a FailOn and try again.')

        # check all the fail ons and apply them to the data
        for fail_on in self.__fail_ons:
            fail_on_id = fail_on['fail_on_id']
            fo = fail_on['fail_on']
            strategy = fail_on['strategy']
            # check the fail on
            check_fail_on = fo.apply_fail_on(data=data, encoding=self._encoding, sep=self._sep)
            # if it fails, see what to do
            if check_fail_on.failed == True:
                # set the fail error message
                err_msg = f'Fail on id: {fail_on_id} has invoked a Fail On. Details: {fo}\n'
                if strategy == 'fail':
                    raise ValueError(err_msg)
                else:
                    warn_fullpath = fail_on['warn_fullpath']
                    dt = datetime.now().strftime(pardon_options.DATETIME_FORMAT)
                    outline = f'Fail On id: {fail_on_id}, Details: {fo}, Date: {dt}\n'
                    if warn_fullpath is not None:
                        # we open as append in case we use the same fullpath
                        with open(warn_fullpath, 'a') as f:
                            f.write(outline)
                    # inform the user a fail on was invoked
                    print(err_msg)

    @__block_null_target
    @__function_unavailable_after_data_clear
    def model_learning_curve(self, n_splits:int=5, n_tests:int=10, score_metric:str='accuracy'):
        """
        Plots the training and cross-validation scores for varying test and training sizes. Note, depending on the type of model, this can take a significant amount of time to complete.

            Args:
                n_splits : int, default 5
                    The number of splitting iterations during cross validation.
                n_tests : int, default 10
                    The number of different test sizes to try. The test sizes are then determined by (total rows x 0.8) / n_tests.
                    For example, if your data has 10000 rows, and you set n_tests=5, this means (10000 x 0.8) = 8000, 8000 / 5 = 1600, therefore the following test sizes will be used: 1600, 3200, 4800, 6400, 8000.
                score_metric : str, default 'accuracy'
                    Specify which metric is to be used when performing the cross-validation. You can see the available scoring metrics using the available_scoring_metrics method. The default for regression models is 'r2'.
        """
        # check the data is ready to be trained before starting
        self._process_can_start(on_error='Data not ready for to produce a model learning curve. Please encode all your data to numeric values and try again.', check_rows=True)
        # ensure there is a model
        self.__check_model_available(func_name='model_learning_curve')

        utility.assert_item_type(item=n_splits, item_types=[int])
        utility.assert_item_type(item=n_tests, item_types=[int])
        utility.assert_item_type(item=score_metric, item_types=[str])

        MIN_TESTS_SPLIT = 2
        if n_tests < MIN_TESTS_SPLIT or n_splits < MIN_TESTS_SPLIT:
            raise ValueError(f'n_tests and n_splits must be {MIN_TESTS_SPLIT} or more. Please check your arguments and try again.')

        # ensure the eval metric is valid
        score_metric = self._validate_scoring_metric(scoring_metric=score_metric)
        cv = utility.get_cv_object(n_splits=n_splits, n_repeats=1, regression=self._is_regression, stratify=self._stratify, random_state=self.__random_state) 
        # learning curve requires a max of 0.8 of the total data available, so we scale down
        total_rows = len(self.data)
        max_tests = int(math.floor(total_rows * 0.8))
        min_tests = int(round(max_tests / n_tests, 0))
        intervals = utility.create_intervals(start=min_tests, end=max_tests, interval=min_tests)
        train_cols = self.__train_data_columns()
        X = self.data[train_cols]
        y = self.data[self.target]
        # create the learning curve
        visuals.create_learning_curve(model=self.model, x=X, y=y, intervals=intervals, cv=cv, score_metric=score_metric)