import os, sys
import json
import re
import varname

import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
from scipy import stats
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.model_selection import RepeatedStratifiedKFold, RepeatedKFold
from streamlit.uploaded_file_manager import UploadedFile
import numpy as np

from . import formats
from . import pardon
from . import pickles

pd.options.mode.chained_assignment = None


class _InvalidFunction:
        """ Internal class to catch invalid function calls"""
        def __init__(self, function):
            self.function = function


class InvalidModel:
        """
        Launch an API on the local host to test the output of your saved Pardon model.

        Args:
            model : class
                The model object that has failed or is invalid.
            model_type : str
                The type of model object that has failed or is invalid
            error : str
                The error that was encountered when training the model.
        """
        def __init__(self, model, error):
            self.model = model
            self.model_type = type(model).__name__
            self.error = error
        
        def __str__(self):

            output = f'{self.model_type}: {self.error}'

            return output


def data_reader(data, encoding='latin-1', sep=',', error_bad_lines=None) -> pd.DataFrame:
    """
    Function to load a file or non-Pandas DataFrame object into a Pandas DataFrame.

        Args:
            data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                The data source. Can be a file path or an object.
            encoding : str, default 'latin-1' {'latin-1' , 'ascii', 'utf-8'}
                The encoding used when opening csv or xml files.
            sep : str, default ','
                The delimiter to use when opening csv or txt files.
            error_bad_lines : bool, default None
                Raise an error if bad lines with too many or too few delimiters are found. If False, bad lines will be dropped.

        Returns:
            (pandas.DataFrame) : Returns a pandas.DataFrame object of the input data.
    """
    # read a file or object into a dataframe
    # if the data is already a dataframe, return it but as a copy so we do not overwrite the original
    if isinstance(data, pd.DataFrame):
        return data.copy()

    # if we are using streamlit, open with read csv
    if isinstance(data, UploadedFile):
        # ensure the file has not previously been read
        data.seek(0)
        data = pd.read_csv(data, encoding=encoding)
        return data

    # if the data is none, return an error
    if data is None:
        raise ValueError('The data is None, please check your data source and try again.')
    # if a filename has been passed
    if isinstance(data, str):
        # if a full stop and extension is valid
        if looks_like_file(string_object=data):
            # get file and extension
            _, ext = os.path.splitext(data)
            
            # if no extension, raise an error
            if ext is None or not ext or ext not in formats.VALID_FILE_FORMATS:
                raise FileNotFoundError(f'The file {data} is invalid. Please ensure you include the whole filepath and filename and try again. Note: valid formats are: {formats.VALID_FILE_FORMATS}')

                # check the data exists
            if not os.path.exists(data):
                raise FileNotFoundError(f'The file {data} cannot be found, ensure the correct path is specified and try again.')

            # read the file into a dataframe
            if ext == '.csv' or ext == '.txt':
                data = pd.read_csv(data, encoding=encoding, low_memory=False, sep=sep, error_bad_lines=error_bad_lines)
            elif ext == '.parquet':
                data = pd.read_parquet(data, engine='fastparquet')
            elif ext == '.json':
                # open the data file
                with open(data, 'r') as json_file:
                    # load the data into json
                    data = json.load(json_file)
                    # take the data string into a dataframe
                    data = pd.DataFrame(data, index=[0])
            elif ext == '.xml':
                data = pd.read_xml(data, encoding=encoding)
            elif ext in ('.xls', '.xlsx', '.xlsm'):
                data = pd.read_excel(data, engine='openpyxl')
            else:
                raise ValueError(f'There is an error reading the input file {data}, please check the file and try again.')
        else:
            # if looks like a json, load it into json format
            data = json.loads(data)
            # turn json dict object into pandas dataframe
            data = pd.DataFrame(data, index=[0])
    # if the data is in dictionary format
    elif isinstance(data, dict):
        data = pd.DataFrame(data, index=[0])
    # getting data from structured array
    elif isinstance(data, (list, np.ndarray)):
        data = pd.DataFrame.from_records(data) 
    else:
        # raise an error if the type is not expected
        raise ValueError(f'The data supplied is in an invalid format, please use filetypes: {formats.VALID_FILE_FORMATS}, or dict, list, or arrays and try again.')

    return data.copy()


