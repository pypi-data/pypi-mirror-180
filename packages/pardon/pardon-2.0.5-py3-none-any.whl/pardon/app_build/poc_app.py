import collections
from imp import reload
import os, sys
import time
from attr import attr

import streamlit as st
import PIL
from st_aggrid import AgGrid
import matplotlib.pyplot as plt
import pyautogui
import pandas as pd
import seaborn as sns

import pardon
import statics


def __refresh():
    """Refresh the session"""
    pyautogui.hotkey('f5')


def default_model_filepath(selected_run:int=None) -> str:
    """Return the default filepath for saving the pardon class object"""
    
    # if a specific run is passed, get that model from the run history, if not, get the current model
    model = st.session_state.ml_model if selected_run is None else st.session_state.run_history[selected_run]['model']

    # this creates the unique name for the file along with the .pkl type
    if isinstance(model, pardon.Pardon):
        output = os.path.join(f'{os.getcwd()}', f'{model.model_unique_identifier}.pkl')
    else:
        output = ''

    return output


def set_logo(width=350):
    '''Set the logo if the image can be found, if not, set a text title'''

    CAPTION = 'The Data Transformation & Machine Learning Accelerator'
    CUR_DIR = os.path.dirname(os.path.realpath(__file__))
    logo = os.path.join(CUR_DIR, 'data', 'pardon_logo.png')

    if os.path.exists(logo):
        # open and apply the image
        logo_image = PIL.Image.open(logo)
        st.image(logo_image,
            caption=CAPTION,
            use_column_width=False,
            width=width)
        apply_markdown(markdown="<hr style='text-align: left; margin-top: 0px; margin-bottom: 0px;'>")
    else:
        FILENAME_MARKDOWN = f"""
                    <h1 style='text-align: left; margin-top: 0px; margin-bottom: 0px;'>
                        pardon
                    </h1>
                    <h4 style='text-align: left; margin-top: 0px; margin-bottom: 0px;'>
                        {CAPTION}
                    </h4>
                    <hr>
                    """
        apply_markdown(markdown=FILENAME_MARKDOWN)


def apply_markdown(markdown:str):
    '''Apply markdown'''
    st.markdown(markdown, unsafe_allow_html=True)


def set_page_configuration():
    """Set the page configuration values"""
   
    # turn off pyplot warnings
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(layout="wide", page_title='pardon')
    st.markdown(statics.PAGE_MARKDOWN, unsafe_allow_html=True)
    st.markdown(statics.BUTTON_MARKDOWN, unsafe_allow_html=True)
    st.markdown(statics.EXPANDER_MARKDOWN, unsafe_allow_html=True)
    st.markdown(statics.SIDEBAR_MARKDOWN, unsafe_allow_html=True)

    # set the session keys to be empty dicts to refresh them
    for key in ['pardon_keys', 'run_history']:
        if key not in st.session_state:
            setattr(st.session_state, key, {})


def text_markdown(text, textsize, colour='black', font_family=statics.FONT_FAMILY):
    '''Create the markdown for the filename'''

    markdown = f'<p style="font-family: {font_family};color:{colour}; font-size: {textsize}px;">{text}</p>'

    return markdown


def build_data_preview():
    '''Build a data preview from the dataframe'''

    with st.spinner('Creating data preview...'):
        st.session_state.raw_data_preview_expander = st.expander('Raw Data Preview', expanded=True)
        with st.session_state.raw_data_preview_expander:
            AgGrid(st.session_state.raw_data.head(100), key='aggrid_rd', fit_columns_on_grid_load=False)


def build_file_uploader(message='Upload your data file', types=['csv', 'txt', 'xls']):
    """Build the file uploader box"""
    st.session_state.file_holder = st.empty()
    st.session_state.file = st.session_state.file_holder.file_uploader(message, type=types)


def check_refresh():
    """This refreshes the page if the refresh button has been pressed"""
    if st.session_state.new_file_button:
        
        for key in st.session_state.keys():
            del st.session_state[key]

        # clear down keys
        st.session_state.pardon_keys = {}
        st.session_state.run_history = collections.defaultdict(dict)
        # rerun the script
        __refresh()


def assign_file_info():
    """Assign the raw data file information"""
    # get the file information and data
    st.session_state.bytes_data = st.session_state.file.getvalue()
    # get file size
    st.session_state.file_size = len(st.session_state.bytes_data)
    # read into data frame
    st.session_state.raw_data = pardon.utility.data_reader(data=st.session_state.file)
    # get some meta data
    st.session_state.raw_data_columns = list(st.session_state.raw_data.columns)
    st.session_state.n_raw_data_rows = len(st.session_state.raw_data)
    st.session_state.n_raw_data_columns = len(st.session_state.raw_data_columns)
    # get rid of the file uploader
    st.session_state.file_holder.empty()


def set_file_details():
    """Get the details from the uploaded file"""
    # set title and file details
    apply_markdown(markdown=text_markdown(text=f'File size: {round(st.session_state.file_size / 1024**2, 2)}MB', textsize=12, colour='DimGrey'))
    apply_markdown(markdown=text_markdown(text=f'Columns: {st.session_state.n_raw_data_columns}', textsize=12, colour='DimGrey'))
    apply_markdown(markdown=text_markdown(text=f'Rows: {st.session_state.n_raw_data_rows}', textsize=12, colour='DimGrey'))
    apply_markdown(markdown=statics.HORIZONTAL_LINE_MARDOWN )
    # if we need to refresh the page
    check_refresh()
    

def set_session_states():
    '''Add variables into the session state'''

    states = ['file','dt_model', 'ml_model', 'z_threshold', 'pca_n_components', 'train_model_kwargs', 'chart_score_metric', 'mlt_run_num']

    for state in states:
        if state not in st.session_state:
            setattr(st.session_state, state, None)


