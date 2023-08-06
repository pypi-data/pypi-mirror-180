from flask import Flask

from . import pardon
from . import utility


class TestAPI:
    """
    Launch an API on the local host to test the output of your saved Pardon model.

        Args:
            model_fullpath : str, pardon.Pardon model
                The full path to your pardon.Pardon pkl file or your pardon.Pardon model.
            return_object : str, default 'array' {'array', 'dict', 'list'}
                The format you want to display in your API output. Array will display an array object containing a dictionary of the class name and the probability predicted for each class or just the prediction if using a regression model. Can also pass 'dict' or 'list'.
            data : csv, txt, xls, xlsx, xlsm, json, parquet, xml, dict, list, numpy.ndarray, pandas.DataFrame, default None
                The data you want to get a prediction for. If not specified, a random row will be selected from the original raw input data.
            include_probabilities : bool, default True
                For classification problems decide if you want to include a probability score for each class. If False, the class with the highest probability will be returned.
            include_title : bool, default False
                Include a title in the output. This will add the target column name for classification. It will also add 'Probability of Class', for classification models with probabilities returning as a list. 
    
        Attributes:
            model
                The Pardon class model.
            data
                The data for prediction.
            return_object
                The format for the API output.
            include_probabilities
                If probabilities are included in the API output.
    """
    def __init__(self, model_fullpath, return_object='array', data=None, include_probabilities=True, include_title=False):

        # load the model - if a pardon model has been passed, use that
        self.model = utility.load_model(model_fullpath=model_fullpath) if not isinstance(model_fullpath, pardon.Pardon) else model_fullpath
        # test that the model has a valid, trained model
        if self.model.model is None:
            raise Exception(f'The model has not been trained and therefore predictions cannot be tested. Train and save your model and try again.')
        
        # assign the data
        self.data = data
        # log the return object format
        self.return_object = str(return_object).lower() if return_object is not None else 'array'
        # log the if probabilities are required
        self.include_probabilities = include_probabilities
        # log if titles are required
        self.include_title = include_title
        # start a flask app
        app = Flask('pardon_test_api')
        # set a rule where whenever a user hits root /, it will run the predict method below
        app.add_url_rule("/", view_func=self.predict)
        # start the flask app
        app.run()

    def predict(self):
        """
        Returns a pardon.Pardon.Prediction.api_output str object containing the api_output for the prediction.

            Returns:
                (str) : Returns a pardon.Pardon.Prediction.api_output str object containing the api_output for the prediction.
        """
        # get data for prediction, use sample row if none specified
        prediction_data = self.model.get_sample_rows(n_rows=1) if self.data is None else self.data
        # ensure the format is right
        prediction_data = utility.data_reader(data=prediction_data, encoding=self.model._encoding, sep=self.model._sep)
        # make a prediction
        prediction = self.model.predict(data=prediction_data, audit_fullpath=None, check_fail_ons=True)
        # create the api output fromn the prediction
        api_data = prediction.api_output(return_object=self.return_object, include_probabilities=self.include_probabilities, include_title=self.include_title, as_json=True)

        return api_data