def load_model(model_fullpath:str):
    """
    Function to load a previously saved pardon.Pardon class.

        Args:
            model_fullpath : str
                The full path to your pardon.Pardon pkl file.

        Returns:
            (pardon.Pardon) : Returns the loaded pardon.Pardon class object.
    """
    model = pickles.load_pickle(model_fullpath)

    # check that the model is an Pardon model
    if not isinstance(model, pardon.Pardon):
        raise TypeError(f'The model specified is not a valid {pardon.Pardon.__name__} object. Check your model file and try again.')

    # return the model
    return model


def proportions(data:pd.Series, as_pct:bool=True, include_all:bool=False) -> dict:
    """
    Function to get the proportions of items in a pandas.Series or single column pandas.DataFrame.

        Args:
            data : pandas.Series, pandas.DataFrame
                The data to get the class proportions.
            as_pct : bool, default True
                Return the proportion percentages in the output.
            include_all : bool, default False
                Return both the count and proportion percentages in the output. Percentages will be shown rounded to 2 decmial places between 0 and 100.

        Returns:
            (dict) : Returns a dictionary containing the proportions for each class in the data.
    """
    # get the proportion of items
    data = data.copy()

    # if it is a series, change to data frame
    if isinstance(data, pd.DataFrame):
        data = data.to_series()

    # get the value counts
    props = data.value_counts().to_dict()
    
    # if pct turn every value into its pct
    if as_pct or include_all:
        totals = sum(props.values())
        # if include all, include the counts too
        props = {k: f'{v} ({round((v / totals) * 100, 2)}%)' for k, v in props.items()} if include_all else {k: v / totals for k, v in props.items()}

    return props


def get_mode(array):
    """
    Function to get the mode average from a given set of data. If multiple modes are found, the fist encountered will be returned.

        Args:
            array : pandas.Series, pandas.DataFrame, list, numpy.array
                The data to get the mode average.

        Returns:
            (str, int, float) : Returns the mode average found in the data.
    """
    if isinstance(array, pd.DataFrame):
        array = array.to_series()
    # gets values and counts
    vals, counts = np.unique(array, return_counts=True)
    # get the index of highest
    index = np.argmax(counts)
    # return that value
    return vals[index]


def get_z_score(array, max:bool=True):
    """
    Function to get the min or max z score from a given set of data.

        Args:
            array : pandas.Series, pandas.DataFrame, list, numpy.array
                The data to get the z score.
            max : bool, default True
                If True return the maximum z score, else return the minimum z score.

        Returns:
            (int, float) : Returns the min or max z score from the data.
    """
    # convert to series
    if isinstance(array, pd.DataFrame):
        array = array.to_series()

    # get the z scores for the array
    z_scores = np.abs(stats.zscore(array))
    # get the max or min so it returns a single value
    z_scores = np.max(z_scores) if max else np.min(z_scores)

    return z_scores


def looks_like_file(string_object:str) -> bool:
    """
    Function to determine if a string object is likely a filename or not.

        Args:
            string_object : str
                The string to check for a filename.

        Returns:
            (bool) : Returns True if the string_object looks like a filename and False if not.
    """
    # check to see if a string looks like a filename or not

    # if invalid characters, probably not a file
    invalids = ['[', ']', '{', '}']

    # check for invalid characters
    for charac in invalids:
        if charac in string_object:
            return False

    # attempt to get extension
    # get file and extension
    _, ext = os.path.splitext(string_object)

    if ext in formats.VALID_FILE_FORMATS:
        return True

    # if the format seems wrong, return false
    return False