def data_transform():
    '''Perform the data transforms'''
    # always performed on raw data
    drop_nulls = True if st.session_state.drop_or_fill == 'Drop' else False
    st.session_state.z_threshold = 3 if not st.session_state.z_threshold else st.session_state.z_threshold
    st.session_state.pre_build_kwargs = dict(convert_to_numeric=st.convert_to_numeric_cols, fill_non_numeric=st.fill_non_numeric, convert_to_string=st.convert_to_string_cols)

    # retain the build kwargs so we can reuse when we train the model
    st.session_state.build_kwargs = dict(train_models=False, drop_duplicates=st.session_state.drop_duplicates, 
                                            remove_outliers=st.session_state.remove_outliers, z_threshold=st.session_state.z_threshold, ignore_target_outliers=False,
                                            label_encode=False, remove_unhelpful_columns=st.session_state.remove_unhelpful,
                                            scale_data=False, drop_nulls=drop_nulls, fill_numeric_with=st.session_state.fill_numeric, fill_text_with=st.session_state.fill_text)
    st.pre_build_funcs = []
    st.session_state.pre_build_source_code = []
    with st.spinner('Transforming data...'):
        error = False
        # get the model and transform the data
        try:
            dt_model = pardon.Pardon(data=st.session_state.raw_data.copy(), target=None)
            if st.session_state.pre_build_kwargs['convert_to_numeric']:
                if str(st.session_state.pre_build_kwargs['fill_non_numeric']).lower() == 'drop':
                    remove_rows_kwargs = {col: 'non-numeric' for col in st.session_state.pre_build_kwargs['convert_to_numeric']}
                    dt_model.remove_rows_containing(column_items=remove_rows_kwargs)
                    st.pre_build_funcs.append({'func': 'remove_rows_containing', 'kwargs': dict(column_items=remove_rows_kwargs)})
                    st.session_state.pre_build_source_code.append(f'paml.remove_rows_containing(column_items={remove_rows_kwargs})') 

                non_numeric = 'median' if str(st.session_state.pre_build_kwargs['fill_non_numeric']).lower() == 'drop' else st.session_state.pre_build_kwargs['fill_non_numeric']
                dt_model.convert_to_numeric(columns=st.session_state.pre_build_kwargs['convert_to_numeric'], fill_non_numeric=non_numeric)
                st.pre_build_funcs.append({'func': 'convert_to_numeric', 'kwargs': dict(columns=st.session_state.pre_build_kwargs['convert_to_numeric'], fill_non_numeric=non_numeric)})
                st.session_state.pre_build_source_code.append(f'paml.convert_to_numeric(columns={st.session_state.pre_build_kwargs["convert_to_numeric"]}, fill_non_numeric="{non_numeric}")') 
            if st.session_state.pre_build_kwargs['convert_to_string']:
                string_cols = [col for col in st.session_state.pre_build_kwargs['convert_to_string'] if col not in st.session_state.pre_build_kwargs['convert_to_numeric']]
                dt_model.convert_to_string(columns=string_cols)
                st.pre_build_funcs.append({'func': 'convert_to_string', 'kwargs': dict(columns=string_cols)})
                st.session_state.pre_build_source_code.append(f'paml.convert_to_string(columns={string_cols})') 

            dt_model.rapid_ml(**st.session_state.build_kwargs)
        except Exception as e:
            error = True
            st.error(f'Error encountered transforming data: {e}')

    if not error:
        # set the model variable
        st.session_state.dt_model = dt_model
        show_message(text='Data transformations completed successfully.', seconds=1)


def show_message(text:str, seconds:int, success=True):
    """Display a success or error message for a numnber of seconds"""

    if success:
        msg = st.success(text)
    else:
        msg = st.error(text)
    # clear the message after a number of seconds
    time.sleep(seconds)
    msg.empty()


def set_run_history():

    if isinstance(st.session_state.ml_model, pardon.Pardon):
        run_num = len(st.session_state.run_history) + 1
        info_dict = dict(model = st.session_state.ml_model, code=st.session_state.train_model_kwargs)
        st.session_state.run_history[run_num] = info_dict


def view_transformed_data():
    '''Show the transformed data preview'''

    if dt_model_available():
        if 'aggrid_dt' in st.session_state and st.session_state.aggrid_dt is not None:
            st.session_state.aggrid_dt.empty()
        with st.spinner('Getting data preview...'):
            apply_markdown(markdown=text_markdown(text=f'Columns: {len(st.session_state.dt_model.data.columns)}&nbsp &nbsp &nbsp &nbspRows: {len(st.session_state.dt_model.data)}', colour='DimGrey', textsize=14))
            AgGrid(st.session_state.dt_model.data.head(100), fit_columns_on_grid_load=False, key='aggrid_dt')
        

def build_data_transform():
    '''Build the data transformation widget'''
    st.session_state.data_transformation_expander = st.expander("Data Transformations", expanded=True)

    with st.session_state.data_transformation_expander:
        st.write('Select and perform data Transformations')

        st.session_state.dtr1col1, st.session_state.dtr1col2, st.session_state.dtr1col3, st.session_state.dtr1col4 = st.columns(4)
        st.session_state.dtr2col1, st.session_state.dtr2col2, st.session_state.dtr2col3, st.session_state.dtr2col4 = st.columns(4)
        st.session_state.dtr3col1, _, _, _ = st.columns(4)
        st.session_state.dtr4col1, st.session_state.dtr4col2 = st.columns((2, 1))
        st.session_state.dtr5col1, _ = st.columns((2, 1))
        st.session_state.dtr6col1, st.session_state.dtr6col2, _ = st.columns((1, 1, 4))

        # set the basic transformations on row 1
        with st.session_state.dtr1col1:
            st.session_state.drop_duplicates = st.selectbox('Drop Duplicate Rows', [True, False])
        with st.session_state.dtr1col2:
            st.session_state.remove_unhelpful = st.selectbox('Remove Unhelpful Columns', [False, True], help='Remove columns that are deemed unhelpful. An unhelpful column is one categorised as one of the following: 1. Every data item in the column is the same value. 2. The proportion of rows that are null exceeds 50%. 3. The column data type is a string and every data item in the column is different.')
        with st.session_state.dtr1col3:
            st.session_state.remove_outliers = st.selectbox('Remove Outliers', [False, True], help='If True, rows with values that are more than n standard deviations from the mean will be removed')
        
        # set transformations on row 2
        if st.session_state.remove_outliers:
            with st.session_state.dtr1col4:
                st.session_state.z_threshold = st.slider('Z Threshold', min_value=0.1, max_value=5.0,  help='The Z Threshold determines the acceptable number of standard deviations away from the mean. If a row contains a value that exeeds the z threshold, it will be removed')
        
        with st.session_state.dtr2col1:
            st.session_state.drop_or_fill = st.selectbox('Deal with Nulls', ['Fill', 'Drop'], help='If Drop, any null values in the row means the row will be dropped, if Fill, specify what to replace Null values with for text and numeric columns')
            # this allows users to specify what nulls get filled with
            if st.session_state.drop_or_fill == 'Fill':
                with st.session_state.dtr2col2:
                    st.session_state.fill_numeric = st.selectbox('Fill Numeric Column Nulls', pardon.statics.AVERAGES,  help='The value to fill Nulls found in numeric columns')
                with st.session_state.dtr2col3:
                    val = get_session_state(item_name='fill_text', default='Unknown')
                    st.session_state.fill_text = st.text_input('Fill Text Column Nulls', value=val, help='The value to fill Nulls found in text columns')

        with st.session_state.dtr3col1:
            show_advanced = st.checkbox('Show Advanced Options')

            if show_advanced:
                all_cols = list(st.session_state.raw_data.columns)
                with st.session_state.dtr4col1:
                    st.convert_to_numeric_cols = st.multiselect('Convert columns to numeric', options=all_cols)
                with st.session_state.dtr4col2:
                    st.fill_non_numeric = st.selectbox('Fill non-numeric', ['Mean', 'Median', 'Mode', 'Drop'], help='Fill non-numeric rows with the column average or select drop to have these rows removed.')
                with st.session_state.dtr5col1:
                    st.convert_to_string_cols = st.multiselect('Convert columns to string', options=all_cols)

        # set the button and submit methods
        with st.session_state.dtr6col1:
            st.session_state.submit_dt_button = st.button('Transform Data')

        if st.session_state.submit_dt_button:
            # perform the transformations
            data_transform()
            # update the session states
            update_dt_states()

        if dt_model_available():
            export_data()

        # this displays the data after it has been transformed
        view_transformed_data()

    # this builds the data transformation model diagram
    build_dt_diagram()


