"""     
    MIN_ROW_REQ
        The minimum number of rows required to train a model. Note, this attribute can be changed prior to instantiation if required. Use: pardon.pardon_options.MIN_ROW_REQ = 10.
    VALID_FILE_FORMATS
        A tuple containing the valid file formats accepted by the Pardon object data parameter. Only available after class instantiation. These values should not be changed.
    DATETIME_FORMAT
        The format to display datetimes. A list of valid date formats can be found here. Change this by using pardon.pardon_options.DATETIME_FORMAT = '%d %B %Y %H:%M:%S'
    AVERAGE_FAIL_DEFAULT_VALUE
        The value to use if the function fails when performing an average calculation. An average calculation may fail if the column contains only nulls or other invalid values. To change this, you can use pardon.pardon_options.AVERAGE_FAIL_DEFAULT_VALUE = 99
    MIN_SAMPLE_FOR_UNDERSAMPLE
        The minimum number of rows to be present before under-sampling will be performed when balancing classes. If the number of instances of a class is fewer than the MIN_SAMPLE_FOR_UNDERSAMPLE, over-sampling will be performed, else under-sampling will be performed. This is to prevent rows being lost in smaller datasets. The default is 20,000 rows in the class with the fewest instances. To change this, you can use pardon.pardon_options.MIN_SAMPLE_FOR_UNDERSAMPLE = 5000
    UNDER_SAMPLING_MODEL
        The model object to use when performing under-sampling. The default is random under-sampling To change this, import the necessary libraries and you can use something like pardon.pardon_options.UNDER_SAMPLING_MODEL = imblearn.under_sampling.TomekLinks()
    OVER_SAMPLING_MODEL
        The model object to use when performing under-sampling. The default is random over-sampling To change this, import the necessary libraries and you can use something like pardon.pardon_options.OVER_SAMPLING_MODEL = imblearn.over_sampling.SMOTE()
    XGBCLASSIFIER_DEFAULT
        The default evaluation metric to use for XGBClassifiers. This is set to 'mlogloss'. You can change this using pardon.pardon_options.XGBCLASSIFIER_DEFAULT = 'auc'
    XGBCLASSIFIER_BINARY_DEFAULT
        The default evaluation metric to use for XGBClassifiers predicting binary classes. This is set to 'logloss'. You can change this using pardon.pardon_options.XGBCLASSIFIER_BINARY_DEFAULT = 'auc'
    SKLEARN_CLASSIFIER_DEFAULT
        The default evaluation metric to use for SKLearn classification models. This is set to 'accuracy'. You can change this using pardon.pardon_options.SKLEARN_CLASSIFIER_DEFAULT = 'recall_macro'
    SKLEARN_REGRESSION_DEFAULT
        The default evaluation metric to use for SKLearn classification models. This is set to 'r2'. You can change this using pardon.pardon_options.SKLEARN_REGRESSION_DEFAULT = 'explained_variance'
    REDUCTION_SCORE_ON
        The metrics that attempt to be minimised when determining best model performance. For these metrics, a lower score indicates a better performing model as opposed to a higher score. This should not be changed.
    BALANCE_SCALE_RATIO 
        This is set to 0.8. This ratio determines when classes will be balanced using over or under sampling. The formula for determining if classes should be balanced is calculated as follows:
        max_ratio = (max_class_instances / total_class_instances) x BALANCE_SCALE_RATIO
        ratio = number_of_class_instances / total_class_instances
        if ratio < rax_ratio for any of the classes, then class balancing will be performed.
        Take the following example:
            Class_a = 200 items
            Class_b = 100 items
            Class_c = 50 items
            max_ratio = (200 / 350) x 0.8 = 0.46
            ratio (Class_c) = 50 / 350 = 0.14
        0.14 < 0.46 and so class balancing will be performed.
        Setting the BALANCE_SCALE_RATIO = 1 will force class balancing to occur unless every single class has the same number of items. Setting the BALANCE_SCALE_RATIO = 0 would mean class balancing would never occur. Therefore, you can tweak this ratio to control the sensitivity when determining class balancing.
        You can change this using pardon.pardon_options.BALANCE_SCALE_RATIO = 0.95
    IGNORE_SINGLE_CLASS_ERROR
        Set this to True if you want to ignore the error raised when encountering single instances of classes. These rows will need to be removed before model training. Switch this check off by using pardon.pardon_options.IGNORE_SINGLE_CLASS_ERROR = True 
"""


from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler


DATETIME_FORMAT = '%d %B %Y %H:%M:%S'
MIN_ROW_REQ = 10
AVERAGE_FAIL_DEFAULT_VALUE = 0
MIN_SAMPLE_FOR_UNDERSAMPLE = 20000
UNDER_SAMPLING_MODEL = RandomUnderSampler(sampling_strategy='not minority')
OVER_SAMPLING_MODEL = RandomOverSampler(sampling_strategy='not majority')
XGBCLASSIFIER_DEFAULT = 'mlogloss'
XGBCLASSIFIER_BINARY_DEFAULT = 'logloss'
SKLEARN_CLASSIFIER_DEFAULT = 'accuracy'
SKLEARN_REGRESSION_DEFAULT = 'r2'
REDUCTION_SCORE_ON = ['mean_absolute_error', 'mean_squared_error', 'mean_squared_error', 'median_absolute_error', 'max_error', 'mean_absolute_percentage_error', 'log_loss']
BALANCE_SCALE_RATIO = 0.8
PREDICTED_COL_SUFFFIX = ' [predicted]'
IGNORE_SINGLE_CLASS_ERROR = False
