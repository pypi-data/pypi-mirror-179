import pandas as pd
import numpy as np
from sklearn.base import clone
import time
import warnings
from ..dataset.helpers import verbose_print
from ..pipeline.helpers import get_mean_fis
from sklearn.utils import Bunch
from scipy.stats import t
from pandas.util._decorators import doc
from .stats_helpers import corrected_std, compute_corrected_ttest
from sklearn.metrics._scorer import (_PredictScorer, _ProbaScorer,
                                     _ThresholdScorer)
from .helpers import clean_str
from copy import deepcopy
import pickle as pkl

from numpy.random import default_rng
import seaborn as sns
import matplotlib.pyplot as plt

from ..util import _refresh_bar, get_progress_bar

from sklearn.metrics._scorer import _MultimetricScorer

_base_docs = {}

_base_docs['dataset'] = """dataset : :class:`Dataset`
            The instance of :class:`Dataset` originally passed to
            :func:`evaluate`.

            .. note::

                If a different dataset is passed, then unexpected
                behavior may occur.

    """


def score_rep(score):

    # If big int
    if len(repr(int(score))) > 5:
        return f'{score:.1f}'

    # Smaller
    if score > 1 or score < -1:
        return f'{score:.2f}'

    # Last case is between 1 and -1
    return f'{score:.4f}'


# @TODO
# 1. Store permutation FI's in object after call
# 2. Add methods for plot feature importance's ?

# TODO - function to easily export saved results in different formats.


def get_non_nan_Xy(X, y):

    # Check for if any missing targets in the test set to skip
    if pd.isnull(y).any():
        non_nan_subjs = y[~pd.isnull(y)].index
        X, y = X.loc[non_nan_subjs], y.loc[non_nan_subjs]

    return X, y


def fi_to_series(fi, feat_names):

    try:
        fi = fi.squeeze()
    except AttributeError:
        pass

    # Base flat case
    if len(fi.shape) == 1:
        return pd.Series(fi, index=feat_names)

    # Categorical case
    # @TODO is there a better way to have this?
    # e.g., maybe explicitly by class value, see self.estimators[0].classes_
    # could put it as another index level.

    series = []
    for class_fi in fi:
        series.append(pd.Series(class_fi, index=feat_names))

    return series


def fis_to_df(fis):

    # Base case - assume that first element is representative
    if isinstance(fis[0], pd.Series):
        return pd.DataFrame(fis)

    # Categorical case
    dfs = []
    for c in range(len(fis[0])):
        dfs.append(pd.DataFrame([fi[c] for fi in fis]))

    return dfs


def mean_no_zeros(df):

    mean = df.mean()
    return mean[mean != 0]