def update_dt_states():
    # set the items items to record their state
    dt_keys = ['drop_duplicates','remove_unhelpful',
                'remove_outliers','z_threshold',
                'drop_or_fill', 'fill_numeric',
                'fill_text']

    # update those items
    update_state(keys=dt_keys)


def set_ml_kwargs():

    # set the parameters that are not held in session state
    models = 'all' if not st.session_state.models else st.session_state.models
    pca_n_components = None if not st.session_state.pca else st.session_state.pca_n_components
    max_correlation = 0.9 if st.session_state.remove_correlated_columns else None
    scale_data = False if not st.session_state.scaler_type else True
    scaler_type = str(st.session_state.scaler_type).replace(' ', '_')
    ordinal_encode = True if 'ordinal' in str(st.session_state.encoding_type).lower() else False
    max_features = 'all' if st.session_state.max_features == len(st.session_state.dt_model.columns) - 1 else st.session_state.max_features

    # create the ml model kwargs
    st.session_state.train_model_kwargs = dict(models=models, train_models=True, eval_metric=st.session_state.eval_metric, 
                                                score_metric=st.session_state.score_metric, stratify=st.session_state.stratify, ordinal_encode=ordinal_encode, label_encode=True,
                                                scale_data=scale_data, scaler_type=scaler_type, scale_imbalanced=st.session_state.scale_imbalance, 
                                                max_features=max_features, pca_n_components=pca_n_components, 
                                                find_best_model_parameters=st.session_state.find_best_params, use_ohe=st.session_state.ohe, 
                                                max_correlation=max_correlation, cross_validation=st.session_state.cross_validation)


def rapid_ml(full_kwargs):
    columns = [] if not st.session_state.columns else st.session_state.columns
    ml_model = pardon.Pardon(data=st.session_state.raw_data.copy(), target=st.session_state.target, test_size=st.session_state.test_size, is_regression=st.session_state.as_regression, columns=columns, stratify=st.session_state.stratify)
    
    for funcs in st.pre_build_funcs:
        func_name = funcs['func']
        if func_name == 'remove_rows_containing':
            ml_model.remove_rows_containing(**funcs['kwargs'])
        elif 'convert_to_numeric' in func_name:
            ml_model.convert_to_numeric(**funcs['kwargs'])
        elif 'convert_to_string' in func_name:
            ml_model.convert_to_string(**funcs['kwargs'])
    ml_model.rapid_ml(**full_kwargs)
    st.session_state.ml_model = ml_model


def train_models():
    '''Train the models based on the user input'''

    set_ml_kwargs()
    # get the kwargs we will build our model using - we do it like this so we can have the audit in the diagram
    # this is a combination of those used on the data transforms and the ml specific ones
    full_kwargs = pardon.utility.merge_dictionaries(dict1=st.session_state.train_model_kwargs, dict2=st.session_state.build_kwargs)

    with st.session_state.rmlr7col1:
        # train the mnodel
        with st.spinner('Training models... Please wait, this may take a while...'):
            rapid_ml(full_kwargs)
        
        # set the default save path
        st.session_state.default_model_filepath = default_model_filepath()
        set_run_history()
        # this shows the message for a specified set of time then clears
        show_message(text=f'{len(st.session_state.ml_model.rapid_ml_scores)} Models trained successfully.', seconds=3)


def export_data():
    '''Export the transformed data'''

    with st.session_state.dtr6col2:
        st.session_state.export_data_button = st.button('Export Data')
    
    def_path = os.path.join(os.getcwd(), f'{os.path.splitext(st.session_state.file.name)[0]}_export.csv')
    st.session_state.export_data_filepath = st.text_input('Select Save location and filename (must be saved as .txt or .csv)', value=def_path)

    if st.session_state.export_data_button:
        if not st.session_state.export_data_filepath:
            show_message(text='Please specify a valid filepath and try again.', seconds=1, success=False)
        else:
            st.session_state.dt_model.data.to_csv(st.session_state.export_data_filepath, index=False)
            show_message(text=f'Data successfully saved to: {st.session_state.export_data_filepath}', seconds=1, success=True)

     
def save_model():
    '''Save the ML Model'''

    with st.session_state.rmlr6col2:
        st.session_state.save_model_button = st.button('Save Model')

    with st.session_state.rmlr7col1:
        st.session_state.save_model_filepath = st.text_input('Select Save location and filename (must be saved as .pkl)', value=st.session_state.default_model_filepath)

        if st.session_state.save_model_button:
            if not st.session_state.save_model_filepath or not isinstance(st.session_state.ml_model, pardon.Pardon) or st.session_state.ml_model.model is None:
                err_message = 'Please specify a valid filepath and try again.' if not st.session_state.save_model_filepath else 'Model not ready to save. Please use Train Model(s) first and try again.'
                show_message(text=err_message, seconds=1, success=False)
            else:
                st.session_state.ml_model.save_model(model_fullpath=st.session_state.save_model_filepath)
                show_message(text=f'{st.session_state.ml_model.model_type} Model successfully saved to: {st.session_state.save_model_filepath}', seconds=1, success=True)

  
