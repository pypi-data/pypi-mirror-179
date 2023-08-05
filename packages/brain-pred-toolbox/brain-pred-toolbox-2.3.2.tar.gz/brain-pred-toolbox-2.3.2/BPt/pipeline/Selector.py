from sklearn.utils.metaestimators import _BaseComposition, available_if
from ..default.params.Params import Dict, Choice
from .base import _get_est_fit_params, _get_est_trans_params

def _ex_estimator_has(attr):
    return lambda self: (hasattr(self.example_estimator_, attr))

def _estimator_has(attr):
    return lambda self: (hasattr(self.estimator_, attr))

class Selector(_BaseComposition):

    _needs_mapping = True
    _needs_fit_index = True
    _needs_transform_index = True

    def __init__(self, estimators, to_use=0):
        self.estimators = estimators
        self.to_use = to_use
        self.example_estimator_ = self.estimators[0][1]

    def get_params(self, deep=True):
        return self._get_params('estimators', deep=deep)

    def set_params(self, **kwargs):

        # Pass params as dict with key select
        select = kwargs['select']

        # Get to use from select
        self.to_use = select['to_use']

        # Set rest of select params
        self._set_params('estimators', **select)
        return self

    @available_if(_ex_estimator_has("fit"))
    def fit(self, *args, **kwargs):

        # Select correct estimator
        self.estimator_ = self.estimators[self.to_use][1]

        # Set correct fit params based on chosen estimator
        fit_params = _get_est_fit_params(self.estimator_, other_params=kwargs)

        # Fit
        self.estimator_.fit(*args, **fit_params)
        self.is_fitted_ = True

        return self

    @available_if(_ex_estimator_has("fit_transform"))
    def fit_transform(self, *args, **kwargs):

        self.estimator_ = self.estimators[self.to_use][1]
        return self.estimator_.fit_transform(*args, **kwargs)

    @available_if(_ex_estimator_has("transform"))
    def transform(self, *args, **kwargs):

        if 'transform_index' in kwargs:
            transform_index = kwargs.pop('transform_index')
        else:
            transform_index = None

        tranform_params = _get_est_trans_params(self.estimator_,
                                                transform_index)

        return self.estimator_.transform(*args, **tranform_params)

    @available_if(_ex_estimator_has("fit_resample"))
    def fit_resample(self, *args, **kwargs):
        self.estimator_ = self.estimators[self.to_use][1]
        return self.estimator_.fit_resample(*args, **kwargs)

    @available_if(_ex_estimator_has("fit_predict"))
    def fit_predict(self, *args, **kwargs):
        self.estimator_ = self.estimators[self.to_use][1]
        return self.estimator_.fit_predict(*args, **kwargs)

    @available_if(_estimator_has("predict"))
    def predict(self, *args, **kwargs):
        return self.estimator_.predict(*args, **kwargs)

    @available_if(_estimator_has("predict_proba"))
    def predict_proba(self, *args, **kwargs):
        return self.estimator_.predict_proba(*args, **kwargs)

    @available_if(_estimator_has("decision_function"))
    def decision_function(self, *args, **kwargs):
        return self.estimator_.decision_function(*args, **kwargs)

    @available_if(_estimator_has("predict_log_proba"))
    def predict_log_proba(self, *args, **kwargs):
        return self.estimator_.predict_log_proba(*args, **kwargs)

    @available_if(_estimator_has("score"))
    def score(self, *args, **kwargs):
        return self.estimator_.score(*args, **kwargs)

    @available_if(_estimator_has("inverse_transform"))
    def inverse_transform(self, *args, **kwargs):
        return self.estimator_.inverse_transform(*args, **kwargs)

    @available_if(_estimator_has("transform_df"))
    def transform_df(self, *args, **kwargs):
        return self.estimator_.transform_df(*args, **kwargs)

    @available_if(_estimator_has("_proc_new_names"))
    def _proc_new_names(self, *args, **kwargs):
        return self.estimator_._proc_new_names(*args, **kwargs)

    @property
    def _estimator_type(self):
        '''This should remain static across all passed estimators'''
        return self.example_estimator_._estimator_type

    @property
    def feature_importances_(self):
        if hasattr(self.estimator_, 'feature_importances_'):
            return getattr(self.estimator_, 'feature_importances_')
        return None

    @property
    def coef_(self):
        if hasattr(self.estimator_, 'coef_'):
            return getattr(self.estimator_, 'coef_')
        return None

    @property
    def classes_(self):
        if hasattr(self.estimator_, 'classes_'):
            return getattr(self.estimator_, 'classes_')
        return None


def selector_wrapper(objs, params, name):

    selector = (name, Selector(objs))

    p_dicts = []
    for i in range(len(objs)):
        obj_name = objs[i][0]
        rel_params =\
            {p: params[p] for p in params if p.split('__')[0] == obj_name}
        rel_params['to_use'] = i

        p_dict = Dict(**rel_params)
        p_dicts.append(p_dict)

    select = Choice(p_dicts, deterministic=True)
    select_params = {name + '__select': select}

    return selector, select_params