class EvalResults():
    '''This class is returned from calls to :func:`evaluate`,
    and can be used to store information from evaluate, or
    compute additional feature importances. It should typically not be
    initialized by the user.'''

    # Add verbose print
    _print = verbose_print

    def __init__(self, estimator, ps,
                 encoders=None,
                 progress_bar=True,
                 store_preds=False,
                 store_estimators=False,
                 store_timing=False,
                 store_cv=True,
                 store_data_ref=True,
                 eval_verbose=0,
                 progress_loc=None,
                 mute_warnings=False,
                 compare_bars=None):

        # Save base
        self.estimator = estimator
        self.ps = ps
        self.encoders_ = encoders

        # Set if using progress bar
        self._set_progress_bar(progress_bar)

        # If store preds
        self.preds = None
        if store_preds:
            self.preds = {}

        # If store estimator
        self.estimators = None
        if store_estimators:
            self.estimators = []

        # If store timing
        self.timing = None
        if store_timing:
            self.timing = {'fit': [], 'score': []}

        # Keep track of if to store cv
        self._store_cv = store_cv
        if not self._store_cv:
            self.cv = None

        # If store reference to data
        self._store_data_ref = store_data_ref
        if not self._store_data_ref:
            self._dataset = None

        self.progress_loc = progress_loc
        self.verbose = eval_verbose
        self.mute_warnings = mute_warnings
        self.compare_bars = compare_bars
    @property
    def estimator(self):
        '''This parameter stores the passed saved, unfitted estimator
        used in this evaluation. This is a sklearn style estimator obtained
        from :func:`get_estimator`.'''

        return self._estimator

    @estimator.setter
    def estimator(self, estimator):
        self._estimator = estimator

    @property
    def mean_scores(self):
        '''This parameter stores the mean scores as
        a dictionary of values, where each dictionary
        is indexed by the name of the scorer, and the dictionary value
        is the mean score for that scorer.'''
        return self._mean_scores

    @mean_scores.setter
    def mean_scores(self, mean_scores):
        self._mean_scores = mean_scores

    @property
    def std_scores(self):
        '''This parameter stores the standard deviation scores as
        a dictionary of values, where each dictionary
        is indexed by the name of the scorer, and value
        contains the standard deviation across evaluation folds
        for that scorer.

        The default scorer key stores the micro standard
        deviation, but in the case that macro standard deviation differs,
        i.e., in the case of multiple repeats in an evaluation, then
        a separate macro standard deviation will be stored under
        the name of the scorer with _macro appended to the key.

        For example if a 3-fold twice repeated evaluation was
        run, with just r2 as the scorer, this parameter might
        look something like:

        ::

            self.std_scores = {'r2': .5, 'r2_macro': .01}

        '''
        return self._std_scores

    @std_scores.setter
    def std_scores(self, std_scores):
        self._std_scores = std_scores

    @property
    def weighted_mean_scores(self):
        '''This property stores the mean scores
        across evaluation folds (simmilar to
        :data:`mean_scores<EvalResults.mean_scores>`),
        but weighted by the
        number of subjects / datapoints in each fold.

        It is scores as a dictionary indexed by the name
        of the scorer as the key, where values are
        the weighted mean score.
        '''
        return self._weighted_mean_scores

    @weighted_mean_scores.setter
    def weighted_mean_scores(self, weighted_mean_scores):
        self._weighted_mean_scores = weighted_mean_scores

    @property
    def scores(self):
        '''This property stores the scores for
        each scorer as a dictionary of lists, where
        the keys are the names of the scorer and the list
        represents the score obtained for each fold, where each
        index corresponds to to a fold of cross validation.'''
        return self._scores

    @scores.setter
    def scores(self, scores):
        self._scores = scores

    @property
    def score(self):
        '''This property represents
        a quick helper for accessing the mean scores
        of whatever the first scorer is (in the case of
        multiple scorers).
        '''

        first_scorer = list(self.scores)[0]
        if len(self.scores[first_scorer]) == 0:
            return None

        return np.mean(self.scores[first_scorer])

    @property
    def ps(self):
        '''A saved and pre-processed version of the problem_spec
        used (with any extra_params applied) when running this
        instance of Evaluator.'''
        return self._ps

    @ps.setter
    def ps(self, ps):
        self._ps = ps

    @property
    def feat_names(self):
        '''The features names corresponding to any measures of
        feature importance, stored as a list of lists, where the top
        level list represents each fold of cross validation.

        This parameter may be especially useful when pipeline
        objects such as transformers or feature selectors are used
        as these can drastically change the features passed to an
        eventual model.

        The values stored here may change
        based on the passed
        value of the `decode_feat_names` parameter from
        :func:`evaluate`.

        For example the feat_names from a 3-fold cross-validation
        with input features ['feat1', 'feat2', 'feat3'] with
        feature selection as a piece of the pipeline may look like:

        ::

            self.feat_names = [['feat1', 'feat2'],
                               ['feat2', 'feat3'],
                               ['feat1', 'feat2']]

        '''
        return self._feat_names

    @feat_names.setter
    def feat_names(self, feat_names):
        self._feat_names = feat_names

    @property
    def val_subjects(self):
        '''| This parameter stores the validation subjects / index
          used in every fold of the cross-validation. It can be
          useful in some cases
          to check to see exactly what cross-validation was applied.

        | This parameter
          differs from
          :data:`all_val_subjects<EvalResults.all_val_subjects>`
          in that even subjects with missing target values are not included.

        '''
        return self._val_subjects

    @val_subjects.setter
    def val_subjects(self, val_subjects):
        self._val_subjects = val_subjects

    @property
    def train_subjects(self):
        '''| This parameter stores the training subjects / index
          used in every fold of the cross-validation. It can be
          useful in some cases to check to see exactly what
          cross-validation was applied.

        | This parameter
          differs from
          :data:`all_train_subjects<EvalResults.all_train_subjects>`
          in that even subjects with missing target values are not included.

        '''
        return self._train_subjects

    @train_subjects.setter
    def train_subjects(self, train_subjects):
        self._train_subjects = train_subjects

    @property
    def all_val_subjects(self):
        '''| This parameter stores the validation subjects / index
          used in every fold of the cross-validation.

        | This parameter
          differs from :data:`val_subjects<EvalResults.val_subjects>`
          in that even subjects with missing target values are included.

        '''
        return self._all_val_subjects

    @all_val_subjects.setter
    def all_val_subjects(self, all_val_subjects):
        self._all_val_subjects = all_val_subjects

    @property
    def all_train_subjects(self):
        '''| This parameter stores the training subjects / index
          used in every fold of the cross-validation.

        | This parameter
          differs from :data:`train_subjects<EvalResults.train_subjects>`
          in that even subjects with missing target values are included.
        '''
        return self._all_train_subjects

    @all_train_subjects.setter
    def all_train_subjects(self, all_train_subjects):
        self._all_train_subjects = all_train_subjects

    @property
    def n_subjects(self):
        '''A quicker helper property to get
        the sum of the length of :data:`train_subjects<EvalResults.train_subjects>`
        and :data:`val_subjects<EvalResults.val_subjects>`. If this number varies by fold,
        it will be set to None.

        This number is supposed to represent the number of subjects with non NaN targets
        used in the training and testing. 
        '''

        lens = [len(self.train_subjects[i]) + len(self.val_subjects[i]) for i in range(len(self.train_subjects))]

        if len(set(lens)) == 1:
            return lens[0]
        return None

    @property
    def n_folds(self):
        '''A quicker helper property to get the number of CV folds
        this object was evaluated with.
        '''
        # Just use len of train subjects as proxy for n_folds
        return len(self.train_subjects)

    @property
    def timing(self):
        '''This property stores information on
        the fit and scoring times, if requested by the
        original call to :func:`evaluate`.
        This parameter is a dictionary with two keys,
        'fit' and 'score'.
        Each key stores the time in seconds as a list of
        values for each of the evaluation folds.
        '''
        return self._timing

    @timing.setter
    def timing(self, timing):
        self._timing = timing

    @property
    def mean_timing(self):
        '''This property stores information on
        the fit and scoring times, if requested by the
        original call to :func:`evaluate`.
        This parameter is a dictionary with two keys,
        'fit' and 'score'.
        Each key stores the mean time in seconds across folds.
        '''
        return self._mean_timing

    @mean_timing.setter
    def mean_timing(self, mean_timing):
        self._mean_timing = mean_timing

    @property
    def preds(self):
        '''If the parameter `store_preds` is set to True when
        calling :func:`evaluate`, then this parameter will store the
        predictions from every evaluate fold.

        The parameter preds is a dictionary, where raw predictions made
        can be accessed by the key 'predict'. Values are stored as list
        corresponding to each evaluation fold.

        In the case where other predict-like functions are available, e.g.,
        in the case of a binary problem, where it may be desirable to
        see the predicted probability, then the those predictions
        will be made available under the name of the underlying predict
        function. In this case, that is self.preds['predict_proba'].
        It will also store results from 'predict' as well.

        self.preds also will store under 'y_true' a list, where
        each element of the list corresponds to the corresponding
        true target values for the predictions made.
        '''

        return self._preds

    @preds.setter
    def preds(self, preds):
        self._preds = preds

    @property
    def estimators(self):
        '''If the parameter `store_estimators` is set to True when
        calling :func:`evaluate`, then this parameter will store the fitted
        estimator in a list. Where each element of the list corresponds to one
        of the validation folds.

        For example to access the fitted estimator from this first
        fold ::

            first_est = self.estimators[0]

        '''
        return self._estimators

    @estimators.setter
    def estimators(self, estimators):
        self._estimators = estimators

    @property
    def cv(self):
        '''If set to store CV is true, a deepcopy of the
        passed cv splitter will be stored'''

        try:
            return self._cv
        except AttributeError:
            return None

    @cv.setter
    def cv(self, cv):
        self._cv = cv

    def _set_progress_bar(self, progress_bar):
        '''Sets correct bar type based on if in notebook or not.'''

        self.progress_bar = get_progress_bar(progress_bar)

    def _eval(self, X, y, cv, dataset=None):

        # Optionally store reference to dataset
        if self._store_data_ref:
            self._dataset = dataset.copy(deep=False)

        # If verbose is lower than -1,
        # then don't show any warnings no matter the source.
        # or mute warnings flag set.
        if self.verbose < -1 or self.mute_warnings:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self._evaluate(X, y, cv)

        # Otherwise, base behavior
        else:
            self._evaluate(X, y, cv)

    def _evaluate(self, X, y, cv):
        '''cv is passed as raw index, X and y as dataframes.'''

        # Store a deep copy of cv if requested
        if self._store_cv:
            self.cv = deepcopy(cv)

        # Compute and warn about num nan targets
        n_nan_targets = pd.isnull(y).sum()
        if n_nan_targets > 0:
            self._print('Warning: There are', str(n_nan_targets) + ' missing',
                        'targets passed to evaluate. Subjects with missing',
                        'target values will be skipped during training and '
                        'scoring.')

            if self.preds is not None:
                self._print('Predictions will still be made for any',
                            'subjects with missing values in',
                            'any validation folds.')

        # Verbose info
        self._print('Predicting target =', str(self.ps.target), level=1)
        self._print('Using problem_type =', str(self.ps.problem_type), level=1)
        self._print('Using scope =', str(self.ps.scope),
                    '(defining a total of', str(X.shape[1]),
                    'features).', level=1)
        self._print(f'Evaluating {len(X)} total data points.', level=1)

        # Init scores as dictionary of lists
        self.scores = {scorer_str: [] for scorer_str in self.ps.scorer}

        # Save train and test subjs
        self.all_train_subjects, self.all_val_subjects = [], []
        self.train_subjects, self.val_subjects = [], []

        # Save final feat names
        self.feat_names = []

        # Init progress bar / save and compute fold info from cv
        progress_bars = self._init_progress_bars(cv)

        self._print('Using CV: ', cv,
                    'to generate evaluation splits.', level=2)
        self._print(level=1)

        # Run each split
        for train_inds, val_inds in cv.split(X, y):

            # Eval
            self._eval_fold(X.iloc[train_inds], y.iloc[train_inds],
                            X.iloc[val_inds], y.iloc[val_inds])

            # Increment progress bars
            progress_bars = self._incr_progress_bars(progress_bars)
            self._incr_compare_bar()

        # Clean up progress bars
        self._finish_progress_bars(progress_bars)

        # Compute and score mean and stds
        self._compute_summary_scores()

    def _init_progress_bars(self, cv):

        # Passed cv should have n_repeats param - save in class
        self.n_repeats_ = 1
        if hasattr(cv, 'n_repeats'):
            self.n_repeats_ = cv.n_repeats

        # Passed cv should already be sklearn style
        n_all_splits = cv.get_n_splits()

        # Compute number of splits per repeat
        self.n_splits_ = n_all_splits
        if self.n_repeats_ > 1:
            self.n_splits_ = int(n_all_splits / self.n_repeats_)

        # Skip if no progress bar
        if self.progress_bar is None:
            return []

        # If passed compare bars is int, init top level bar
        if isinstance(self.compare_bars, int):

            # Init and set as new
            compare_bar = self.progress_bar(total=self.compare_bars,
                                            desc='Compare', dynamic_ncols=True)
            self.compare_bars = [compare_bar]

        # If already init'ed
        elif isinstance(self.compare_bars, list):

            # Return all but last compare bar
            return self.compare_bars[:-1]

        bars = []

        # If 1 repeat, then just folds progress bar
        if self.n_repeats_ == 1:
            folds_bar = self.progress_bar(total=self.n_splits_, desc='Folds',
                                          dynamic_ncols=True)
            bars = [folds_bar]

        # Otherwise folds and repeats bars - init repeats bar first, so on top
        else:
            repeats_bar = self.progress_bar(total=self.n_repeats_,
                                            desc='Repeats', dynamic_ncols=True)
            folds_bar = self.progress_bar(total=self.n_splits_, desc='Folds',
                                          dynamic_ncols=True)
            bars = [folds_bar, repeats_bar]

        # If compare bars was init'ed this run
        if self.compare_bars is not None:
            self.compare_bars = bars + self.compare_bars

        return bars

    def _incr_progress_bars(self, progress_bars):

        # Skip if not requested
        if self.progress_bar is None:
            return []

        # Increment folds bar
        folds_bar = progress_bars[0]
        folds_bar.n += 1

        # Calculate estimate for this fold so far, and set
        first_scorer = list(self.scores)[0]
        fold_mean = np.mean(self.scores[first_scorer][-folds_bar.n:])
        folds_bar.desc = f'Folds ({score_rep(fold_mean)})'

        # If just folds bar update and return
        if len(progress_bars) == 1:
            _refresh_bar(folds_bar)
            return [folds_bar]

        # Increment partially repeats bar
        repeats_bar = progress_bars[1]
        repeats_bar.n += (1 / self.n_splits_)
        repeats_bar.n = round(repeats_bar.n, 2)

        # Set estimate score from all avaliable
        repeats_bar.desc = f'Repeats ({score_rep(self.score)})'

        # If both, check to see if n_repeats should be
        # rounded, and folds bar reset to 0, and reset descr
        if folds_bar.n == self.n_splits_:
            folds_bar.n = 0
            folds_bar.desc = 'Folds'
            repeats_bar.n = round(repeats_bar.n)

            # If end, set to full
            if repeats_bar.n == self.n_repeats_:
                folds_bar.n = self.n_splits_

        # Update and  then return
        _refresh_bar([folds_bar, repeats_bar])
        return [folds_bar, repeats_bar]

    def _incr_compare_bar(self):

        if self.compare_bars is None:
            return

        amt = 1 / (self.n_repeats_ * self.n_splits_)

        self.compare_bars[-1].n += amt
        self.compare_bars[-1].n = round(self.compare_bars[-1].n, 2)

        _refresh_bar(self.compare_bars[-1])

    def _finish_progress_bars(self, progress_bars):

        # Refresh label on repeats (if any)
        if len(progress_bars) == 2:
            progress_bars[1].desc = 'Repeats'
            _refresh_bar(progress_bars[1])

        # Refresh label on folds
        if len(progress_bars) > 0:
            progress_bars[0].desc = 'Folds'
            _refresh_bar(progress_bars[0])

        # Close progress bars
        if self.compare_bars is None:
            for p_bar in progress_bars:
                p_bar.close()

            return

        # Otherwise compare bars case, reset
        _refresh_bar(progress_bars, n=0)

        # Increment w/ round and refresh compare
        self.compare_bars[-1].n = round(self.compare_bars[-1].n)
        _refresh_bar(self.compare_bars[-1])

        return

    def _eval_fold(self, X_tr, y_tr, X_val, y_val):

        # Get clone of estimator to fit
        estimator_ = clone(self.estimator)

        # Save all train and val inds before missing targets removed
        self.all_train_subjects.append(X_tr.index)
        self.all_val_subjects.append(X_val.index)

        # Check for if any missing targets, if so - skip
        # those subjects.
        X_tr, y_tr = get_non_nan_Xy(X_tr, y_tr)
        X_val_c, y_val_c = get_non_nan_Xy(X_val, y_val)

        # Keep track of subjects in folds - where a subject is not included
        # in the train or val fold if has NaN target
        self.train_subjects.append(X_tr.index)
        self.val_subjects.append(X_val_c.index)

        # Add extra to verbose print if any skipped for NaN
        tr_extra, val_extra = '', ''

        dif_tr = len(self.all_train_subjects[-1]) -\
            len(self.train_subjects[-1])
        dif_val = len(self.all_val_subjects[-1]) -\
            len(self.val_subjects[-1])

        if dif_tr != 0:
            tr_extra = f' (skipped {dif_tr} NaN targets)'
        if dif_val != 0:
            val_extra = f' (skipped {dif_val} NaN targets)'

        # Print info on sizes
        self._print(f'Training Set: {X_tr.shape}{tr_extra}', level=1)
        self._print(f'Validation Set: {X_val_c.shape}{val_extra}', level=1)

        # Fit estimator_, passing as arrays, and with train data index
        start_time = time.time()

        estimator_.fit(X=X_tr, y=np.array(y_tr))
        fit_time = time.time() - start_time
        self._print(f'Fit fold in {fit_time:.1f} seconds.', level=1)

        # Score estimator
        start_time = time.time()
        self._score_estimator(estimator_, X_val_c, y_val_c)
        score_time = time.time() - start_time

        # Store timing if requested
        if self.timing is not None:
            self.timing['fit'].append(fit_time)
            self.timing['score'].append(score_time)

        # Save preds - pass full val with NaN targets
        self._save_preds(estimator_, X_val, y_val)

        # Get and save final transformed feat names
        # Feat names w/ nested model applied ~
        self.feat_names.append(
            estimator_.transform_feat_names(X_tr,
                                            encoders=self.encoders_,
                                            nested_model=True))

        # If store estimators, save in self.estimators
        if self.estimators is not None:
            self.estimators.append(estimator_)

    def _score_estimator(self, estimator_, X_val, y_val):
        
        # Use multi-metric scorer here - handles not repeating calls to
        # predict / predict proba, ect... - can safely wrap even single metrics
        scorers = _MultimetricScorer(**self.ps.scorer)
        scores = scorers(estimator_, X_val, np.array(y_val))

        # Append each to scores, keeps track per fold
        for scorer_str in self.scores:

            score = scores[scorer_str]
            self.scores[scorer_str].append(score)

            # Optional verbose
            self._print(f'{scorer_str}: {score_rep(score)}', level=1)

        # Spacing for nice looking output
        self._print(level=1)

    def _save_preds(self, estimator, X_val, y_val):

        if self.preds is None:
            return

        self._print('Saving predictions on validation set.', level=2)

        for predict_func in ['predict', 'predict_proba', 'decision_function']:

            # Get preds, skip if estimator doesn't have predict func
            try:
                preds = getattr(estimator, predict_func)(X_val)
            except AttributeError:
                continue

            # Add to preds dict if estimator has predict func
            try:
                self.preds[predict_func].append(preds)
            except KeyError:
                self.preds[predict_func] = [preds]

        # Add y_true
        try:
            self.preds['y_true'].append(np.array(y_val))
        except KeyError:
            self.preds['y_true'] = [np.array(y_val)]

    def _compute_summary_scores(self):

        self._print('Computing summary scores.', level=2)

        self.mean_scores, self.std_scores = {}, {}
        self.weighted_mean_scores = {}

        for scorer_key in self.scores:

            # Save mean under same name
            scores = self.scores[scorer_key]
            self.mean_scores[scorer_key] = np.mean(scores)

            # Compute scores weighted by number of subjs
            # Use val_subjects without NaN targets
            weights = [len(self.val_subjects[i])
                       for i in range(len(self.val_subjects))]
            self.weighted_mean_scores[scorer_key] =\
                np.average(scores, weights=weights)

            # Compute and add base micro std
            self.std_scores[scorer_key] = np.std(scores)

            # If more than 1 repeat, add the macro std
            if self.n_repeats_ > 1:
                scores = np.reshape(scores,
                                    (self.n_repeats_, self.n_splits_))
                self.std_scores[scorer_key + '_macro'] =\
                    np.std(np.mean(scores, axis=1))

        # Add mean timing
        if self.timing is not None:
            self.mean_timing = {}

            for time_key in self.timing:
                self.mean_timing[time_key] = np.mean(self.timing[time_key])

    def get_preds_dfs(self, drop_nan_targets=False):
        '''This function can be used to return the raw predictions
        made during evaluation as a list of pandas Dataframes.

        Parameters
        ------------
        drop_nan_targets : bool, optional
            If False (default), then this method will return the
            DataFrame of predictions including targets
            with NaN. To skip these, e.g., in this case
            of plotting against ground truth or computing
            new metrics, set to True.

            ::

                default = False

        Returns
        ---------
        dfs : list of pandas.DataFrame
            list of dataframe's per fold, where each DataFrame
            contains predictions made.
        '''

        dfs = []

        # For each fold
        for fold_indx in range(len(self.all_val_subjects)):

            # Init df
            df = pd.DataFrame(index=self.all_val_subjects[fold_indx])

            # Add each predict type as a column
            for predict_type in self.preds:
                ps = self.preds[predict_type][fold_indx]

                # Either float or multi-class case
                if isinstance(ps[0], (float, np.floating)):
                    df[predict_type] = ps

                else:
                    for cls in range(len(ps[0])):
                        df[predict_type + '_' + str(cls)] = ps[:, cls]

            # Drop nan-cols if not requested
            if drop_nan_targets:
                nan_targets = df[df['y_true'].isna()].index
                df = df.drop(nan_targets)

            # Add to by fold list
            dfs.append(df)

        return dfs

    def _get_display_name(self):
        return str(self.__class__.__name__)

    def __repr__(self):
        rep = self._get_display_name() + '\n'
        rep += '------------\n'

        # Add scores + means pretty rep
        for key in self.mean_scores:
            rep += f'{key}: {score_rep(self.mean_scores[key])} '
            rep += f'± {score_rep(self.std_scores[key])}\n'
        rep += '\n'

        # Show available saved attrs
        saved_attrs = []
        avaliable_methods = ['to_pickle', 'compare']

        if self.estimators is not None:
            saved_attrs.append('estimators')
            avaliable_methods.append('get_X_transform_df')
            avaliable_methods.append('get_inverse_fis')
            avaliable_methods.append('run_permutation_test')

        if self.preds is not None:
            saved_attrs.append('preds')
            avaliable_methods.append('get_preds_dfs')
            avaliable_methods.append('subset_by')
        if self.timing is not None:
            saved_attrs.append('timing')

        saved_attrs += ['estimator', 'train_subjects', 'val_subjects',
                        'feat_names', 'ps',
                        'mean_scores', 'std_scores',
                        'weighted_mean_scores', 'scores']

        # Only show if different
        ati_len = len(sum([list(e) for e in self.all_train_subjects], []))
        ti_len = len(sum([list(e) for e in self.train_subjects], []))
        if ati_len != ti_len:
            saved_attrs.append('all_train_subjects')

        avi_len = len(sum([list(e) for e in self.all_val_subjects], []))
        vi_len = len(sum([list(e) for e in self.val_subjects], []))
        if avi_len != vi_len:
            saved_attrs.append('all_val_subjects')

        if self.estimators is not None:

            # Either or
            if self.feature_importances_ is not None:
                saved_attrs += ['fis_', 'feature_importances_']
                avaliable_methods += ['get_fis', 'get_feature_importances']
            elif self.coef_ is not None:
                saved_attrs += ['fis_', 'coef_']
                avaliable_methods += ['get_fis', 'get_coef_']

            avaliable_methods.append('permutation_importance')

        if self._store_cv:
            saved_attrs += ['cv']

        rep += 'Saved Attributes: ' + repr(saved_attrs) + '\n\n'
        rep += 'Available Methods: ' + repr(avaliable_methods) + '\n\n'

        # Use custom display str, no need to show scorer.
        rep += 'Evaluated With:\n'
        rep += self.ps._get_display_str(show_scorer=False) + '\n'

        return rep

    def _estimators_check(self):

        if self.estimators is None:
            raise RuntimeError('This method is not available unless '
                               'evaluate is run with store_estimators=True!')

    def _dataset_check(self, dataset=None):

        # If dataset not passed, try to use saved dataset ref
        if dataset is None:
            
            # Check for no saved
            if not hasattr(self, '_dataset') or getattr(self, '_dataset') is None:
                raise RuntimeError('No saved reference dataset, you must pass a dataset to use.')

            # Use saved
            dataset = self._dataset

        return dataset

    @property
    def feature_importances_(self):
        '''This property stores the mean values
        across fitted estimators assuming each fitted estimator
        has a non empty `feature_importances_` attribute.'''

        self._estimators_check()
        return get_mean_fis(self.estimators, 'feature_importances_')

    def get_feature_importances(self):
        '''This function returns each `feature_importances_`
        value across fitted estimators. If None have this parameter,
        it will return a list of None.

        Returns
        --------
        feature_importances : list
            A list of `feature_importances_` where each element
            in the list refers to a fold from the evaluation.
        '''

        self._estimators_check()
        return [estimator.feature_importances_
                for estimator in self.estimators]

    @property
    def coef_(self):
        '''This attribute represents the mean `coef_` as
        a numpy array across all folds. This parameter will only
        be available if all estimators have a non null `coef_` parameter
        and each returns the same shape. See `fis_` for a more flexible
        version of this parameter that can handle when there
        are differing numbers of features.'''

        self._estimators_check()
        return get_mean_fis(self.estimators, 'coef_')

    def get_coefs(self):
        '''This function returns each `coef_`
        value across fitted estimators. If None have this parameter,
        it will return a list of None.

        Returns
        --------
        coefs : list
            A list of `coef_` where each element
            in the list refers to a fold from the evaluation.
        '''

        self._estimators_check()
        return [estimator.coef_
                for estimator in self.estimators]

    @property
    def fis_(self):
        '''This property stores the mean value
        across each fold of the CV for either the `coef_`
        or `feature_importance_` parameter.

        Warnings
        ---------
        If a feature is not present in all folds,
        then it's mean value will be computed from only the
        folds in which it was present.

        When using transformers, for example one hot encoder,
        since the encoding is done on the fly, there is no
        guarantee that 'one hot encoder category_1' is actually
        the same category 1 across folds.

        If for some reason some folds have a model with feature
        importances and other `coef_` they will still all be averaged
        together, so make sure that this parameter is only used when
        all of the underlying models across folds should have comparable
        feature importances.
        '''

        # @TODO incoperate in information about the original
        # class names here // maybe in specific objects like
        # OneHotEncoder.

        self._estimators_check()

        # Grab fis as Dataframe or list of
        fis = self.get_fis()

        # Base case
        if isinstance(fis, pd.DataFrame):
            return fis.mean()

        # Categorical case
        return [fi.mean() for fi in fis]

    def _get_base_fis_list(self):

        self._estimators_check()

        coefs = self.get_coefs()
        feature_importances = self.get_feature_importances()

        fis = []
        for coef, fi, feat_names in zip(coefs, feature_importances,
                                        self.feat_names):
            if coef is not None:
                fis.append(fi_to_series(coef, feat_names))
            elif fi is not None:
                fis.append(fi_to_series(fi, feat_names))
            else:
                fis.append(None)

        return fis

    def get_fis(self, mean=False, abs=False):
        '''This method will return a pandas DataFrame with
        each row a fold, and each column a feature if
        the underlying model supported either the `coef_`
        or `feature_importance_` parameters.

        In the case that the underlying feature importances
        or `coefs_` are not flat, e.g., in the case
        of a one versus rest categorical model, then a list
        multiple DataFrames will be returned, one for each class.
        The order of the list will correspond to the order of classes.

        Parameters
        -----------
        mean : bool, optional
            If True, return the mean value
            across evaluation folds as a pandas Series.
            Any features with a mean value of 0 will
            also be excluded. Otherwise, if default
            of False, return raw values for each fold
            as a Dataframe.

            ::

                default = False

        abs : bool, optional
            If the feature importances
            should be absolute values
            or not.

            ::

                default = False

        Returns
        --------
        fis : pandas DataFrame or Series
            Assuming mean=False, the
            a pandas DataFrame where each row contains the
            feature importances from an evaluation fold (unless the underlying
            feature importances are categorical, in which a list of DataFrames
            will be returned.)

            If mean=True, then a pandas Series (or in the case of
            underlying categorical feature importances, list of)
            will be returned, with the mean value from each fold
            and all features with a value of 0 excluded.

            Note: To get the mean values without zero's excluded,
            just call .mean() on the result of this method
            with mean=False.


        '''

        fis = self._get_base_fis_list()
        base = fis_to_df(fis)

        # Proc. abs arg
        if abs:
            if isinstance(base, list):
                base = [b.abs() for b in base]
            else:
                base = base.abs()

        # If not mean, return as is
        if not mean:
            return base

        # Categorical mean case
        if isinstance(base, list):
            return [mean_no_zeros(b) for b in base]

        # Base mean case
        return mean_no_zeros(base)

    def get_inverse_fis(self, fis=None):
        '''Try to inverse transform stored
        feature importances (either beta weights or
        automatically calculated feature importances)
        to their original space.

        .. warning::

            If there are any underlying non-recoverable
            transformations in the pipeline, this method
            will fail! For example, if a PCA was applied,
            then a reverse transformation cannot be computed.

        This method can be especially helpful when using :class:`Loader`.

        Returns
        -------
        inverse_fis : list of pandas Series
            | The inverse feature importances will be returned
              as a list, where each index of the list refers to
              a fold of the cross-validation, and each element
              of the list is either a pandas Series or a list
              of pandas Series (in the case of a categorical
              problem type where separate feature importances
              were calculated for each class).

            | If a :class:`Loader` was used, the returned Series
              may contain multi-dimensional arrays instead of scalar
              values, representing feature importances as transformed
              back into the original loaded space / shape.
        '''

        # As list of series or list of list of series
        if fis is None:        
            fis = self._get_base_fis_list()

        # If passed in df format, convert first
        # Drop any NaN also ~
        # @ TODO handle categorical case ... 
        elif isinstance(fis, pd.DataFrame):
            fis = [fis.loc[i].dropna() for i in range(len(fis))]

        # Otherwise, assumes passed
        inv_trans_fis = []
        for i, fi in enumerate(fis):

            # The estimator for this fold
            estimator = self.estimators[i]

            # Non-categorical case
            if isinstance(fi, pd.Series):
                inv_trans_fis.append(
                    estimator.inverse_transform_fis(fi))

            # Categorical case
            else:
                cat_inv_fis =\
                    [estimator.inverse_transform_fis(f) for f in fi]
                inv_trans_fis.append(cat_inv_fis)

        return inv_trans_fis

    def _get_val_fold_Xy(self, estimator, X_df,
                         y_df, fold, just_model=True,
                         nested_model=True):

        # Get the X and y df's - assume self.val_subjects stores
        # only subjects with non nan target variables
        X_val_df = X_df.loc[self.val_subjects[fold]]
        y_val_df = y_df.loc[self.val_subjects[fold]]

        # Base as array, and all feat names
        X_trans, feat_names = np.array(X_val_df), list(X_val_df)

        # Transform the X df, casts to array if just_model.
        if just_model:

            # Calculate corresponding feat names
            # with or without nested_model
            feat_names =\
                estimator.transform_feat_names(feat_names,
                                               encoders=self.encoders_,
                                               nested_model=nested_model)

            # Also calculate X_trans, with and without nested model
            X_trans = estimator.transform(X_trans,
                                          transform_index=X_val_df.index,
                                          nested_model=nested_model)

            # If nested model, then we need to make sure to
            # grab the nested final estimator
            if nested_model:
                estimator = estimator._nested_final_estimator

            # Otherwise use the one deep final estimator
            else:
                estimator = estimator._final_estimator

        return estimator, X_trans, np.array(y_val_df), feat_names

    @doc(dataset=_base_docs['dataset'])
    def permutation_importance(self, dataset=None,
                               n_repeats=10, scorer='default',
                               just_model=True, nested_model=True,
                               return_as='dfs', n_jobs=1,
                               random_state='default'):
        '''This function computes the permutation feature importances
        from the base scikit-learn function
        :func:`sklearn.inspection.permutation_importance`

        Parameters
        -----------
        {dataset}

            | If left as default=None, then will try to use
              a shallow copy of the dataset passed to the original
              evaluate call (assuming evaluate was run with store_data_ref=True).

            ::

                default = None

        n_repeats : int, optional
            The number of times to randomly permute each feature.

            ::

                default = 10

        scorer : sklearn-style scoring, optional
            Scorer to use. It can be a single sklearn style str,
            or a callable.

            If left as 'default' will use the first scorer defined when
            evaluating the underlying estimator.

            ::

                default = 'default'

        just_model : bool, optional
            When set to true, the permutation feature importances
            will be computed using the final set of transformed features
            as passed when fitting the base model. This is reccomended
            behavior because it means that the features do not need to
            be re-transformed through the full pipeline to evaluate each
            feature. If set to False, will permute the features in the
            original feature space (which may be useful in some context).

            ::

                default = True

        nested_model : bool, optional
            In the case that `just_model` is set to True, there exists
            in some cases the further option to use an even more transformed
            set of features. For example, in the case where in the main pipeline
            the final estimator is another pipeline, there could be more static
            transformations applied in this second pipeline. If `nested_model` is
            set to True, then it will attempt to apply these further nested
            transformations in the same way as with just_model, feeding in
            eventually an even further transformed set of features and even more
            specific final estimator when calculating the permutation feature
            importances.

            By default, this value is True, so the calculated
            feature importances here will correspond to the
            saved `self.feat_names` in this object.

            ::

                default = True

        return_as : ['dfs', 'raw'], optional
            This parameter controls if calculated permutation
            feature importances should be returned as a DataFrame
            with column names as the corresponding feature names,
            or if it should be returned as a list with the raw
            output from each fold, e.g., sklearn Batch's with
            parameters 'importances_mean', 'importances_std'
            and 'importances'.

            If return as DataFrame is requested, then
            'importances_mean' and 'importances_std'
            will be returned, but not the raw 'importances'.

            ::

                default = 'dfs'


        n_jobs : int, optional
            The number of jobs to use for this function. Note
            that if the underlying estimator supports multiple jobs
            during inference (predicting), and the original
            problem_spec was set with multiple n_jobs then that original
            behavior will still hold, and you may wish to keep this
            parameter as 1. On the otherhand, if the base estimator
            does not use multiple jobs, passing a higher value here
            could greatly speed up computation.

            ::

                default = 1

        random_state : int, 'default' or None, optional
            Pseudo-random number generator to control the permutations
            of each feature.
            If left as 'default' then use the random state defined
            during the initial evaluation of the model. Otherwise, you may
            pass an int for a different fixed random state or None
            for explicitly no
            random state.

            ::

                default = 'default'
        '''

        # @TODO in case of just_model = False, won't pass along
        # transform_index correctly to scorer.

        from sklearn.inspection import permutation_importance

        # Check dataset
        dataset = self._dataset_check(dataset)

        # Check estimators
        self._estimators_check()

        # If default scorer, take the first one
        if scorer == 'default':
            first = list(self.ps.scorer)[0]
            scorer = self.ps.scorer[first]
            self._print('Using scorer:', first, level=1)

        # If default random_state use the one saved in
        # original problem spec.
        if random_state == 'default':
            random_state = self.ps.random_state

        # Get X and y from saved problem spec
        X, y = dataset.get_Xy(self.ps)

        # For each estimator
        all_fis, all_feat_names = [], []
        for fold, estimator in enumerate(self.estimators):

            # Get correct estimator, X_val, y_val and feat_names
            estimator, X_val, y_val, feat_names =\
                self._get_val_fold_Xy(estimator, X_df=X, y_df=y,
                                      fold=fold, just_model=just_model,
                                      nested_model=nested_model)
            all_feat_names.append(feat_names)

            # Run the sklearn feature importances.
            fis = permutation_importance(estimator, X_val, y_val,
                                         scoring=scorer, n_repeats=n_repeats,
                                         n_jobs=n_jobs,
                                         random_state=random_state)
            # Add to all fis
            all_fis.append(fis)

        # If raw, return as raw
        if return_as == 'raw':
            return all_fis

        # Otherwise, use return df
        mean_series, std_series = [], []
        for fis, feat_names in zip(all_fis, all_feat_names):
            mean_series.append(
                fi_to_series(fis['importances_mean'], feat_names))
            std_series.append(
                fi_to_series(fis['importances_std'], feat_names))

        # Return as sklearn bunch of DataFrames
        return Bunch(importances_mean=fis_to_df(mean_series),
                     importances_std=fis_to_df(std_series))

    @doc(dataset=_base_docs['dataset'])
    def get_X_transform_df(self, dataset=None, fold=0, subjects='tr',
                           nested_model=True, trans_y=False):
        '''This method is used as a helper for getting the transformed
        input data for one of the saved models run during evaluate.

        Parameters
        -----------
        {dataset}
        
            | If left as default=None, then will try to use
              a shallow copy of the dataset passed to the original
              evaluate call (assuming evaluate was run with store_data_ref=True).

            ::

                default = None

        fold : int, optional
            The corresponding fold of the trained
            estimator to use.

        subjects : 'tr', 'val' or :ref:`Subjects`, optional
            The subjects data in which to return. As
            either special strings 'tr' for train subjects
            in the corresponding fold. Special str
            'val' for the validation subjects in the
            selected for or lastly any valid
            :ref:`Subjects` style input.

            ::

                default = 'tr'

        nested_model : bool, optional
            In the case where the final estimator is itself
            a nested pipeline, the user may want to apply any of
            those transformations too. If passed as True, then these
            transformed features will apply to the fitted estimators
            `self._nested_final_estimator`, which may not be the same
            a the base `self._final_estimator`.

            Note: In the case of some complex nested ensemble, this method
            may break.

            ::

                default = False

        trans_y : bool, optional
            Can optionally try to tranform y along with X,
            this is experimental designed to work with
            samplers. Default is False, as not 100% confident
            will work correctly in all cases.

            default = False


        Returns
        ----------
        X_trans_df : pandas DataFrame
            The transformed features in a DataFrame,
            according to the saved estimator from a fold,
            for the specified subjects.

            If kept as the default of subjects == 'tr',
            then these represent the feature values as
            passed to trained the actual model component
            of the pipeline.
        '''

        # Check dataset
        dataset = self._dataset_check(dataset)

        # This method requires that the fitted estimators
        # were saved.
        self._estimators_check()

        # Estimator from the fold
        estimator = self.estimators[fold]

        if subjects == 'tr':
            subjects = self.train_subjects[fold]
        elif subjects == 'val':
            subjects = self.val_subjects[fold]

        # Get as X dataframe, since passing df don't need to worry
        # about transform_index
        X_fold, y_fold = dataset.get_Xy(problem_spec=self.ps,
                                        subjects=subjects)

        # Get feature names from fold
        if nested_model:
            feat_names = self.feat_names[fold]

        # If not using nested_model, need to re-calculate
        else:
            feat_names = estimator.transform_feat_names(X_fold,
                                                        encoders=self.encoders_,
                                                        nested_model=False)

        # Trans y experimental case
        if trans_y:
            X_trans_fold, y_trans_fold, transform_index =\
                estimator.transform(X_fold, nested_model=nested_model, trans_y=y_fold)

            X_trans_df = pd.DataFrame(X_trans_fold, columns=feat_names,  index=transform_index)
            y_series = pd.Series(y_trans_fold, index=transform_index)
            return X_trans_df, y_series

        # Transform the data up to right before it gets passed to the
        # final model
        X_trans_fold = estimator.transform(X_fold, nested_model=nested_model)
        
        # Put the data in a dataframe with associated feature names, and index then return
        return pd.DataFrame(X_trans_fold, columns=feat_names,  index=X_fold.index)

    def compare(self, other, rope_interval=[-0.01, 0.01]):
        '''This method is designed to perform a statistical comparison
        between the results from the evaluation stored in this object
        and another instance of :class:`EvalResults`. The statistics
        produced here are explained in:
        https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html

        .. note::
            In the case that the sizes of the training and validation sets
            at each fold vary dramatically, it is unclear if this
            statistics are still valid.
            In that case, the mean train size and mean validation sizes
            are employed when computing statistics.

        Parameters
        ------------
        other : :class:`EvalResults`
            Another instance of :class:`EvalResults` in which
            to compare which. The cross-validation used
            should be the same in both instances, otherwise
            statistics will not be generated.

        rope_interval : list or dict of
            | This parameter allows for passing in a custom
                region of practical equivalence interval (or rope interval)
                a concept from bayesian statistics. If passed as
                a list, this should be a list with two elements, describing
                the difference in score which should be treated as two
                models or runs being practically equivalent.

            | Alternatively, in the case of multiple underlying
                scorers / metrics. A dictionary, where keys correspond
                to scorer / metric names can be passed with a separate
                rope_interval for each. For example:

            ::

                rope_interval = {'explained_variance': [-0.01, 0.01],
                                 'neg_mean_squared_error': [-1, 1]}

            This example would define separate rope regions depending
            on the metric.

            ::

                default = [-0.01, 0.01]

        Returns
        -------
        compare_df : pandas DataFrame
            | The returned DataFrame will generate separate rows
                for all overlapping metrics / scorers between the
                evaluators being compared. Further, columns with
                statistics of interest will be generated:

                - 'mean_diff'
                    The mean score minus other's mean score

                - 'std_diff'
                    The std minus other's std

            | Further, only in the case that the cross-validation
                folds are identical between the comparisons,
                the following additional columns will be generated:

                - 't_stat'
                    Corrected paired ttest statistic.

                - 'p_val'
                    The p value for the corrected paired ttest statistic.

                - 'better_prob'
                    The probability that this evaluated option is better than
                    the other evaluated option under a bayesian framework and
                    the passed value of rope_interval. See sklearn example
                    for more details.

                - 'worse_prob'
                    The probability that this evaluated option is worse than
                    the other evaluated option under a bayesian framework and
                    the passed value of rope_interval. See sklearn example
                    for more details.

                - 'rope_prob'
                    The probability that this evaluated option is equivalent to
                    the other evaluated option under a bayesian framework and
                    the passed value of rope_interval. See sklearn example
                    for more details.

        '''

        equal_cv = True

        # Make sure same number of folds
        if len(self.train_subjects) != len(other.train_subjects):
            equal_cv = False

        # Make sure subjects from folds line up
        for fold in range(len(self.train_subjects)):
            if not np.array_equal(self.train_subjects[fold],
                                  other.train_subjects[fold]):
                equal_cv = False

            if not np.array_equal(self.val_subjects[fold],
                                  other.val_subjects[fold]):
                equal_cv = False

        # Only compute for the overlapping metrics
        overlap_metrics = set(list(self.mean_scores)).intersection(set(
            list(other.mean_scores)))

        for metric in overlap_metrics:
            if np.array_equal(self.scores[metric], other.scores[metric]):
                raise RuntimeError(
                    f'Cannot compare as scores are identical for {metric}.')

        # Init difference dataframe
        dif_df = pd.DataFrame(index=list(overlap_metrics))

        # Add base differences
        for metric in overlap_metrics:

            dif_df.loc[metric, 'mean_diff'] =\
                self.mean_scores[metric] - other.mean_scores[metric]

            dif_df.loc[metric, 'std_diff'] =\
                self.std_scores[metric] - other.std_scores[metric]

        # Only compute p-values if equal cv
        if equal_cv:
            for metric in overlap_metrics:

                # Grab scores and other info
                scores1 = np.array(self.scores[metric])
                scores2 = np.array(other.scores[metric])

                differences = scores1 - scores2
                n = len(scores1)
                df = n - 1

                # Use the mean train / test size
                n_train = np.mean([len(ti) for ti in self.train_subjects])
                n_test = np.mean([len(ti) for ti in self.val_subjects])

                # Frequentist Approach
                t_stat, p_val = compute_corrected_ttest(differences, df,
                                                        n_train, n_test)
                dif_df.loc[metric, 't_stat'] = t_stat
                dif_df.loc[metric, 'p_val'] = p_val

                # Bayesian
                t_post = t(df, loc=np.mean(differences),
                           scale=corrected_std(differences, n_train, n_test))

                # Passed as either list of two values or dict
                if isinstance(rope_interval, dict):
                    ri = rope_interval[metric]
                else:
                    ri = rope_interval

                worse_prob = t_post.cdf(ri[0])
                better_prob = 1 - t_post.cdf(ri[1])
                rope_prob =\
                    t_post.cdf(ri[1]) - t_post.cdf(ri[0])

                # Add to dif_df
                dif_df.loc[metric, 'better_prob'] = better_prob
                dif_df.loc[metric, 'worse_prob'] = worse_prob
                dif_df.loc[metric, 'rope_prob'] = rope_prob

        return dif_df

    @doc(dataset=_base_docs['dataset'])
    def subset_by(self, group, dataset=None, decode_values=True):
        '''Generate instances of :class:`EvalResultsSubset` based
        on subsets of subjects based on different unique groups.

        This method is used to analyze results
        as broken down by the different unique groups
        of a column in the passed :class:`Dataset`.

        Note that the train subjects in resulting breakdown will not change,
        that only the validation sets will be split by group.

        Parameters
        ------------
        group : str
            The name of a column within the passed dataset
            that defines the different subsets of subjects.
            This column must be categorical and have no missing
            values.

        {dataset}

            | If left as default=None, then will try to use
              a shallow copy of the dataset passed to the original
              evaluate call (assuming evaluate was run with store_data_ref=True).

            ::

                default = None

        decode_values : bool
            If the original values of the group column
            were encoded via a :class:`Dataset` function,
            this if True, this function will try to
            represent values by their original name
            rather than the name used internally.
            If False, then the internal ordinal number
            value will be used.

            ::

                default = True

        Returns
        ---------
        subsets : dict of :class:`EvalResultsSubset`
            | Returns a dictionary of :class:`EvalResultsSubset`,
              where keys are generated as a representation of
              the value stored for each unique group. If decode_values
              is True, then these values are the original names
              otherwise they are the internal names.

            | Saved under each key is an instance of
              :class:`EvalResultsSubset`, which can be
              treated the same as an instance of
              :class:`EvalResults`, except it has a subset
              of values for val_subjects, and different
              preds and scores representing this subset.
        '''

        from .compare import compare_dict_from_existing

        # Check dataset
        dataset = self._dataset_check(dataset)

        if self.preds is None:
            raise RuntimeError('store_preds must have been set '
                               'to True to use this function.')

        subsets = {}

        # Make sure exists, is categorical and no NaN
        dataset._validate_group_key(group, name='group')

        # Get the values for just this column
        values = dataset._get_values(group,
                                     decode_values=decode_values)

        # Add a subset for each set of values
        for value in values.unique():
            subset_name = clean_str(f'{group}={value}')

            # Get all subjects with this value
            subjs = values[values == value].index

            # Get evaluator subset
            subsets[clean_str(value)] =\
                EvalResultsSubset(self, subjs, subset_name=subset_name)
        
        # Return as compare dict, so we have access to the summary function
        return compare_dict_from_existing(subsets)

    def to_pickle(self, loc):
        '''Quick helper to save as pickle.

        Parameters
        -----------
        loc : str
            The location in which to save the results object.
        '''

        with open(loc, 'wb') as f:
            pkl.dump(self, f)

    @doc(dataset=_base_docs['dataset'])
    def run_permutation_test(self, n_perm=100, dataset=None, random_state=None,
                             blocks=None, within_grp=True, plot=False):
        '''Compute signifigance values for the original results according to
        a permutation test scheme. In this setup, we estimate the null model
        by randomly permuting the target variable, and re-evaluating the same
        pipeline according to the same CV. In this manner,
        a null distribution of size `n_perm` is generated in which
        we can compare the real, unpermuted results to.

        Note: If using a custom scorer, w/ no sign_ attribute, this method
        will assume that higher values for metrics are better.

        Parameters
        ------------
        n_perm : int, optional
            The number of permutations to test.

            ::

                default = 100

        {dataset}

            | If left as default=None, then will try to use
              a shallow copy of the dataset passed to the original
              evaluate call (assuming evaluate was run
              with store_data_ref=True).

            ::

                default = None

        random_state : int, or None, optional
            Pseudo-random number generator to control the permutations
            of each feature. If left as None, then initialize a new
            random state for each permutation.

            ::

                default = None

        blocks : None, array, pd.Series or pd.DataFrame, optional
            This parameter is only available when the neurotools
            library is installed.
            See: https://github.com/sahahn/neurotools

            This parameter represents the underlying exchangability-block
            structure of the data passed. It is also used to
            constrain the possible
            permutations in some way.

            See PALM's documentation for an introduction
            on how to format ExchangeabilityBlocks:
            https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM/ExchangeabilityBlocks

            This parameter accepts the same style input as PALM,
            except it is passed here as an array or DataFrame instead
            of as a file. The main requirement is that the shape of
            the structure match the number of subjects / data points
            in the first dimension.

            ::

                default = None

        within_grp : bool, optional
            This parameter is only relevant when a permutation
            structure / blocks is passed, in that
            case it describes how the left-most exchanability /
            permutation structure column should act.
            Specifically, if True, then it specifies that the
            left-most column should be treated as groups
            to act in a within group swap only manner. If False,
            then it will consider the left-most column
            groups to only be able to swap at the group level
            with other groups of the same size.

            ::

                default = True

        plot : bool, optional
            Can optionally add a plot visualizing the true result in comparison
            to the generated null distribution.

            ::

                default = False

        Returns
        ------------
        p_values : dict of float
            A dictionary, as indexed by all of the valid metrics, with the
            computed p-values.

        p_scores : dict of array
            The null distribution, as indexed by all of the valid metrics,
            of scores.

        '''

        # Check dataset
        dataset = self._dataset_check(dataset)

        # Make sure cv is saved
        if self.cv is None:
            raise RuntimeError('The original call to evaluate must have had '
                               'store_cv set to True to use this method.')

        # Init rng
        rng = default_rng(random_state)

        # X stays the same
        X, _ = dataset.get_Xy(self.ps)

        if blocks is not None:

            # If not same length, try to match them
            if len(X) != len(blocks):

                try:
                    blocks = blocks.loc[X.index]
                except:

                    # TODO give more info
                    raise RuntimeError('length of blocks and data do not match.')

        # TODO add option to multi-process here
        # TODO add verbose / progress bar
        p_scores = {}
        for _ in range(n_perm):

            # Get the random seed for this permutation
            try:
                rng_integers = rng.integers
            except AttributeError:
                rng_integers = rng.randint
            rs = rng_integers(147483648)

            # Get permuted y
            y_perm = dataset._get_permuted_y(self.ps, random_state=rs,
                                             blocks=blocks,
                                             within_grp=within_grp)

            # Init silent copy to eval with
            p_eval = EvalResults(estimator=self.estimator,
                                 ps=self.ps,
                                 encoders=self.encoders_,
                                 progress_bar=False,
                                 store_preds=False,
                                 store_estimators=False,
                                 store_timing=False,
                                 store_cv=False,
                                 store_data_ref=False,
                                 eval_verbose=-2,
                                 progress_loc=None,
                                 mute_warnings=False,
                                 compare_bars=None)

            # Evaluate - with internal eval method
            p_eval._eval(X, y_perm, cv=deepcopy(self.cv))

            # Extract scores and add to baseline
            for metric, score in p_eval.mean_scores.items():
                try:
                    p_scores[metric].append(score)
                except KeyError:
                    p_scores[metric] = [score]

        # Convert to p-values
        p_values, null_dist_means, null_dist_stds = {}, {}, {}
        for metric, scores in p_scores.items():

            # Sort actual w/ null dist
            actual = self.mean_scores[metric]
            base = np.vstack(scores + [actual])
            sorted_base = np.sort(base, axis=0)

            # Get ind in sorted
            ind = np.where(sorted_base == actual)[0][0]

            # Compute p-value, if no info on higher better,
            # e.g., custom scorer, then we just assume higher better.
            higher_better = True
            if hasattr(self.ps.scorer[metric], '_sign'):
                higher_better = bool(self.ps.scorer[metric]._sign)

            # Use version based on if higher better
            if higher_better:
                p_values[metric] = (n_perm - ind + 1) / (n_perm + 1)
            else:
                p_values[metric] = (ind + 1) / (n_perm + 1)

            # Add means and stds
            null_dist_means[metric] = np.mean(scores)
            null_dist_stds[metric] = np.std(scores)

        # Optionally make plot
        if plot:

            if len(p_scores) == 1:
                n_rows, n_cols = 1, 1
            else:
                n_rows, n_cols = (len(p_scores) // 2) + (len(p_scores) % 2), 2

            # Init sub plots
            _, ax = plt.subplots(n_rows, n_cols, figsize=(n_cols * 8, n_rows * 6))

            # Plot each metric
            for row in range(n_rows):
                for col in range(n_cols):

                    if len(p_scores) == 1:
                        a = ax
                    elif n_rows == 1:
                        a = ax[col]
                    elif n_cols == 1:
                        a = ax[row]
                    else:
                        a = ax[row][col]

                    # Get current metric
                    try:
                        metric = list(p_scores)[col + (row * n_cols)]
                    except IndexError:
                        continue

                    # Base hist
                    hist_label = f'Null Dist. (Mean): {null_dist_means[metric]:.3f}'
                    sns.histplot(p_scores[metric], ax=a, kde=True,
                                 label=hist_label)

                    # Add vert line
                    a.axvline(self.mean_scores[metric], 
                              linewidth=6, color='Red',
                              label=f'Baseline: {self.mean_scores[metric]:.3f}'
                                    f' (pval={p_values[metric]:.3f})')

                    # Add legend + title
                    a.legend()
                    a.set_title(metric)

        # Return p_values and each of the null results
        return p_values, p_scores


class EvalResultsSubset(EvalResults):
    '''This class represents a subset of :class:`EvalResults` and
    is returned as a result of calling :func:`EvalResults.subset_by`.

    This class specifically updates values for a subset of val_subjects,
    which mean only the following attributes are re-calculated / will be
    different from the source :class:`EvalResults` ::

        val_subjects
        all_val_subjects
        preds
        scores
        mean_scores
        weighted_mean_scores

    '''

    def __init__(self, evaluator, subjects, subset_name=None):

        # Save some class attributes
        self.ps = evaluator.ps
        self.estimators = evaluator.estimators
        self.train_subjects = evaluator.train_subjects
        self.all_train_subjects = evaluator.all_train_subjects
        self.n_repeats_ = evaluator.n_repeats_
        self.timing = evaluator.timing
        self.cv = evaluator.cv
        self._store_cv = evaluator._store_cv
        self.verbose = -1

        # Save name for display
        self.subset_name = subset_name

        # If keeping track of dataset, we keep track of the whole dataset, based on
        # the nature of how the subsetting works
        self._store_data_ref = evaluator._store_data_ref
        if self._store_data_ref:
            self._dataset = evaluator._dataset
        else:
            self._dataset = None

        # Need to set val indices first
        self._set_val_subjects(subjects, evaluator)

        # Then can set preds and scores
        self._set_preds(evaluator)
        self._set_scores()

        # Calculate summary scores
        self._compute_summary_scores()

    def _get_display_name(self):

        base = str(self.__class__.__name__)
        if self.subset_name is None:
            return base

        return base + '(' + self.subset_name + ')'

    def _set_val_subjects(self, subjects, evaluator):

        self.val_subjects = [fold_indices.intersection(subjects)
                             for fold_indices in evaluator.val_subjects]

        self.all_val_subjects = [fold_indices.intersection(subjects)
                                 for fold_indices
                                 in evaluator.all_val_subjects]

    def _set_preds(self, evaluator):

        masks = [np.array([ind in self.all_val_subjects[i]
                           for ind in evaluator.all_val_subjects[i]])
                 for i in range(len(self.all_val_subjects))]

        self.preds = {metric: [ps[mask] for ps, mask in
                               zip(evaluator.preds[metric], masks)]
                      for metric in evaluator.preds}

    def _set_scores(self):

        self.scores = {}

        for scorer_str in self.ps.scorer:
            scorer = self.ps.scorer[scorer_str]

            if isinstance(scorer, _PredictScorer):
                preds = self.preds['predict']
            elif isinstance(scorer, _ProbaScorer):

                # Binary case
                if self.preds['predict_proba'][0][0].shape[0] == 2:
                    preds = [p[:, 1] for p in self.preds['predict_proba']]

                # Cat case
                else:
                    preds = self.preds['predict_proba']

            elif isinstance(scorer, _ThresholdScorer):
                if 'decision_function' in self.preds:
                    preds = self.preds['decision_function']

                # Binary proba case
                elif self.preds['predict_proba'][0][0].shape[0] == 2:
                    preds = [p[:, 1] for p in self.preds['predict_proba']]

                # Cat case
                else:
                    preds = self.preds['predict_proba']
            else:
                raise RuntimeError('invalid scorer type')

            # Calculate scores for each fold
            self.scores[scorer_str] = []
            for p, yt in zip(preds, self.preds['y_true']):
                score = scorer._score_func(yt, p, **scorer._kwargs)
                score *= scorer._sign
                self.scores[scorer_str].append(score)


# TODO - 
class EvalResultsFold():

    def __init__(self, evaluator, fold):

        if hasattr(evaluator, 'estimators'):
            self.estimator = evaluator.estimators[fold]

        # self.scores =
        # self.feat_names =