def get_metrics_models() -> dict:
    """The the evaluation and scoring metrics, and available models for the model type"""

    # this determines if the model is inferred to be regression and if the user has requested it be inferred
    inferred_regression = pardon.utility._check_if_regression(data=st.session_state.raw_data.copy(), target=st.session_state.target)
    user_regression = True if st.session_state.model_type == 'Regression' else False

    # set the marker for what models we will display
    st.session_state.as_regression = inferred_regression if st.session_state.model_type =='Infer' else user_regression
    # get the metrics and return in a dictionary
    eval_metrics = pardon.pardon_models._st_get_evaluation_metrics(st.session_state.as_regression)
    score_metrics = pardon.pardon_models._st_get_scoring_metrics(st.session_state.as_regression)
    available_models = pardon.pardon_models._st_get_models(st.session_state.as_regression)

    output_dict = dict(eval_metrics=eval_metrics, score_metrics=score_metrics, available_models=available_models)

    return output_dict


def build_rapid_ml():
    """Build the Rapid ML section of the site"""

    # rapid ml
    st.session_state.rapid_ml_expander = st.expander("Rapid ML", expanded=True)

    with st.session_state.rapid_ml_expander:
        st.write('Use your transformed data to build a machine learning model')
         # this is the top row, we will leave it solo
        st.session_state.rmlr1col1, st.session_state.rmlr1col2, st.session_state.rmlr1col3, st.session_state.rmlr1col4 = st.columns(4)
        st.session_state.rmlr2col1, st.session_state.rmlr2col2, st.session_state.rmlr2col3, st.session_state.rmlr2col4 = st.columns(4)
        st.session_state.rmlr3col1, st.session_state.rmlr3col2, st.session_state.rmlr3col3, st.session_state.rmlr3col4 = st.columns(4)
        st.session_state.rmlr4col1, st.session_state.rmlr4col2, st.session_state.rmlr4col3, st.session_state.rmlr4col4 = st.columns(4)
        st.session_state.rmlr5col1, st.session_state.rmlr5col2 = st.columns(2)
        st.session_state.rmlr6col1, _ = st.columns((1, 3))
        st.session_state.rmlr7col1, _ = st.columns((2, 1))

        available_columns = list(st.session_state.dt_model.columns)

        # get the target column
        with st.session_state.rmlr1col1:
            st.session_state.target = st.selectbox('Target Column', available_columns, index=len(available_columns)-1, help='This is the column you want to predict.')

        with st.session_state.rmlr1col2:
            st.session_state.model_type = st.selectbox('Model Type', ['Infer', 'Regression', 'Classification'], index=0, help='If your "Target column" contains discrete values, this will be a Classification model, if continuous values like a price, a Regression Model. Use "Infer" to let this be determined automatically.')   
                
        with st.session_state.rmlr1col3:
            st.session_state.stratify = st.selectbox('Stratify Data', [True, False], index=0, help='Use the same proportion of classes encountered in the dataset when splitting data into train and test. Only applicable to Classification models.')

        with st.session_state.rmlr1col4:
            st.session_state.test_size = st.slider('Test Size', min_value=0.05, max_value=0.95, value=0.3, help=f'The proportion of data to use for test. 0.3 means 30% of the data will be used for testing.')

        with st.session_state.rmlr2col1:
            st.session_state.find_best_params = st.selectbox('Find Best Model Parameters', [False, True], index=0, help='Basic hyper-parameter tuning using GridSearchCV will be performed for each model. This can take SEVERAL HOURS, EVEN DAYS TO RUN, depending on your compute.')

        with st.session_state.rmlr2col2:
            st.session_state.cross_validation = st.selectbox('Perform Cross-Validation', [True, False], index=0, help="Perform cross validation during model training. This should only ever be switched off if you're simply testing an idea and want to reduce training time. It is advised you always perform cross validation.")
        
        with st.session_state.rmlr2col3:
            st.session_state.ohe = st.selectbox('Perform One-Hot Encoding', [False, True], index=0, help='If True, all object/text columns with 10 or fewer unique values will be One-Hot Encoded.')

        with st.session_state.rmlr2col4:
            st.session_state.scale_imbalance = st.selectbox('Scale Imbalanced Data', [True, False], index=0, help='If imbalanced class distribution is found, scale using under or over sampling to balance class distribution before training.')

        # this infers the datatype and sets the correct drop down items
        metrics_models = get_metrics_models()
        eval_metrics = metrics_models['eval_metrics']
        score_metrics = metrics_models['score_metrics']
        available_models = metrics_models['available_models']
        
        with st.session_state.rmlr3col1:
            st.session_state.eval_metric = st.selectbox('Model Evaluation Metric', eval_metrics, help='This is the metric your model will use to determine its performance during training and adjust its parameters accordingly.')

        with st.session_state.rmlr3col2:
            st.session_state.score_metric = st.selectbox('Model Scoring Metric', score_metrics, index=0, help='This is the metric to determine which of the models trained performed the best during testing and will be selected.')

        with st.session_state.rmlr3col3:
            st.session_state.pca = st.selectbox('Perform PCA', [False, True], index=0, help='Perform Principal Component Analysis (PCA) and reduce the columns to n components.')

            if st.session_state.pca:
                with st.session_state.rmlr3col4:
                    st.session_state.pca_n_components = st.number_input('PCA Number of Components', min_value=1, max_value=None, value=2, help='The number of components to reduce your columns to during PCA.')

        with st.session_state.rmlr4col1:
            st.session_state.remove_correlated_columns = st.selectbox('Remove correlated Columns', [False, True], index=0, help='If True, columns with a correlation of 0.9 or higher will be removed. Of the 2 correlated columns, the column with the lower feature contribution score will be removed.')

        with st.session_state.rmlr4col2:
            st.session_state.max_features = st.slider('Maximum Columns', min_value=2, max_value=len(available_columns) - 1, value=len(available_columns) - 1, help='The maximum number of columns to keep in the dataset. The top n performing columns will be retained. Note, the "Target Column" is not included in the training columns and so the maximum is number of columns - 1.')

        with st.session_state.rmlr4col3:
            st.session_state.scaler_type = st.selectbox('Scale Data', ['Standard Scaler', 'Min Max Scaler', 'Max Abs Scaler',False], index=0, help='Scale the data using a standard or min-max scaler. Use False to not scale.')

        with st.session_state.rmlr4col4:
            st.session_state.encoding_type = st.selectbox('Encode non-numeric Data', ['Label Encoding', 'Ordinal Encoding'], index=0, help='Encode non-numeric data. Ordinal encoding will be based on ascending values. A non-numeric target column will be label encoded by default.')

        with st.session_state.rmlr5col1:
            st.session_state.models = st.multiselect('Include Models (leave blank to include all valid models)',  available_models, default=None, help='Select which models you want to train. The best performing model will be selected based on the Scoring Metric.')
        
        with st.session_state.rmlr5col2:
            st.session_state.columns = st.multiselect('Include Columns (leave blank to include all)',  available_columns, default=None, help='Select the columns you wish to include from your input dataset.')

        with st.session_state.rmlr6col1:
            st.session_state.submit_ml_button = st.button('Train Model(s)')

        st.write('Trained models can be saved at the Rapid ML Selected Model section')

        # if the user clicks the submit button
        if st.session_state.submit_ml_button:
            try:
                # empty the expanders prior to load
                empty_ml_expanders()
                train_models()
                # update the keys so we can retain them for the user
                update_ml_states()
            except ValueError as err:
                st.error(err)