def _check_save_parameters(fullpath:str, filetype:str=None, suppress_error:bool=False) -> str:
    """Internal function to check if save parameters are correct, and add working directory if not directory specified"""
    # get the directory from the fullpath
    dir_name = os.path.dirname(fullpath)

    # if the directory starts with a . the user will mean current working directory
    if dir_name.startswith('.'):
        # get the working dir
        cwd = os.getcwd()
        # replace the first . with the working dir
        dir_name = dir_name.replace('.', cwd, 1)
    
    # if no dir_name, set the current working directory
    if not dir_name:
        # get the working dir
        dir_name = os.getcwd()
        # create the fullpath with directory name
        fullpath = os.path.join(dir_name, fullpath)
    
    # if the dir name is empty or doesnt exist raise an error
    if not os.path.exists(dir_name) and not suppress_error:
        raise FileNotFoundError(f'The folder {dir_name} does not exist, please specify a valid fullpath and try again.')
    
    # if we are checking a file type, endsure the type is correct
    if filetype is not None:
        # get items into a list
        filetype = single_to_list(filetype)
        # loop through the file types and get true if oner is valid
        valids = [True if fullpath.endswith(ft) else False for ft in filetype]
        # if none are valid, raise an error unless supressed
        if True not in valids and not suppress_error:
            raise TypeError(f'Please specify a file name of type {filetype}, the name {os.path.basename(fullpath)} is not valid.')
    
    return fullpath


def remove_non_ascii(string:str) -> str:
    """
    Function to remove non-ascii characters from a string.

        Args:
            string : str
                The string to remove non-ascii characters from.

        Returns:
            (str) : Returns a string with non-ascii characters removed.
    """
    string = string.encode('ascii', 'ignore')

    return string.decode()


def extract_postcode(string:str, type:str='uk', return_empty:bool=False) -> str:
    """
    Function to extract a UK postcode or US zip code from a string. If found, a formatted postcode will be returned.
        
        Args:
            string : str
                The string to extract the postcode from.
            type : str, default 'uk' {'uk', 'us'}
                The type of postcode to extract. This can be “uk” for a UK postcode, or “us” for a US zip code.
            return_empty : bool, default False
                If True, when a match is not found, an empty string will be returned. If False, the original string will be returned.

        Returns:
            (str) : Returns a string containing the extracted postcode.
    """
    # ensure type
    if not isinstance(type, str):
        return ValueError(f'type must be a string containing "uk" or "us" determining the type of postcode to search.')

    # ensure only uk or us
    if type.lower() not in ('uk', 'us'):
        raise ValueError(f'Only "uk" or "us" can be specified for type. Change {type} to one of these values and try again.')
    
    if type.lower() == 'uk':
        # compile uk postcode regex into named group, front_match being the part of uk post, back_match being the back
        regex = re.compile(r'(?P<FRONT>([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?)))))\s*(?P<BACK>[0-9][A-Za-z]{1,2}))')
    else:
        regex = re.compile(r'.*(\d{5}(\-\d{4})?)')

    # check uk first
    matches = regex.search(string)

    # if a match is found, return formatted front and back
    if matches is not None:
        # check uk
        if type.lower() == 'uk':
            # get the 2 groups from the regex
            front = matches.groups()[0]
            back = matches.groups()[-1]
            # if both items were matched
            if front is not None and back is not None:
                front = front.upper().strip()
                back = back.upper().strip()
                # ensure no overlap - this can happen because of the regex, meaning the front can contain the back part
                front = front.replace(back, '').strip()
                # create the formatted output
                output = f'{front} {back}'.upper().strip()
                
                return output
        else:
            # get the match
            output = matches.groups()[0]
            # if a match was found
            if output is not None:
                return str(output).strip()

    # return an empty string if the users specifies
    if return_empty:
        return ''

    return string


