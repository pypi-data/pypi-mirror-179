from ..helpers import get_obj_and_params, all_from_objects
from ...extensions.loaders import Identity
import warnings

LOADERS = {
    'identity': (Identity, ['default']),
}

# If nilearn dependencies
try:

    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        from nilearn.input_data import NiftiLabelsMasker

    from ...extensions.loaders import SingleConnectivityMeasure
    LOADERS['volume rois'] = (NiftiLabelsMasker, ['default'])
    LOADERS['connectivity'] = (SingleConnectivityMeasure, ['default'])

except ImportError:
    pass


def get_loader_and_params(loader_str, extra_params, params, **kwargs):

    loader, extra_loader_params, loader_params =\
        get_obj_and_params(loader_str, LOADERS, extra_params, params)

    return loader(**extra_loader_params), loader_params


all_obj_keys = all_from_objects(LOADERS)
