from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier, SGDClassifier, LinearRegression, Ridge, SGDRegressor, ElasticNet, Lasso, HuberRegressor, PoissonRegressor
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, HistGradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, Birch, MeanShift, DBSCAN
import sklearn
import xgboost as xgb

from . import utility


def _models_and_names() -> dict:

    reg_mods = list(_regression_models().keys())
    class_mods = list(_classification_models().keys())
    all_mods = reg_mods + class_mods
    names_dict = {str(type(model).__name__).lower(): model for model in all_mods}

    return names_dict


def _regression_models() -> dict:
    # return the regression models
    # set parameter spaces for all model types
    lr_space = dict()
    lr_space['fit_intercept'] = [False, True]
    lr_space['normalize'] = [False, True]

    r_space = dict()
    r_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    r_space['tol'] = [0.001, 0.1, 1.0]

    sgdr_space = dict()
    sgdr_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    sgdr_space['learning_rate'] = ['invscaling', 'optimal']
    sgdr_space['max_iter'] = [1000, 1500, 2000]

    en_space = dict()
    en_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    en_space['l1_ratio'] = [0.5, 1.0]

    l_space = dict()
    l_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    l_space['tol'] = [0.001, 0.1, 1.0]

    h_space = dict()
    h_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    h_space['epsilon'] = [1.1, 1.35, 2.0]
    h_space['tol'] = [0.001, 0.1, 1.0]

    p_space = dict()
    p_space['alpha'] = [0.0001, 0.5, 1.0, 2.0]
    p_space['tol'] = [0.001, 0.1, 1.0]

    # set the regression models and their search space if any
    models = {LinearRegression(n_jobs=-1): lr_space,
            Ridge(random_state=13): r_space, 
            SGDRegressor(random_state=13): sgdr_space,
            ElasticNet(): en_space,
            Lasso(random_state=13): l_space,
            HuberRegressor(): h_space,
            PoissonRegressor(): p_space}

    return models


def _classification_models() -> dict:
    # return the classification models
    # set parameter spaces for all model types
    xgb_space = dict()
    xgb_space['colsample_bytree'] = [0.2, 0.5, 0.8]
    xgb_space['max_depth'] = [None, 4, 5]
    xgb_space['learning_rate'] = [0.1, 0.2, 0.3]
    # this just so we see the output
    xgb_space['verbosity'] = [2]
    
    rfc_space = dict()
    rfc_space['max_features'] = ['auto', 0.2, 0.5, 0.8]
    rfc_space['max_depth'] = [None, 4, 5, 6]
    rfc_space['ccp_alpha'] = [0.0, 0.2, 0.5]
    
    b_space = dict()
    b_space['alpha'] = [0.0, 0.5, 1.0, 1.5, 2.0]
    
    ab_space = dict()
    ab_space['learning_rate'] = [0.1, 0.2, 0.3, 0.5]
    ab_space['n_estimators'] = [50, 100, 200, 500]
    
    lr_space = dict()
    lr_space['penalty'] = ['l2', 'none']
    lr_space['C'] = [0.5, 1.0, 2.0]
    lr_space['tol'] = [0.001, 0.1, 1.0]
    
    bc_space = dict()
    bc_space['max_features'] = [0.3, 0.5, 0.8, 1.0]
    bc_space['max_samples'] = [0.3, 0.5, 0.8, 1.0]

    hgb_space = dict()
    hgb_space['learning_rate'] = [0.1, 0.2, 0.3, 0.5]
    hgb_space ['max_depth'] = [None, 4, 5]
    hgb_space ['l2_regularization'] = [0, 0.5, 1.75]
    
    sgd_space = dict()
    sgd_space['max_iter'] = [100, 200, 500, 1000]

    # knn seems a bit too slow for this
    knn_space = dict()
    knn_space['n_neighbors'] = [3, 5, 7]
    knn_space['weights'] = ['uniform', 'distance']

    pac_space = dict()
    pac_space['C'] = [0.5, 1.0, 2.0]
    pac_space['tol'] = [0.001, 0.1, 1.0]

    models = {xgb.XGBClassifier(random_state=13, n_estimators=500, n_jobs=-1, use_label_encoder=False): xgb_space,
            RandomForestClassifier(random_state=13, n_estimators=500, n_jobs=-1): rfc_space,
            BernoulliNB(): b_space,
            AdaBoostClassifier(random_state=13, n_estimators=500): ab_space,
            LogisticRegression(multi_class='multinomial', random_state=13, max_iter=1000, n_jobs=-1): lr_space,
            BaggingClassifier(random_state=13, n_jobs=-1): bc_space,
            HistGradientBoostingClassifier(max_iter=500, random_state=13): hgb_space,
            SGDClassifier(random_state=13, n_jobs=-1): sgd_space,
            KNeighborsClassifier(n_jobs=-1): knn_space,
            PassiveAggressiveClassifier(n_jobs=-1, random_state=13): pac_space}

    return models