def update_ml_states():
    """Update and retain the states used in the rapid ML section"""

    # set the items items to record their state
    ml_keys = ['target', 'model_type','stratify', 
                'test_size', 'find_best_params', 
                'cross_validation', 'ohe', 'scale_imbalance', 
                'eval_metric', 'score_metric', 'pca', 'pca_n_components', 
                'remove_correlated_columns', 'max_features', 'scaler_type',
                'columns', 'models']

    # update those items
    update_state(keys=ml_keys)


def build_rapid_ml_output():
    """Build the rapid ML sections that become available after a model has been trained"""

    build_selected_model()
    build_model_comparisons()
    build_model_test_scores()
    build_model_feature_importance()
    build_model_feature_contribution()
    build_model_diagram()
    build_model_tester()
    build_model_source_code()


def build_model_feature_importance():
    """Build the section that displays a chart with feature importance"""
    run_index = get_current_run_index()
    runs = get_runs()

    st.session_state.select_feature_importance_expander = st.expander(f'Rapid ML Feature Importance', expanded=False)

    with st.session_state.select_feature_importance_expander:
        fir1, _ = st.columns((1, 10))
        chrc, _ = st.columns((0.8, 1))
        with fir1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='fi_run')

        with st.spinner('Building Chart...'):
            model =  st.session_state.run_history[run_selection]['model']
            feat_imp = model.get_feature_importance()
            with chrc:
                st.pyplot(build_feature_chart(data=feat_imp, title='Feature Importance'))


def build_model_feature_contribution():
    """Build the section that displays a chart with feature contribution"""
    run_index = get_current_run_index()
    runs = get_runs()

    st.session_state.select_feature_contribution_expander = st.expander(f'Rapid ML Feature Contribution', expanded=False)

    with st.session_state.select_feature_contribution_expander:
        fir1, _ = st.columns((1, 10))
        chrc, _ = st.columns((0.8, 1))
        with fir1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='fc_run')

        with st.spinner('Building Chart...'):
            model =  st.session_state.run_history[run_selection]['model']
            feat_cont = model.get_feature_contribution()
            with chrc:
                st.pyplot(build_feature_chart(data=feat_cont, title='Feature Contribution'))


def build_feature_chart(data:dict, title:str):

    data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

    sns.barplot(
        x=list(data.values()), 
        y=list(data.keys()), 
        orient='h',
        dodge=False,
        palette="ch:.25")

    plt.title(title)
    plt.show()


def build_model_source_code():
    """Build the section that displays the associated pardon source code for reproducing the model"""

    run_index = get_current_run_index()
    runs = get_runs()

    st.session_state.select_source_code_expander = st.expander(f'Rapid ML pardon.Pardon Source Code', expanded=False)

    with st.session_state.select_source_code_expander:
        rmscr1, _ = st.columns((1, 10))
        with rmscr1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='rmsc_run')

        sc = get_source_code(run_number=run_selection)

        st.code(sc, language='python')


def get_current_run_index() -> int:
    """Return the index position of the current run"""

    # it will usually be the last item in the list but this will ensure it is always correct
    runs = get_runs()
    cur_run = current_run_number()

    return runs.index(cur_run)


def get_source_code(run_number:int) -> str:
    """Build the source code for the relevant run number"""

    args_code = st.session_state.run_history[run_number]['code']
    model = st.session_state.run_history[run_number]['model']

    # add the save output if the model was saved
    if model.model_fullpath is not None:
        # this replace single backslash with double so it ignores the escape charactefrs
        args_code['model_fullpath'] = model.model_fullpath.replace('\\', '\\\\')

    if st.session_state.model_type == 'Regression':
        is_regression = True
    elif st.session_state.model_type == 'Classification':
        is_regression = False
    else:
        is_regression = "'infer'"

    input = f"paml = pardon.Pardon(data='{st.session_state.file.name}', target='{model.target}', test_size={model.test_size}, stratify={model._stratify}, is_regression={is_regression})"
    for item in st.session_state.pre_build_source_code:
        input += f'\n\n{item}'

    arguments = ',\n\t\t'.join([f"{k}={v}" if not isinstance(v, str) else f"{k}='{v}'" for k, v in args_code.items()])
    full_output = f"{input}\n\npaml.rapid_ml({arguments})"

    return full_output


def get_session_state(item_name:str, default=None, options:list=[]):
    """Get the session state for the associated item"""

    # get the value of the item
    value = st.session_state.pardon_keys.get(item_name, default)

    # if options we want to return the index of the value in the list
    if options:
        value = 0 if value not in options else options.index(value)

    return value


def update_state(keys:list):
    """Update the session states of the items provided"""
    for key in keys:
        st.session_state.pardon_keys[key] = getattr(st.session_state, key)


def empty_ml_expanders():
    """Empty the sections in the Rapid ML to be replaced with the updated information"""

    # empty the expanders so they can be rebuilt
    if 'select_model_expander' in st.session_state.keys():
        st.session_state.select_model_expander.empty()
        st.session_state.model_comparison_expander.empty()
        st.session_state.all_test_scores_expander.empty()
        st.session_state.ml_data_flow_expander.empty()
    
    
