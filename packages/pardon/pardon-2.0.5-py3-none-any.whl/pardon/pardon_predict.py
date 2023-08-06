from datetime import datetime

import pandas as pd
import numpy as np
from flask import Response

from . import pardon_options
from . import utility

class Prediction:
    '''
    The class object returned from the pardon.Pardon.predict method.

        Args:
            target : str, default None
                The predicted target class.
            model_identifier : str, default None
                The unique identifier for the model that made the prediction.
            features : list, default None
                A dictionary object containing key value pairs of the input data passed for prediction.
            model_classes : list, default None
                The classes as used in the model training.
            class_labels : dict, default None
                The actual name of the classes as per the input data.
            predictions : str, int, list, default None
                The predictions made from the model.
            y : str, list, default None
                If training or test data was used, y is the labelled data containing the actual class or value of the input data.
            has_probabilties : bool, default False
                True if the predictions are probabilities for each class, False if a single prediction is made for each input data.

        Attributes:
            target
                The predicted target class.
            model_identifier
                The unique identifier for the model that made the prediction.
            features
                A dictionary object containing key value pairs of the input data passed for prediction.
            model_classes
                The classes as used in the model training.
            class_labels
                The actual name of the classes as per the input data.
            predicted_datetime
                The datetime the prediction was made.
            y
                If training or test data was used, y is the labelled data containing the actual class or value of the input data.
            actual
                The correct class for the input data. Only available if y is provided.
            is_correct
                Is the prediction correct. Only available if y is provided.
            delta
                The difference between the prediction and actual. Only used with regression models when y is provided.
            predicted
                The predicted class or value for the input data. If a classification model, this is the class with the highest probability from the prediction.
            probabilities
                The probability of each class in the prediction. Only used in classification models that produce predictions with probabilities.
            audit
                The pardon.Audit class containing information on the predictions audit.
            error
                Details any errors occurred during the prediction. This should return None unless an error was encountered.
    '''
    __ROUND_PERCENTAGES_DECIMAL = 2
    def __init__(self, target=None, model_identifier=None, features=None, model_classes=None, class_labels=None, predictions=None, y=None, has_probabilties=False):
        self.target = 'Prediction' if target is None else target
        self.model_identifier = model_identifier
        self.features = features
        self.model_classes = model_classes
        self.class_labels = class_labels
        self.predicted_datetime = datetime.now().strftime(pardon_options.DATETIME_FORMAT)
        self.y = y
        self.actual = []
        self.is_correct = []
        self.delta = []
        self.predicted = []
        self.error = None
        self._error_code = None
        self.probabilities = []
        self._has_infs = False
        self._has_probabilties = has_probabilties
        self.__assign_prediction_data(predictions=predictions)
        self.audit = None

    def as_series(self) -> pd.Series:
        '''
        Return the predictions as a pandas Series.

            Returns: 
                (pandas.Series) : pandas.Series containing the model predictions.
        '''
        return pd.Series(self.predicted, name=self.target)

    def as_dataframe(self) -> pd.DataFrame:
        '''
        Return the predictions as a pandas DataFrame.

            Returns: 
                (pandas.DataFrame) : pandas.DataFrame containing the model predictions.
        '''
        return self.as_series().to_frame()

    def api_output(self, return_object:str='array', include_probabilities:bool=True, include_title:bool=False, as_json:bool=True) -> str:
        '''
        Return the output ready to be delivered to an API response.

            Args:
                return_object : str, default 'array' {'array', 'dict', 'list'}
                    The format of the response. Can be array, dict, or list. 'array' will attempt to determine the best output.
                include_probabilities : bool, default True
                    For classification problems decide if you want to include a probability score for each class. If False, the class with the highest probability will be returned.
                include_title : bool, default False
                    Include a title in the output. This will add the word 'Prediction' for classification predictions with no probabilities and regression models, and will add the words 'Class', and 'Probability of Class', for classification models with probabilities returning as a list.
                as_json : bool, default True
                    Return the output object in json format.

            Returns:
                (str) : Returns a string representation of the return_object, be it a list, dict, or array.
        '''

        if self._error_code is not None:
            response_dict = {'Reason': self.error}
            response = Response(f'{response_dict}', status=self._error_code, mimetype='application/json')
            # if an error has occurred, return an empty string and error code
            return response

        # if this is a regresison task, set include title to true if user wants a dict otherwise no key value pairing
        if not self._has_probabilties and return_object == 'dict' and not include_title:
            print('WARNING: setting include_title=True because return_object="dict". Use return_object="array" or "list" to ignore titles for regression models (or classification models without probabilities) or use include_probabilities=True for classification models.')
            include_title = True
        
        return_object = str(return_object).lower()
        full_output = []
        
        if return_object == 'list':
            if include_probabilities and self._has_probabilties:
                for prediction in self.probabilities: 
                    output_obj = self.__set_probability_values(prediction=prediction, include_title=include_title, for_list=True)
                    full_output.append(output_obj)
            else:
                for prediction in self.predicted:
                    if include_title:
                        prediction = [self.target, prediction]
                    full_output.append(prediction)
        else:
            # create an output object as a dictionary
            if include_probabilities and self._has_probabilties:
                for prediction in self.probabilities:
                    output_obj = self.__set_probability_values(prediction=prediction, include_title=include_title, for_list=False, as_json=as_json)
                    full_output.append(output_obj)
            else:
                for output_obj in self.predicted:
                    if as_json:
                        # if the user wants it to json, it must be a string
                        output_obj = str(output_obj)
                    if include_title:
                        # add the title
                        output_obj = {self.target: output_obj}

                    full_output.append(output_obj)

        # dump the output to json if requested
        if as_json:
            full_output = utility.to_json(full_output)

        return str(full_output)

    def __str__(self) -> str:
        # set the title
        output = f'{self.target} '

        # if nothing to show, just return the error message
        if self.error is not None:
            output += f'Prediction failed due to: {self.error})'
            return output

        output += f'Prediction(s): {self.predicted}'

        return output
        
    def __assign_prediction_data(self, predictions):
        '''Assign the predictions to the class'''
        # if we have receieved predictions
        if predictions is not None:
            try:
                # check the predictions is the right class
                if isinstance(predictions, np.ndarray):
                    # model_classes not none means we are working with classification problem
                    if self.model_classes is not None and self._has_probabilties:
                        for _, predict in enumerate(predictions):
                            class_dict = {}
                            for i, class_ in enumerate(self.model_classes):
                                pred_label = self.class_labels.get(class_) if self.class_labels.get(class_) is not None else class_
                                class_dict[pred_label] = predict[i]

                            class_dict = dict(sorted(class_dict.items(), key=lambda item: item[1], reverse=True))
                            self.probabilities.append(class_dict)
                            # set the actual predicted class
                            predicted = max(class_dict, key=class_dict.get) 
                            self.predicted.append(predicted)
                    else:
                        # iterate through and add each prediction
                        for _, predict in enumerate(predictions):
                            # check to see if inf has been returned - this is usally because training data was scaled and prediction not or vice versa
                            if np.isinf(predict):
                                # flag it if it is
                                self._has_infs = True
                            # regression predictions or models without predict proba
                            self.predicted.append(predict)
                    
                    if self.y is not None:
                        # iterate through each prediction and set if it were correct or not
                        for i, prediction in enumerate(self.predicted):
                            actual_raw = self.y.iloc[i]
                            actual = self.class_labels.get(actual_raw) if self.class_labels is not None and actual_raw in self.class_labels else actual_raw
                            self.actual.append(actual)
                            self.is_correct.append(actual == prediction)
                            # set the delta between predicted and actual if regression
                            if isinstance(actual, (int, float)) and isinstance(prediction, (int, float)):
                                self.delta.append(prediction - actual)
                            else:
                                self.delta.append(None)
                else:
                    # if the prediction is not an np array, it's invalid
                    self.error = f'Predictions object is of type: {type(predictions)} and not an np.ndarray, therefore is invalid.'

            except Exception as err:
                # catch the error
                self.error = err

    def __set_probability_values(self, prediction:dict, include_title:int=True, for_list:bool=True, as_json:bool=True) -> list:
        '''Set the prediction values'''

        # if using a list we perform this differently
        if for_list:
            output_obj = []
            # loop through the probabilities and set the key and value and add to array
            for k, v in prediction.items():
                k = 'None' if k is None else k
                # assign the values
                output_obj.append([str(k), round(v * 100, Prediction.__ROUND_PERCENTAGES_DECIMAL)])
            # sort the output
            output_obj = sorted(output_obj)
            # if none is found, put it to the end
            if 'None' in output_obj:
                output_obj.append(output_obj.pop('None'))
            if include_title:
                # add the title and legend list
                output_obj.insert(0, [self.target, 'Probability'])
        else:
            output_obj = {}
            for k, v in prediction.items():
                output_obj[str(k)] = round(v * 100, Prediction.__ROUND_PERCENTAGES_DECIMAL)
            # sort the dictionary in value order
            output_obj = utility.sort_dictionary(dict_object=output_obj, desc=True)
            # check json
            if as_json:
                # if using json, we need to make the values strings
                output_obj = {k: str(v) for k, v in output_obj.items()}
            if include_title:
                # add the title
                output_obj = {self.target: output_obj}

        return output_obj