def _st_get_models(is_regression:bool=None) -> list:
    # this is used in the streamlit app
    # if we dont know classif or regression, get all models
    if is_regression is None:
        classif = _classification_models()
        reg = _regression_models()
        models = utility.merge_dictionaries(classif, reg)
    else:
        models = _classification_models() if not is_regression else _regression_models()

    models = [type(model).__name__ for model in models.keys()]

    return models


def _st_get_scoring_metrics(is_regression:bool=None) -> list:
    # this is used in the streamlit app
    if is_regression is None:
        classif = _classification_scoring_metrics()
        reg = _regression_scoring_metrics()
        metrics = utility.merge_dictionaries(classif, reg)
    else:
        metrics = _classification_scoring_metrics() if not is_regression else _regression_scoring_metrics()

    return list(metrics.keys())


def _st_get_evaluation_metrics(is_regression:bool=None) -> list:
    # this is used in the streamlit app
    score_metrics = _st_get_scoring_metrics(is_regression)
    xgbmetrics = _xgboost_eval_metrics()

    eval_metrics = score_metrics + xgbmetrics if is_regression is not None and not is_regression else score_metrics

    return eval_metrics


def _regression_scoring_metrics() -> dict:
    mets = dict()
    mets['r2'] = sklearn.metrics.r2_score
    mets['explained_variance'] = sklearn.metrics.explained_variance_score
    mets['mean_absolute_error'] = sklearn.metrics.mean_absolute_error
    mets['mean_squared_error'] = sklearn.metrics.mean_squared_error
    mets['mean_squared_log_error'] = sklearn.metrics.mean_squared_log_error
    mets['median_absolute_error'] = sklearn.metrics.median_absolute_error
    mets['mean_absolute_percentage_error'] = sklearn.metrics.mean_absolute_percentage_error
    mets['max_error'] = sklearn.metrics.max_error

    return mets


def _classification_scoring_metrics() -> dict:
    mets = dict()
    mets['accuracy'] = sklearn.metrics.accuracy_score
    mets['recall_macro'] = sklearn.metrics.recall_score
    mets['precision_macro'] = sklearn.metrics.precision_score
    mets['jaccard_macro'] = sklearn.metrics.jaccard_score
    mets['f1_macro'] = sklearn.metrics.f1_score
    mets['balanced_accuracy'] = sklearn.metrics.balanced_accuracy_score
    mets['roc_auc'] = sklearn.metrics.roc_auc_score
    mets['log_loss'] = sklearn.metrics.log_loss

    return mets


def _xgboost_eval_metrics(num_classes:int=None) -> list:
    # the xgboost specific metrics
    evals = ['auc']
    n2_classes = ['mlogloss', 'merror']
    n_classes = ['logloss', 'error']

    if num_classes is None:
        evals.extend(n2_classes)
        evals.extend(n_classes)
    else:
        # when using more than 2 classes, xgboost has to use mean logloss and mean error so we set these to mlogloss and merror
        evals.extend(n2_classes) if num_classes > 2 else evals.extend(n_classes)
            
    return evals


def _scoring_metrics(is_regression:bool) -> dict:
    # return a dictionary of the various score metrics
    mets = dict()
    # regression and classification have different scoring methods
    mets = _regression_scoring_metrics() if is_regression else _classification_scoring_metrics()

    return mets


def _cluster_models() -> tuple:
    # returns the valid clustering models
    return (KMeans, Birch, MeanShift, DBSCAN) 


def _default_model(is_regression:bool=True):

    if is_regression:
        model = LinearRegression()
    else:
        # set the default xgboost
        model = xgb.XGBClassifier()

    return model


def _default_model_params(is_regression:bool=True, random_state:int=13) -> dict:
    # this is used with linear regression
    if is_regression:
        params = dict(n_jobs=-1)
    else: 
        # this is used with xgboost classifier
        params = dict(random_state=13, n_estimators=500, n_jobs=-1, use_label_encoder=False)
        # these were the parameters for the previous model
        # params = dict(n_estimators=500, random_state=random_state, verbosity=0, 
        #         colsample_bytree=0.2, learning_rate=0.2, max_depth=5, reg_lambda=1.75,
        #         subsample=0.7, n_jobs=-1, reg_alpha=0.5, num_parallel_tree=3, 
        #         gamma=0.5, use_label_encoder=False)

    return params