def build_selected_model():
    """Build the selected model section"""

    run_index = get_current_run_index()
    runs = get_runs()

    st.session_state.select_model_expander = st.expander(f'Rapid ML Selected Model', expanded=False)

    with st.session_state.select_model_expander:
        smr1, _ = st.columns((1, 10))
        with smr1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='sm_run')

        model =  st.session_state.run_history[run_selection]['model']
        selected_model_identifier = model.model_unique_identifier
        selected_score_metric = model.rapid_ml_scores[selected_model_identifier]['score_metric']
        apply_markdown(f"<p>Best Performing Model Type: <b>{model.rapid_ml_scores[selected_model_identifier]['model_type']}</b></p>")
        apply_markdown(f"<p>Model Unique Identifier: <b>{selected_model_identifier}</b></p>")
        apply_markdown(f"<p>Selected Score Metric: <b>{selected_score_metric}</b></p>")
        apply_markdown(f"<p>Model {selected_score_metric} Test Score: <b>{model.rapid_ml_scores[selected_model_identifier]['model_test_scores'][selected_score_metric]}</b></p>")

        st.write(model.rapid_ml_scores[selected_model_identifier])

        save_model = st.button('Save Model', key='selected_model_button_save')
        save_location = default_model_filepath(run_selection)
        save_model_filepath = st.text_input('Select Save location and filename (must be saved as .pkl)', value=save_location, key='model_select_save')

        if save_model:
            if not save_model_filepath:
                st.error('Please specify a valid filepath and try again')
            else:
                model.save_model(model_fullpath=save_model_filepath)
                # display the sucess message
                show_message(text=f'{model.model_type} Model successfully saved to: {save_model_filepath}', seconds=1)


def get_model_chart_data(run_number:int, score_metric:str) -> dict:
    """Get the data required for the chart"""

    # get a dictionary for the chart data
    chart_data = {}

    models = st.session_state.run_history[run_number]['model'].rapid_ml_scores
    first_item = list(models.keys())[0]

    if score_metric not in models[first_item]['model_test_scores'].keys():
        return None

    for model_identifier in models.keys():
        model_type = models[model_identifier]['model_type']
        score = models[model_identifier]['model_test_scores'][score_metric]
        chart_data[model_type] = score

    return chart_data


def current_run_number() -> int:
    """Return the most recent run number"""

    runs = get_runs()
    return max(runs)
    

def build_comparison_chart(run_number:int, score_metric:int):
    """Build the chart that compares ML models"""

    # get the chart data
    chart_data = get_model_chart_data(run_number=run_number, score_metric=score_metric)

    if chart_data is not None:
        chart_data = dict(sorted(chart_data.items(), key=lambda item: item[1], reverse=False))
        # labels and values for the chart
        labels = list(chart_data.keys())
        values = list(chart_data.values())
        # plot
        plt.barh(range(len(chart_data)), values, tick_label=labels)
        plt.title(f'Tested Models {score_metric} scores')
        plt.show()
    else:
        st.error(f'{score_metric} not available the the run: {run_number}')


def get_runs() -> list:
    """Return the list of runs"""

    # if no run has occurred, return 1 in a list as it is the first run
    if not st.session_state.run_history:
        return [1]

    return list(st.session_state.run_history.keys())


def build_model_comparisons():
    """Build the Rapid ML model comparison section"""

    st.session_state.model_comparison_expander = st.expander('Rapid ML Model Comparison', expanded=False)

    runs = get_runs()
    run_index = get_current_run_index()
    score_metrics = get_metrics_models()['score_metrics']

    with st.session_state.model_comparison_expander:
        rn1, rn2, _ = st.columns((0.7, 2, 5))
        with rn1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='bmc_run')
        with rn2:
            chart_score_metric = st.selectbox('Score Metric', score_metrics, key='bmc_run')

        st.session_state.mc_r1col1, _ = st.columns((1, 1))
        with st.session_state.mc_r1col1:
            st.pyplot(build_comparison_chart(run_number=run_selection, score_metric=chart_score_metric))


def build_model_test_scores():
    """Build the Rapid ML model test score section"""

    st.session_state.all_test_scores_expander = st.expander('Rapid ML Test Scores', expanded=False)

    with st.session_state.all_test_scores_expander:
        runs = get_runs()
        cur_run = current_run_number()
        run_index = runs.index(cur_run)
        rn1, _ = st.columns((1, 10))
        rn2, _ = st.columns((10, 1))
        with rn1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='bmt_run')
        with rn2:
            full_scores = get_test_scores_from_dict(test_dict=st.session_state.run_history[run_selection]['model'].rapid_ml_scores)
            st.write(full_scores)


def get_test_scores_from_dict(test_dict:dict) -> dict:
    """Get the test scores from the test dictionary object"""

    out_dict = collections.defaultdict(dict)

    for model_identifier in test_dict:
        out_dict[model_identifier]['model_type'] = test_dict[model_identifier]['model_type']
        out_dict[model_identifier]['model_test_scores'] = test_dict[model_identifier]['model_test_scores']

    return out_dict


def build_model_diagram():
    """Build the Rapid ML flow diagram section"""

    st.session_state.ml_data_flow_expander = st.expander('Rapid ML Data Flow Diagram', expanded=False)
    
    with st.session_state.ml_data_flow_expander:
        runs = get_runs()
        cur_run = current_run_number()
        run_index = runs.index(cur_run)
        mdr1, _ = st.columns((1, 10))
        _, mdr2, _ = st.columns((1, 0.5, 1))

        with mdr1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='md_run')
        with mdr2:
            with st.spinner('Building Data Flow Diagram...'):
                st.pyplot(st.session_state.run_history[run_selection]['model'].model_diagram(fontsize=16))


