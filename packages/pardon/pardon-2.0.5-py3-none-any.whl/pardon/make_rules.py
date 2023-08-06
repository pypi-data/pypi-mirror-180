import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy import stats

from . import utility


pd.options.mode.chained_assignment = None 


class FailOnOutput:
    '''
    The class object returned from the pardon.FailOn.apply_fail_on method.

        Args:
            column : str
                The column of the FailOn.
            failed : bool
                A Boolean stating if the FailOn failed or not. True means the FailOn failed, and False means it did not.
            failed_value : int, float, str
                The value that failed the FailOn

        Attributes:
            column
                The column of the FailOn.
            failed
                A Boolean stating if the FailOn failed or not. True means the FailOn failed, and False means it did not.
            failed_value
                The value that failed the FailOn
    '''
    def __init__(self, column, failed, failed_value=None):
        self.column = column
        self.failed = failed
        self.failed_value = failed_value

    def __str__(self):
        output = f'FailOn Ouput: Column: {self.column} | Failed: {self.failed}'

        return output


class FailOn:
    '''
    Class allowing a set of rules to be applied to the input data. If any of these rules match, the input data will invoke a failure. Essentially, add a rule that will cause a failure. 
        
        Args:
            column : str
                The column name you are applying the Fail On rule to.
            operator : str {'gt', 'gte', 'e', 'ne','lt', 'lte', 'i', 'ni', 'b', 'nb'}
                The rule logic to be applied. The descriptions are as follows:
                -> gt: Greater than
                -> gte: Greater than or equal to
                -> e: Equal to
                -> ne: Not equal to
                -> lt: Less than
                -> lte: Less than or equal to
                -> i: In
                -> ni: Not in
                -> b: Between
                -> nb: Not between
            value : str, int, float
                The value to compare the logic and calculation to. For example, if you used the operator 'lt', and value=5, if the column contains a value less than 5, a failure will be invoked.
            calculation : func, str, None, default None
                The function to apply to the column before making the comparison. The following in-built functions can be passed as strings: 'mean', 'median', 'mode', 'z_score', 'max', 'min', 'sum', 'count'. 
                Note, if only 1 row is passed for checking, the raw value from the row will be used instead of the calculation, except for 'z_score', where 0 will be used.
            subset : dict, None, default None
                Add any subset of the data you wish to apply the check to. For example, if you only wanted to apply this to customers with a last name of 'Smith' in the customer_last_name column, you could use subset=dict(customer_last_name='Smith').
    
        Attributes:
            column
                The column that the FailOn is applied to.
            operator
                The FailOn operator.
            value
                The FailOn value for comparison.
            calculation
                The FailOn calculation to apply to the column.
            subset
                The subset to apply the FailOn to.
    '''
    def __init__(self, column, operator, value, calculation=None, subset=None):
        self.__NUMERIC_ONLY_CALCS = (np.std, np.mean, np.median, stats.zscore, np.max, np.min,  np.sum)
        self.__CALC_OPERATORS = {'gt': '_greater_than', 
                                 'lt': '_less_than', 
                                 'gte' : '_greater_than_or_equal_to', 
                                 'lte': '_less_than_or_equal_to', 
                                 'e': '_equal_to', 
                                 'ne': '_not_equal_to',  
                                 'b': None, # these are determined differently
                                 'nb': None, # these are determined differently 
                                 'i': '_in', 
                                 'ni': '_not_in'}
        self.__CALC_OPTIONS = {'sd': np.std, 
                               'mean': np.mean, 
                               'mode': utility.get_mode, 
                               'median': np.median, 
                               'z_score': utility.get_z_score, 
                               'max': np.max, 
                               'min': np.min,
                               'sum': np.sum,
                               'count': len}
                               
        self._operators = list(self.__CALC_OPERATORS.keys())
        self.column = column
        self.operator = str(operator).lower()
        self.value = value
        self.calculation = calculation
        self._calculation = None
        self._calculated_value = None
        self.subset = subset
        self._greater_than = None
        self._less_than = None
        self._greater_than_or_equal_to = None
        self._less_than_or_equal_to = None
        self._equal_to = None
        self._not_equal_to = None 
        self._bnb_start = None
        self._bnb_end = None
        self._in = None 
        self._not_in = None
        # validate the arguments
        self._validate_args()

    def __repr__(self):

        return f'{self.column} | {self.operator} | {self.value}'

    def __str__(self):

        # string output of the Rule class
        output = f'Column: {self.column}'

        for attr in self.__CALC_OPERATORS.values():
            if attr is not None:
                v = getattr(self, attr)
                if v is not None:
                    output += f' | {attr.replace("_", " ").title().strip()}: {v}'
        
        if self.operator in ('b', 'nb'):
            output += f' | Between: {self._bnb_start} and {self._bnb_end}'

        if self.calculation is not None:
            output += f' | Calculation: {self.calculation}'
 
        return output
    
    def _validate_args(self):

        # validate argument logic here
        # check the operator
        if self.operator not in self._operators:
            raise ValueError(f'operator should be one of the following {self._operators}.')

        if self.subset is not None and not isinstance(self.subset, dict):
            raise TypeError(f'The subset parameter can only take None or a dictionary object. When using this option, supply the column name of the subset as your dict key, and the value of the subset as your value. E.G subset=dict(LastName="Smith")') 

        # see if there is a particular calculation
        if isinstance(self.calculation, str):
            self._calculation = self.__CALC_OPTIONS.get(self.calculation, None) if self.__CALC_OPTIONS.get(self.calculation, None) is not None else self.calculation
 
        # if using a calculation, it should be a function
        if self._calculation is not None:
            if not callable(self._calculation):
                raise ValueError(f'The calculation needs to be a callable function or object, or one of the following {list(self.__CALC_OPTIONS.keys())}')

        # there must be either a calculation or a value
        if self._calculation is None and self.value is None:
            raise ValueError('You must provide a specific value, or set of values, or a calculation. They cannot both be None.')

        # check betweens and ins
        if self.operator in ('b', 'nb', 'i', 'ni'):
            if not isinstance(self.value, list):
                # set the argument specific error
                if self.operator in ('b', 'nb'):
                    msg = 'When using between or not between, pass the values in a list, going from smallest to largest. eg. value=[3, 500]'
                    # raise the error
                    raise ValueError(msg)
                else:
                    # if using i, ni, change to a list
                    self.value = [self.value]
            
            # check between values
            if self.operator in ('b', 'nb'):
                # ensure all values are numeric
                if not all(map(lambda x: isinstance(x,(int, float)), self.value)):
                    raise ValueError('When using between or not between, all values must be numeric.')
                # ensure there are 2 values
                if len( self.value) != 2:
                    raise ValueError('When using between or not between, 2 values must be provided, the lowest value then the highest value.')
                # get the start and end value
                start_val = self.value[0]
                end_val = self.value[1]
                # if start is greater than end, switch them
                if start_val > end_val:
                    # switch them
                    start_val, end_val = end_val, start_val
                    print(f'*** WARNING: between values were in the wrong order so they were switch to between {start_val} and {end_val} instead of {end_val} to {start_val} ***')

                # set attributes
                self._bnb_start = start_val
                self._bnb_end = end_val

        # set the in or not in attributes
        attr = self.__CALC_OPERATORS.get(self.operator)

        # set the attribute if not None
        if attr is not None:
            setattr(self, attr, self.value)

    def apply_fail_on(self, data, encoding:str='latin-1', sep:str=',') -> FailOnOutput:
        '''
        Returns a FailOnOutput object containing the FailOn assessment after apply the FailOn to the dataset.
            
            Args:
                data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame
                    The data to apply the FailOn to.
                encoding : str, default 'latin-1' {'latin-1' , 'ascii', 'utf-8'}
                    The encoding used when opening csv files.
                sep : str, default ','
                    The delimiter to use when opening csv or txt files.
        '''
        # if the user is just testing a single value, try it here
        if isinstance(data, (int, float)) or (isinstance(data, str) and not utility.looks_like_file(data)):
            df = pd.DataFrame(columns=[self.column])
            df[self.column] = [data]
            data = df
        else:
            # get the data into a dataframe
            data = utility.data_reader(data=data, encoding=encoding, sep=sep)
        
        # just keep the relevant column
        data = data.copy()

        # check the calculation to be applied if it needs to be to a numeric column, enforce that rule
        if self._calculation in self.__NUMERIC_ONLY_CALCS and not is_numeric_dtype(data[self.column]):
            raise ValueError(f'The calculation: {self.calculation}, requires a numeric column. The column: {self.column} is not numeric. Change the FailOn parameters and try again.')
        
        # if using subset, get them
        if self.subset is not None:
            # get the subset columns
            for sub_col, sub_val in self.subset.items():
                # set it to be a list by default
                if not isinstance(sub_val, list):
                    sub_val = [sub_val]
                # get the values
                data = data[data[sub_col].isin(sub_val)]

        # check if we need to make a calculation
        if self._calculation is not None:
            # if the data is 1 row, just get the first item
            if len(data) == 1 and self._calculation != len:
                # if the user selected z score, just set to 0 as we cannot work out the z scores
                if self.calculation == 'z_score':
                    self._calculated_value = 0
                else:
                    # get the raw value as no calculations possible
                    self._calculated_value = data[self.column].iloc[0]
            else:
                # apply the calculation to the data
                self._calculated_value = self._calculation(data[self.column])
        else:
            # set calc val to be None if not using
            self._calculated_value = None

        failed = self.__assess(data=data)
   
        return FailOnOutput(column=self.column, failed=failed)

    def __assess(self, data) -> bool:
        # returns True if the assessment fails else false if it passes - this is because we are testing a "FailOn"
        failed = False

        # if using the betweens, get the start and end
        if self.operator in ('b', 'nb'):
            start = self._bnb_start
            end = self._bnb_end
            # get the function we will use
            if self.operator == 'b':   
                bnb_lambda = lambda x, start, end: True if x >= start and x <= end else False
            else:
                bnb_lambda = lambda x, start, end: True if x < start or x > end else False

            # check the calculations
            if self._calculated_value is not None:
                # check to see if the calculated value matches the brief
                failed = bnb_lambda(self._calculated_value, start, end)
            else:
                # if no calculated value, check every row using apply
                failed = data[self.column].apply(lambda x: bnb_lambda(x, start, end)).any()
            
        elif self.operator in ('i', 'ni'):
            # get the attribute name
            check_attr = self.__CALC_OPERATORS.get(self.operator)
            # get the values
            check_val = getattr(self, check_attr)

            # ensure we are dealing with a list
            if not isinstance(check_val, list):
                check_val = [check_val]

            # check if in or not in
            if self.operator == 'i':
                # check if in
                data = data[data[self.column].isin(check_val)]
            else:
                # check if not in
                data = data[~data[self.column].isin(check_val)]
            
            # if we meet any of these, we fail
            if len(data) > 0:
                failed = True
        # for the others, a calculation would have been required
        else:
            # iterate through the operators, if we get a value, that was the one provided by the user
            for attr in self.__CALC_OPERATORS.values():
                if attr is not None:
                    # if we have a value, this means it is the one we're using
                    val = getattr(self, attr)
                    if val is not None:
                        # if check using relevant operator
                        if self.operator == 'gt':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value > val else False
                            else:
                                failed = True if len(data[data[self.column] > self.value]) > 0 else False
                        elif self.operator == 'gte':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value >= val else False
                            else:
                                failed = True if len(data[data[self.column] >= self.value]) > 0 else False
                        elif self.operator == 'lt':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value < val else False
                            else:
                                failed = True if len(data[data[self.column] < self.value]) > 0 else False
                        elif self.operator == 'lte':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value <= val else False
                            else:
                                failed = True if len(data[data[self.column] <= self.value]) > 0 else False
                        elif self.operator == 'e':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value == val else False
                            else:
                                failed = True if len(data[data[self.column] == self.value]) > 0 else False
                        elif self.operator == 'ne':
                            if self._calculated_value is not None:
                                failed = True if self._calculated_value != val else False
                            else:
                                failed = True if len(data[data[self.column] != self.value]) > 0 else False

                        # break the loop as we are done
                        break

        return failed



        