def remove_characters(string:str, remove_chars:str, is_regex:bool=False) -> str:
    """
    Function to remove specified characters from a string, by passing the characters to remove, or a regular expression.

        Args:
            string : str
                The string to remove characters from.
            remove_chars : str, list
                The character or list of characters, or regex or list of regexes to remove or apply to the string.
            is_regex : bool, default False
                If supply regex to the remove_chars argument, set this flag to true to have the regex applied to the string. If False, a simple find and replace will occur.

        Returns:
            (str) : Returns a string with the specified characters removed.
    """
    # return string if not a valid object
    if not isinstance(string, str):
        return string

    # make sure we are dealing with a list
    remove_chars = single_to_list(remove_chars)

    if not is_regex:
        # remove the characters from the string
        for char in remove_chars:
            string = string.replace(char, '')
    else:
        # apply the regex
        for char in remove_chars:
            # attempt to apply the regex
            try:
                string = re.sub(char, '', string)
            except re.error:
                raise ValueError(f'The regex: "{char}" is invalid. Check your regex and try again.')

    return string


def create_intervals(start, end, interval) -> list:
    """
    Function to create a list of numbers for a specified interval.

        Args:
            start : int, float
                The first number to start your interval from.
            end : int, float
                The number to end your interval on.
            interval : int, float
                The size of the interval between each item in the list.

        Returns:
            (list) : Returns a list containing the interval values, increasing by the interval specified.
    """
    # ensure all items are integers or floats
    for item in (start, end, interval):
        if not isinstance(item, (int, float)):
            raise ValueError(f'start, end, and interval arguments must all be integers of floats.')

    # create intervals
    output = []
    current = start
    while current <= end:
        output.append(current)
        current += interval

    return output


def create_interval_labels(intervals:list) -> list:
    """
    Function to create a list of string labels for your specified interval list.

        Args:
            intervals : list
                Your interval list.
        
        Returns:
            (list) : Returns a list of string labels for each value in the interval list.
    """
    # ensure the intervals is a list
    if not isinstance(intervals, list):
        raise ValueError('The intervals argument must be a list.')

    output = []
    # we do not want to go to the last item so we say -2 
    # labels have to be 1 less than the number of intervals, and the last label is generated with a + symbol
    max_i = len(intervals) - 2
    # check if we need to round
    round_vals = False if isinstance(intervals, float) else True

    # create the labels in range
    for i, _ in enumerate(intervals[:-1]):
        min_val = intervals[i]
        if i < max_i:
            max_val = intervals[i+1]
            # create andf add the labels
            label = f'{round(min_val)}-{round(max_val)}' if round_vals else f'{min_val}-{max_val}'
            output.append(label)
        else:
            # when done, on the final value use the value and +
            output.append(f'{round(min_val)}+' if round_vals else f'{min_val}+')

    return output


def get_sentiment(text:str, return_as:str='text') -> str:
    """
    Apply sentiment analysis to the text specified using the nltk library.

        Args:
            text : str
                The text to apply the sentiment analysis to.
            return_as: str, dict, default 'text'
                Define the output of your sentiment analysis. If 'text', each string will have a sentiment analysis determined to be 'positive', 'neutral', or 'negative'. You can supply a dictionary object outlining what value to return for each sentiment type. For example, return_as=dict('positive'=3, 'neutral'=2, 'negative'=1).
    
        Returns:
            (str) : Returns a string with the assessed sentiment of the text supplied.
    """
    # return the sentiment of the text
    # set the dict object containing outputs
    SENTIMENTS = {'neg': 'negative', 'neu': 'neutral', 'pos': 'positive'}

    # force text into a string format
    if not isinstance(text, str):
        text = str(text)

    if isinstance(return_as, dict):
        # set all the keys to lower case
        return_as = {str(k).lower(): v for k, v in return_as.items()}
        # get full words
        full_words = ('negative', 'neutral', 'positive')
        # check all full words are in keys
        for word in full_words:
            if word not in return_as:
                raise KeyError(f'The word: {word} is not found in your return_as dictionary. Please use positive, neutral, and negative and try again. For example: return_as=dict(positive=3, neutral=2, negative=1)')

    # initalise the class
    sia = SentimentIntensityAnalyzer()
    # score the text
    sent = sia.polarity_scores(text)
    # pop the compound score
    sent.pop('compound')
    # get the highest score for the sentiment
    sentiment = max(sent, key=sent.get)
    # get the full word
    sentiment = SENTIMENTS[sentiment]
    # if the user specified their own values, get them
    if isinstance(return_as, dict):
        sentiment = return_as[sentiment]

    return sentiment


