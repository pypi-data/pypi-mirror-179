from ..main.input import (Ensemble, FeatSelector, Scaler, Pipeline, Model,
                          ParamSearch, Transformer, Imputer)
from ..main.compare import Compare, Option


# Pieces
# TODO add identity loader to default pipelines?
m_imputer = Imputer('mean', scope='float')
c_imputer = Imputer('median', scope='category')
r_scaler = Scaler('robust', scope='float')
ohe = Transformer('one hot encoder', scope='category')

random_search = ParamSearch('RandomSearch', n_iter=60, cv=3)
hs_search = ParamSearch('HammersleySearch', n_iter=60, cv=5)

elastic_search = Model('elastic', params=1, param_search=hs_search)
ridge_search = Model('ridge', params=1, param_search=hs_search)
rf_search = Model('rf', params=1, param_search=hs_search)
svm_search = Model('svm', params=1, param_search=hs_search)
gb_search = Model('hgb', params=1, param_search=hs_search)

u_feat = FeatSelector('univariate selection', params=2)
svm = Model('svm', params=1)
svm_fs_search_pipe = Pipeline(steps=[u_feat, svm], param_search=hs_search)
svm_fs_search = Model(svm_fs_search_pipe)


stacking = Ensemble('stacking', models=[elastic_search,
                                        ridge_search,
                                        svm_fs_search,
                                        gb_search],
                    base_model=ridge_search,
                    n_jobs_type='models')

voting = Ensemble('voting', models=[elastic_search,
                                    ridge_search,
                                    svm_fs_search,
                                    gb_search],
                  n_jobs_type='models')

# Pre-defined pipelines
_base_steps = [m_imputer, c_imputer, r_scaler, ohe]

elastic_pipe = Pipeline(steps=_base_steps + [elastic_search])
ridge_pipe = Pipeline(steps=_base_steps + [ridge_search])
gb_pipe = Pipeline(steps=_base_steps + [gb_search])
rf_pipe = Pipeline(steps=_base_steps + [rf_search])
svm_pipe = Pipeline(steps=_base_steps + [svm_search])
svm_fs_pipe = Pipeline(steps=_base_steps + [svm_fs_search])

stacking_pipe = Pipeline(steps=_base_steps + [stacking])
voting_pipe = Pipeline(steps=_base_steps + [voting])

compare_pipe = Compare([Option(elastic_pipe, name='elastic'),
                        Option(ridge_pipe, name='ridge'),
                        Option(svm_fs_pipe, name='svm_fs'),
                        Option(gb_pipe, name='gb')])

pieces = {'m_imputer': m_imputer,
          'c_imputer': c_imputer,
          'r_scaler': r_scaler,
          'ohe': ohe,
          'random_search': random_search,
          'hs_search': hs_search,
          'elastic_search': elastic_search,
          'rf_search': rf_search,
          'gb_search': gb_search,
          'svm_search':  svm_search,
          'u_feat': u_feat,
          'svm': svm,
          'svm_search_pipe': svm_fs_search_pipe,
          'svm_fs_search': svm_fs_search,
          'ridge_search': ridge_search,
          'stacking': stacking,
          'voting': voting}

pipelines = {'elastic_pipe': elastic_pipe,
             'ridge_pipe': ridge_pipe,
             'rf_pipe': rf_pipe,
             'gb_pipe': gb_pipe,
             'svm_pipe': svm_pipe,
             'svm_fs_pipe': svm_fs_pipe,
             'stacking_pipe': stacking_pipe,
             'voting_pipe': voting_pipe,
             'compare_pipe': compare_pipe}

pieces_keys = list(pieces)
pipelines_keys = list(pipelines)
