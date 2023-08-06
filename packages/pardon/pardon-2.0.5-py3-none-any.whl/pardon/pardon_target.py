from collections import deque
from operator import index
import sys

import pandas as pd

from . import utility
from . import statics


class Target:
    """
    A class defining the target object ready for machine learning.
        Args:
            data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data source. Can be a filepath or an object.
            target : str
                    The name of the target column(s).
            multi_label : bool, default False
                    If the target is a multi-label column.
            clean : bool, default True
                    Clean the column names created from the target column.
            sep : str, default ','
                    The delimiter to use when opening csv or txt files.
        
        Attributes:
            target
                The cleaned target.
    """
    def __init__(self, target:str=None, multi_label:bool=False, data:pd.DataFrame=None, clean=True, sep:str=','):
        self.__target = target
        self.__multi_label = multi_label
        self.__sep = sep
        self.__multi_label_columns = self._create_multi_label_columns(data=data, clean=clean)

    def __eq__(self, other) -> bool:
        if not self.__multi_label or utility.is_array(other):
            return self.target == other
        # if checking a string against the columns, see if that string exists in the columns
        return other in self.__multi_label_columns

    def __hash__(self):

        return hash(tuple(self.target))

    def __contains__(self, item) -> bool:

        return item in self.target
        
    def __iter__(self):

        for item in self.target:
            yield item

    def __str__(self) -> str:

        return str(self.target)

    def __repr__(self):

        return self.target

    @property
    def target(self):

        return self.__target if not self.__multi_label else self.__multi_label_columns

    def _create_multi_label_columns(self, data:pd.DataFrame, clean:bool=True) -> list:
        
        # if an iterable keep
        if utility.is_array(self.__target):
            return self.__target

        if not self.__multi_label or data is None:
            return []

        if self.__target not in data.columns:
            raise KeyError(f'The column {self.target} does not exist in the data.')

        data = utility.data_reader(data=data)

        unique_items = get_unique_column_values(data=data[self.__target], sep=self.__sep)

        if clean:
            unique_items = clean_list_items(list_items=unique_items)

        return unique_items

        
def get_unique_column_values(data:pd.Series, sep:str=',') -> list:
    """
    Get the unique values found in the data.

        Args:
            data : pandas.Series
                The data to get the unique values from.
            sep : str, default ','
                The separator used to seprate values in lists.

        Returns:
            (list) : A list of the unique values found in your pandas.Series including those in lists.
    """
    utility.assert_item_type(item=data, item_types=[pd.Series(dtype='object')])

    all_values = data.str.split(sep).values

    unique_items = utility.flatten_list(all_values, deduplicate=True, apply_to_items=lambda x: str(x).strip(), ignore_items=['nan', ''])

    return unique_items


def one_hot_encode_from_data(data:pd.DataFrame, target:str, labels:list, clean:bool=True) -> pd.DataFrame:
    """
    One hot encode your data from the data in the lists in each row.

        Args:
            data : pandas.DataFrame
                The data to one hot encode.
            target : str
                The column containing the data to one hot encode.
            labels : list
                The list of labels you want to create new columns for.
            clean : bool, default True
                Clean the data in the target column.

        Returns:
            (pandas.DataFrame) : Returns a dataframe with the data one hot encoded from the relevant column.
    """
    data = utility.data_reader(data=data)

    # this ensures all values are in array form
    data[target] = data[target].apply(lambda x: [x] if not utility.is_array(x) else x)

    if clean:
        data[target] = data[target].apply(lambda x: clean_list_items(x))

    for col in (item for item in labels):
        new_col = pd.Series(data[target].apply(lambda x: 1 if col in x else 0), name=col)
        data = pd.concat((data, new_col), axis=1)

    return data

     
def clean_list_items(list_items:list, clean_regex=None) -> list:
    """
    Check to see if a particular label appears in the row data.

        Args:
            list_items : list
                The list of data items to clean.

        Returns:
            (list) : Returns the cleaned list.
    """
    
    clean_regex = statics.CLEAN_COLUMN_NAME_REGEX if clean_regex is None else clean_regex

    return list(map(lambda x: utility.remove_characters(x, remove_chars=clean_regex, is_regex=True), list_items))