def to_json(object_to_json) -> str:
    """
    Convert the object to json format.

        Args:
            object_to_json : Any
                The object to convert to json. pandas.DataFrame and pandas.Series will be converted using internal methods.
   
        Returns:
            (str) : Returns a string with the object converted to json format.
    """
    # if using dataframe or series, use the pandas convert
    if isinstance(object_to_json, pd.DataFrame) or isinstance(object_to_json, pd.Series):
        # create a copy so to not overwrite the original
        pdobject = object_to_json.copy()
        # reset the index is necessary
        pdobject = pdobject.reset_index(drop=True)
        # both series and dataframes have the to_json method
        object_to_json = pdobject.to_json(orient='records')
    else:
        # dump the object to a json format and load
        object_to_json = json.dumps(object_to_json)

    return object_to_json


def single_to_list(item) -> list:
    """
    Converts an item to a list if not already a list.

        Args:
            item : any
                The item to change to a list if not already a list.

        Returns:
            (list) : Returns the item as a single item list if not already a list, else returns the item as is.
    """
    # if the item is not already a list, turn it into a single item list
    item = [item]  if not isinstance(item, list) else item
        
    return item


def assert_item_type(item, item_types:list):
    """
    Checks if an item is a particular type, and raises a helpful error specifying the valid type if not.

        Args:
            item : Any
                The variable to check for the valid item types.
            item_types : list
                A list containing the valid item types.

    """    
    # ensure item types is a list
    item_types = single_to_list(item=item_types)
    # ensure all the items in item_types have been instantiated
    item_types = [x() if callable(x) else x for x in item_types]

    # iterate through, if the item is any of the valid items, we can return and ignore any errors
    for i in item_types:
        if isinstance(item, type(i)):
            return
    # if we are here, the item is invalid, raise an error and declare the valid types
    valid_types = ', '.join([type(x).__name__ for x in item_types])   

    raise TypeError(f"The {varname.argname('item')} argument must be of types: {valid_types}, not: {type(item)}")


def get_data_averages(data:pd.Series) -> dict:
    """
    Returns a dictionary object with the data averages and standard deviation.

        Args:
            data : pandas.Series
                The data to get averages from.

        Returns:
            (dict) : Returns a dict object containing the averages and std for the data.

    """
    if isinstance(data, pd.DataFrame):
        data = data.to_series()
     # if regression model, get the averages
    mean = np.mean(data)
    median = np.median(data)
    mode = get_mode(array=data)
    std = np.std(data)
    averages = {'mean': mean, 'median': median, 'mode': mode, 'std': std}

    return averages


def list2_differences(list1:list, list2:list) -> list:
    """
    Returns a list of items in list2 that are not in list1.

        Args:
            list1 : list
                The list with the assumed correct items to check for in list2.
            list2 : list
                The list to check for items not in list1.

        Returns:
            (list) : Returns a list containing items in list2 that are not in list1.

    """
    differences = list(set(list2) - set(list1))

    return differences


def list_differences(list1:list, list2:list) -> list:
    """
    Returns a list of items that are in either list but not the other.

        Args:
            list1 : list
                First list for comparison.
            list2 : list
                Second list for comparison.

        Returns:
            (list) : Returns a list containing items that are in either list but not the other.

    """
    differences1 = list(set(list2) - set(list1))
    differences2 = list(set(list1) - set(list2))

    all_differences = list(set(differences1 + differences2))

    return all_differences