def build_model_tester():
    """Build the Model Tester"""

    st.session_state.ml_model_test_expander = st.expander('Rapid ML Model Tester', expanded=False)

    with st.session_state.ml_model_test_expander:
        runs = get_runs()
        cur_run = current_run_number()
        run_index = runs.index(cur_run)
        mtr1c1, _ = st.columns((1, 10))

        with mtr1c1:
            run_selection = st.selectbox('Run Number', runs, index=run_index, key='mt_run')

        # get the data from the relevant model
        model = st.session_state.run_history[run_selection]['model']

        if 'data_row' not in st.session_state or st.session_state.mlt_run_num != run_selection:
            st.session_state.data_row = model.get_sample_rows(include_target=True)

        columns = [col for col in model.required_columns() if col != model.target]

        refresh_data = st.button('Refresh input data')
        if refresh_data:
            st.session_state.data_row = model.get_sample_rows(include_target=True)

        data = st.session_state.data_row

        st.session_state.data_input_columns = columns.copy()
    
        while columns:
            col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
            all_cols = [col_1, col_2, col_3, col_4, col_5, col_6]
            for idx in range(len(all_cols)):
                if not columns: break
                with all_cols[idx]:
                    col = columns.pop()
                    setattr(st.session_state, col, st.text_input(col, data.iloc[0][col]))

        br1c1, _ = st.columns((1, 4))
        with br1c1:
            predict_button = st.button('Get Prediction')

        if predict_button:
            data_dict = {col: getattr(st.session_state, col) for col in st.session_state.data_input_columns}
            data = data.to_dict(orient='records')[0]
            data.update(data_dict)
            input_data = pd.DataFrame([data])

            for col in input_data.columns:
                if input_data[col].dtype != st.session_state.data_row[col].dtype:
                    # try and convert to the applicable type if possible
                    try:
                        input_data[col] = input_data[col].astype(st.session_state.data_row[col].dtype)
                    except:
                        pass

            prediction = model.predict(data=input_data)
            apply_markdown(f'<p>{model.target} Prediction: <b>{prediction.predicted[0]}</b></p>')
            if prediction.probabilities:
                apply_markdown(f'<p>{model.target} Probabilities: <b>{prediction.probabilities[0]}</b></p>')

        st.session_state.mlt_run_num = run_selection

def build_dt_diagram():
    """Build the Data Transformation flow diagram section"""

    if dt_model_available():
        st.session_state.dt_data_flow_expander = st.expander('Data Transformation Data Flow Diagram', expanded=False)
        
        with st.session_state.dt_data_flow_expander:
            _, st.session_state.dflow_r1col2, _ = st.columns((1, 0.5, 1))
            with st.session_state.dflow_r1col2:
                with st.spinner('Building Data Flow Diagram...'):
                    st.pyplot(st.session_state.dt_model.model_diagram(fontsize=16))


def build_chart(ml_model:pardon.Pardon=None):
    '''Build the chart'''
    # set the data we are using
    with st.spinner('Building Chart...'):
        with st.session_state.d_vis_r4col1:
            try:
                st.pyplot(create_visualisation(ml_model=ml_model))
            except ValueError as err:
                st.error(f'''There has been an error rendering the chart. Check your chart inputs are transformed and valid, and try again.
                             Error encountered: {err}''')


def chart_selected_columns() -> list:
    """Return the columns that have been used in the build chart"""

    # return the values from the possible columns
    
    return [st.session_state.x, st.session_state.y, st.session_state.c,st.session_state.size]


def create_visualisation(ml_model:pardon.Pardon=None):
    """Create the visualisations"""
    # create the visualisations to be rendered into a pyplot widget
    apply_transformations = False
    if st.session_state.use_data_source == 'Transformed Data':
        # apply_transformations = False
        if ml_model is not None and f'{ml_model.target}{pardon.pardon_options.PREDICTED_COL_SUFFFIX}' in chart_selected_columns():
            data = ml_model.data.copy()
        else:
            data = st.session_state.dt_model.data.copy()
    else:
        # apply_transformations = True if st.session_state.chart_type.lower() not in ('correlation', 'histogram') else False
        data = st.session_state.raw_data.copy()

    # if there is no classes option, we do not care what the classes are so just set to any text value
    classes = None if not isinstance(st.session_state.ml_model, pardon.Pardon) else st.session_state.ml_model.classes()

    trendline = st.session_state.include_trendline if 'include_trendline' in st.session_state else True

    # this is done this way so we can cache the output
    if isinstance(ml_model, pardon.Pardon):
        return ml_model.plot_data(data=data, x=st.session_state.x, y=st.session_state.y, c=st.session_state.c, size=st.session_state.size, n_predictions='all', include_trendline=trendline, show_as=st.session_state.chart_type, as_prediction=False, n_bins='auto', lineplot_estimator=st.session_state.estimator, apply_transformations=apply_transformations)
    elif st.session_state.chart_type.lower() == 'scatterplot':
        return pardon.visuals._plot_scatter(data=data, x=st.session_state.x, y=st.session_state.y, c=st.session_state.c, size=st.session_state.size, target=st.session_state.chart_target, classes=classes, include_trendline=trendline, as_prediction=False, randomised_data=None, randomised_data_title=None)
    elif st.session_state.chart_type.lower() == 'histogram':
        return pardon.visuals._plot_hist(data=data, x=st.session_state.x, n_bins='auto', as_prediction=False, target=st.session_state.chart_target)
    elif st.session_state.chart_type.lower() == 'correlation':
        return pardon.visuals.plot_corr(data=data, columns=list(data.columns))
    elif st.session_state.chart_type.lower() == 'lineplot':
        return pardon.visuals._plot_lineplot(data=data, x=st.session_state.x, y=st.session_state.y, c=st.session_state.c, size=st.session_state.size, target=st.session_state.chart_target, as_prediction=False, lineplot_estimator=st.session_state.estimator)


