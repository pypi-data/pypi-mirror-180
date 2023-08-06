import sqlite3
import sys, os
from . import utility


class Audit:
    '''
    Class for the auditing of predictions from a particular model. 

        Args:
            prediction : pardon.Pardon.Prediction, default None
                The pardon.Pardon.Prediction class object.
            fullpath : str, default None
                The location of the sqlite database file.

        Attributes:
            prediction
                The Pardon.Prediction object containing the prediction information.
            fullpath
                The fullpath to the sqlite database saving the predictions for audit.
            PREDICTIONS_TABLE_NAME
                The name of the predictions table name in the sqlite database instance.
    '''
    def __init__(self, prediction=None, fullpath=None):
        self.prediction = prediction
        self.fullpath = fullpath
        self.PREDICTIONS_TABLE_NAME = 'Predictions'
        self._error = None
        # if the oputput full path is invalid, confirm there is an error but do not fail as this is part of the prediction method
        if self.fullpath is not None and not self.__validation_db_directory(fullpath=self.fullpath):
            self._error = 'The output fullpath is invalid. Please ensure you include a valid directory and a filename ending .db'
        elif self.prediction and self.fullpath is not None:   
            self.__insert_prediction()
        elif self.prediction is None and self.fullpath is not None:
            # if the user is instantiating a class object without a prediction, check the file exists and error if not
            # check the fullpath and add the working directory if it was not added
            self.fullpath = utility.check_save_parameters(self.fullpath, filetype='.db')
            if not self.__validation_db_directory(fullpath=self.fullpath, check_file_exists=True):
                raise FileNotFoundError(f'The database file at {self.fullpath} does not exist')
        
    def __validation_db_directory(self, fullpath, check_file_exists=False):
        # ensure the file is the right type
        if not fullpath.endswith('.db'):
            return False
        # if the directory does not exist return invalid
        if not os.path.exists(os.path.dirname(fullpath)):
                return False
        # if the file must already exist, check it
        if check_file_exists:
            if not os.path.exists(fullpath):
                return False
        
        # return true
        return True
            
    def __execute_statement(self, sql, values=None):
        '''execute the sql statement'''
        # create the connection
        connection, cursor = self._connection_objects()
        
        if values is None:
            # execute the sql
            cursor.execute(sql)
        else:
            cursor.executemany(sql, values)

        # commit the changes
        connection.commit()
        # close cursor and connection
        cursor.close()
        connection.close()

    def _connection_objects(self):

        '''return the database connection object'''        
        # create the connection and cursor
        connection = sqlite3.connect(self.fullpath)
        cursor = connection.cursor()

        return connection, cursor
    
    def _drop_table(self):
        '''drop the predictions table'''
        # create drop statement
        drop_table_sql = f'DROP TABLE {self.PREDICTIONS_TABLE_NAME};'
        # execute the sql
        self.__execute_statement(self, sql=drop_table_sql)

    def __create_table(self):
        # create the table if it does not exist
        create_table_sql = f"""
                        CREATE TABLE IF NOT EXISTS {self.PREDICTIONS_TABLE_NAME}
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            model_identifier text NOT NULL,
                            features text NOT NULL,
                            prediction text NOT NULL,
                            prediction_date text NOT NULL,
                            prediction_probabilities text,
                            class_labels text);
                        """
        # execute the sql
        self.__execute_statement(sql=create_table_sql)
        
    def __insert_prediction(self):
        '''insert the prediction'''

        # ensure the table exists
        self.__create_table()

        # create the insert sql
        insert_sql = f"""INSERT INTO {self.PREDICTIONS_TABLE_NAME}
                            (model_identifier,
                            features,
                            prediction,
                            prediction_date,
                            prediction_probabilities,
                            class_labels)
                            VALUES (?, ?, ?, ?, ?, ?)"""
        
        insert_values = []
        # iterate over every prediction
        for i, prediction in enumerate(self.prediction.predicted):
            probabilities = self.prediction.probabilities[i] if self.prediction.probabilities else None
            vals = (f'{self.prediction.model_identifier}',
                    f'{self.prediction.features}',
                    f'{prediction}',
                    f'{self.prediction.predicted_datetime}', 
                    f'{probabilities}', 
                    f'{self.prediction.class_labels}')
            # append the tuple to the insert values
            insert_values.append(vals)

        if insert_values:
            #execute the insert
            self.__execute_statement(sql=insert_sql, values=insert_values)
            print(f'{len(insert_values)} predictions added successfully to {self.fullpath}')

    def select_all_predictions(self, include_headers=False) -> list:
        '''
        Function to return the predictions from the sqlite database containing the predictions data.

        Args:
            include_headers : bool, default False
                Include the column headers in the output

        Returns:
            (list) : Returns a list containing the predictions that have been saved in the sqlite database.
        '''

        # ignore this if output full path is none
        if self.fullpath is None:
            raise FileNotFoundError(f'Please specify a valid database file using the output_fullpath parameter and try again.')

        # check the database exists
        if not self.__validation_db_directory(fullpath=self.fullpath):
            raise FileNotFoundError(f'The file {self.fullpath} cannot be found, please check the output fullpath and try again.')
        
        # create the connection
        connection, cursor = self._connection_objects()
        
        # execute the select statement
        cursor.execute(f"SELECT * FROM {self.PREDICTIONS_TABLE_NAME}")

        # get all predictions
        all_preds = cursor.fetchall()

        # if the user wants the headers, add them
        if include_headers:
            headers = list(map(lambda x: x[0], cursor.description))
            # insert the headers as the first row
            all_preds.insert(0, headers)
        
        # close cursor and connection
        cursor.close()
        connection.close()
        
        return all_preds