def get_labels(data:pd.Series) -> dict:
    """
    Returns a dictionary of numeric labels for each value in a pandas.Series.

        Args:
            data : pandas.Series
                The data to get numeric labels.

        Returns:
            (dict, None) : Returns a dictionary object with a numeric label for each unique value in the data. Returns None if the data is already numeric.

    """
    # if numeric, return none as not required
    if is_numeric_dtype(data):
        return None

    # get unique values, sorted
    unique = data.unique()
    # ensure every item is a string and sort
    unique = sorted([str(x) for x in unique])
    # get a number for each label starting from 1
    labels_dict = {x: i for i, x in enumerate(unique)}

    return labels_dict


def map_col_labels(data:pd.DataFrame, column:str, labels:dict) -> pd.DataFrame:
    """
    Returns a dictionary of numeric labels for each value in a pandas.Series.

        Args:
            data : pandas.DataFrame
                The data to get numeric labels.
            column : 
                The name of the column to map the numeric labels to.
            labels : dict
                The dictionary object containing each unique value in the data column and a corresponding numeric label.
        Returns:
            (pd.DataFrame) : Returns a pandas.DataFrame of the data mapped to the new labels.

    """
    # copy the data
    data = data.copy()
    # map the labels to the data
    data[column] = data[column].map(labels) if labels is not None else data[column] 

    return data


def get_cv_object(n_splits:int=10, n_repeats:int=3, regression:bool=False, stratify:bool=True, random_state:int=13) -> object:
    """
    Returns a cross-validator object. RepeatedStratifiedKFold or RepeatedKFold.

        Args:
            n_splits : int, default 10
                The number of splits.
            n_repeats : int, default 3
                The number of times to repeat the cross-validator.
            regression : bool, default False
                If this is for use with a regression model.
            stratify : bool, default True
                If you wish to stratify your folds with the cross-validator.
            random_state : int, default 13
                Controls the randomness of each repeated cross-validation instance.
        Returns:
            (sklearn.model_selection.RepeatedStratifiedKFold or sklearn.model_selection.RepeatedKFold) : Returns a cross-validator object.

    """
    # get the cross validation object relevant to the model
    kf = RepeatedStratifiedKFold if not regression and stratify else RepeatedKFold
    # create the object
    cv = kf(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)

    return cv


def all_numeric(data_list:list) -> bool:
    """
    Returns a boolean if the list contains all numeric items.

        Args:
            data_list : list
                The list to check for all numeric.

        Returns:
            (boolean) : True if all items in the list are numeric else False.

    """
    # return true if all items are numeric else false
    return all([True if (isinstance(x, (int, float) or is_numeric_dtype(x))) or str(x).isnumeric() else False for x in data_list])


def normal_dist_in_range(mean, sd, min, max):
    """
    Returns a value within a normal distribution, within the bounds of the min and max values found in the dataset.
    If the value generated is above the max it will be set to the max. If the value generated is below the min it will be set to the min.

        Args:
            mean : float, int
                The mean found in your distribution.
            sd : float, int
                The standard deviation found in your distribution.
            min : float, int
                The minimum value found in your distribution.
            max : float, int
                The maximum value found in your distribution.

        Returns:
            (int, float) : Returns a numeric value within a normal distribution within the bounds of the min and max value.

    """
    # get a normal distribution value
    rand = np.random.normal(mean, sd)
    # if it is below or above the min or max, replace the values
    if rand <  min:
        rand = min
    elif rand > max:
        rand = max

    return rand


def merge_dictionaries(dict1:dict, dict2:dict) -> dict:
    """
    Merge 2 dictionaries into a single dictionary object. For keys in both dictionaries, those in dict1 will be kept.

        Args:
            dict1 : dict
                The first dictionary object.
            dict2 : dict
                The second dictionary object.

        Returns:
            (dict) : Returns a dictionary object containing both dictionary keys.

    """
    output = dict2.copy()
    output.update(dict1)

    return output