def build_data_visualisations():
    """Build the data visualisations section"""
    
    # set default estimator
    st.session_state.estimator = 'mean'
    st.session_state.data_visualisations_expander = st.expander('Create Data Visualisations', expanded=True)

    with st.session_state.data_visualisations_expander:
        st.session_state.d_vis_r1col1, st.session_state.d_vis_r1col2, st.session_state.d_vis_r1col3, st.session_state.d_vis_r1col4 = st.columns(4)
        st.session_state.d_vis_r2col1, st.session_state.d_vis_r2col2, st.session_state.d_vis_r2col3, st.session_state.d_vis_r2col4 = st.columns(4)
        st.session_state.d_vis_r3col1, st.session_state.d_vis_r3col2, _, _, = st.columns((0.5, 0.7, 1, 1))
        st.session_state.d_vis_r4col1, _ = st.columns((0.8, 1))

        with st.session_state.d_vis_r1col1:
            # if the user has not performed transformations, only allow raw data
            data_sources =  ['Raw Data', 'Transformed Data'] if dt_model_available() else ['Raw Data']
            st.session_state.use_data_source = st.selectbox(f'Use Data', data_sources, help='Raw data is that directly from the file, transformed is the data after any transformations have been applied.')
            # set the data columns
            data_columns = list(st.session_state.dt_model.data.columns) if st.session_state.use_data_source == 'Transformed Data' else list(st.session_state.raw_data.columns) 
            
        # update the columns to include the predicted elements if not using correlation
        if ml_model_available():
            st.session_state.chart_target = st.session_state.ml_model.target
            # we do not want users to use predicted columns when using transformed data as it looks strange and may cause confusion
            if st.session_state.use_data_source == 'Raw Data':
                targ_index = data_columns.index(st.session_state.chart_target) + 1
                predict_targ = f'{st.session_state.ml_model.target}{pardon.pardon_options.PREDICTED_COL_SUFFFIX}'
                data_columns.insert(targ_index, predict_targ)
        else:
            # just set the last item as the target if no actual target
            st.session_state.chart_target = data_columns[-1]

        with st.session_state.d_vis_r1col2:
            if not ml_model_available():
                runs = ['N/A']
                run_index = 0
            else:
                runs = get_runs()
                run_index = get_current_run_index()

            with st.session_state.d_vis_r1col2:
                run_selection = st.selectbox('Predictions from Run Model', runs, index=run_index, key='ml_model_d_run')
                ml_model = None if run_selection == 'N/A' else st.session_state.run_history[run_selection]['model']

        with st.session_state.d_vis_r1col3:
            st.session_state.chart_type = st.selectbox(f'Chart type', ['Scatterplot', 'Histogram', 'Correlation', 'Lineplot'], help='Select the Chart type')

        if st.session_state.chart_type.lower() == 'lineplot':
            with st.session_state.d_vis_r1col4:
                opt = list(pardon.visuals._LINEPLOT_ESTIMATORS.keys())
                st.session_state.estimator = st.selectbox(f'Lineplot Estimator', opt, help='When using a lineplot chart, specify the type of aggregation to perform on the y axis. For text columns, this will automatically be set to "count". When using z_score, the max z_score for each data point will be used.')

        # correlation gets no input
        if st.session_state.chart_type.lower() != 'correlation':
            with st.session_state.d_vis_r2col1:
                st.session_state.x = st.selectbox(f'x-axis column', data_columns, help='The column for the x axis')

            # only show these options when not a histogram
            if st.session_state.chart_type.lower()!= 'histogram':
                with st.session_state.d_vis_r2col2:
                    st.session_state.y = st.selectbox(f'y-axis column', data_columns, help='The column for the y axis', index=data_columns.index(st.session_state.chart_target))

                with st.session_state.d_vis_r2col3:
                    st.session_state.c = st.selectbox(f'Colour column', [None] + data_columns, help='The column determining marker colour')

                with st.session_state.d_vis_r2col4:
                    st.session_state.size = st.selectbox(f'Size column', [None] + data_columns, help='The column determining marker size')

        with st.session_state.d_vis_r3col1:
            st.session_state.build_chart = st.button('Build Chart')

            if st.session_state.chart_type.lower() == 'scatterplot':
                with st.session_state.d_vis_r3col2:
                    st.session_state.include_trendline = st.checkbox('Include Trendline', value=True)

            if st.session_state.build_chart:
                build_chart(ml_model=ml_model)


def ml_model_available(ml_model=None) -> bool:
    '''See if the ML model is available'''

    ml_model = st.session_state.ml_model if ml_model is None else ml_model

    if isinstance(ml_model, pardon.Pardon) and ml_model.model is not None:
        return True

    return False


def dt_model_available() -> bool:
    """See if the data transformation model is available"""

    if isinstance(st.session_state.dt_model, pardon.Pardon):
        return True
    
    return False
 

def build_main_form():
    '''Build the main form and create the file uploader'''
    st.session_state.main_form_col, _, _ = st.columns(3)
    if st.session_state.file is None:
        with st.session_state.main_form_col:
            build_file_uploader()
      
        
def build_sidebar():
    """Build the sidebar"""
    st.session_state.sidebar = st.sidebar

    with st.session_state.sidebar:
        st.session_state.new_file_button = st.button('Load New File')
        apply_markdown(markdown=statics.HORIZONTAL_LINE_MARDOWN)
        apply_markdown(markdown=text_markdown(text=st.session_state.file.name, textsize=22))
        # get the file information
        assign_file_info()
        # this sets the title at top of page
        set_file_details()
        

def build_content():
    """Build the site content"""

    # this builds the main column structure, and gets the original upload file
    build_main_form()

    if st.session_state.file:
        # add the side bar
        build_sidebar()
        # build the tabs
        st.session_state.tab1, st.session_state.tab2, st.session_state.tab3, st.session_state.tab4  = st.tabs(['Raw Data', 'Transform Data', 'Machine Learning', 'Data Visualisations'])

        with st.session_state.tab1:
            build_data_preview()
        with st.session_state.tab2:
            build_data_transform()
        with st.session_state.tab3:
            if dt_model_available():
                build_ml_section()
            else:
                # this displays that the data has not been transformed, and gives the user the option to ignore
                transforms_not_required()
        with st.session_state.tab4:
            build_data_visualisations()


def transforms_not_required():
    """Create the data transformation not required message and button"""
    # this is used when the user has not done any data transformation and selected the machine learning section
    # they can confirm that no transformations are required with a button
    # we create a placeholder to attach the button and error so we can then clear them
    err = st.error('Please first use the Data Transformations to prepare your data for Machine Learning and try again. Alternatively, confirm data transformations are not required below.')
    placeholder = st.empty()
    with placeholder:
        transform_not_needed = st.button('Transformations not required')
    # we can clear the message
    if transform_not_needed:
        placeholder.empty()
        err.empty()
        st.session_state.dt_model = pardon.Pardon(data=st.session_state.raw_data.copy(), target=None)
        # we set an empty buildkwargs because we did not do any transforms
        st.session_state.build_kwargs = {}
        build_ml_section()


def build_ml_section():
    """Build the machine learning sections"""

    build_rapid_ml()

    if ml_model_available():
        build_rapid_ml_output()


def build_app():
    """Build the application"""
    set_page_configuration()
    set_logo()
    set_session_states()
    build_content()


if __name__ == '__main__':
    build_app()