def _check_if_regression(data, target:str) -> bool:
    """Determine if the model will be for a regression task by checking the target"""

    if target not in data.columns:
        return False

    # if not numeric, not regression
    if not is_numeric_dtype(data[target]):
        return False

    # if there are only 2 unique values, possible we are looking at a binary classification task
    if len(data[target].unique()) == 2:
        return False
    # if numeric and more than 2 unique items, assume it's regression
    return True


def flatten_list(list_item:list, ignore_items:list=None, apply_to_items:list=None, deduplicate:bool=False) -> list:
    """
    Function to turn a list of lists into a single list.
        
        Args:
            list_item : list
                The list containing further lists.
            ignore_items : any, list, default None
                A single item or list of items to ignore when adding to your new list.
            apply_to_items : func, list, default None
                A single function or list of functions to apply to the items being kept in your list. If not callable, will not be applied.
            deduplicate: bool, default False
                Return a deduplicated list. Note, this is case sensitive.
            
        Returns:
            (list) : Returns a single list containing selected items.
    """
    # the flatten function is a recursive function to get all items from n number of lists
    output_list = __flatten(list_item, flat_list=[], ignore_items=ignore_items, apply_to_items=apply_to_items)

    if deduplicate:
        output_list = list(set(output_list))

    return output_list


def __flatten(current_list, flat_list=[], ignore_items=None, apply_to_items=None):

    # set lambda func
    current_list = np.array(current_list, dtype='object')
    check_func = lambda x: np.ndim(x) != 0

    not_ignore_flag = ignore_items is not None
    apply_to_items_flag = apply_to_items is not None
    # ensure all items are lists
    if not_ignore_flag:
        ignore_items = single_to_list(ignore_items)
    if apply_to_items_flag:
        apply_to_items = single_to_list(apply_to_items)
    # reduce any number of list of lists into a single list
    if check_func(current_list):
        for item in current_list:
            if check_func(item):
                __flatten(current_list=item, flat_list=flat_list, ignore_items=ignore_items, apply_to_items=apply_to_items)
            else:
                if not_ignore_flag:
                    # if the item is in the ignore list, skip to next
                    if item in ignore_items: continue
                if apply_to_items_flag:
                    for func in apply_to_items:
                        # only try if callable
                        if callable(func):
                            item = func(item)
                flat_list.append(item)
    else:
        if not not_ignore_flag or (ignore_items is not None and current_list not in ignore_items):
            flat_list.append(current_list)
    return flat_list


def columns_with_nulls(data):
    """
    Return a list of columns that contain null values.

        Args:
            data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                The data to check for columns with null values.

        Returns:
            (list) : Returns a list of strings with the column names that contain null values.
    """
    data = data_reader(data=data)

    return data.columns[data.isna().any()].tolist()


def numeric_columns(data) -> list:
    """
    Return a list of columns that have a numeric data type.

        Args:
            data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame, default None
                The data to check for columns with for numeric data types. If no data is specified, the training data will be used.

        Returns:
            (list) : Returns a list of strings with the column names that have a numeric data type.
    """
    # use training data if a dataframe is not provided
    data = data_reader(data=data)
    # get the valid columns
    return data.select_dtypes(include='number').columns.tolist()


def is_array(obj) -> bool:
    """
    Returns True if the object is an array object such as a list or an numpy array else False.

        Args:
            obj : any
                The object to check.

        Returns:
            (bool) : Returns True if the object is an array object else False.
    """
    return np.ndim(obj) != 0


def sort_dictionary(dict_object:dict, desc:bool=True) -> dict:
    """
    Sorts a dictionary object by its values.
        
        Args:
            dict_object : dict
                The dict to be sorted.
            desc : bool, default True
                Sort descending.

        Returns:
            (dict) : Returns the dict sorted.

    """
    assert_item_type(item=dict_object, item_types=[dict])
    assert_item_type(item=desc, item_types=[bool])

    output = dict(sorted(dict_object.items(), key=lambda item: item[1], reverse=desc))

    return output