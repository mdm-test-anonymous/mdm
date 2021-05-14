import logging as _log
import sys as _sys
import seaborn as sns
import numpy as _np
from sklearn.metrics import confusion_matrix as _cm
import os as _os
from matplotlib import pyplot as _plt
import pathlib
_log.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                     level=_log.INFO, stream=_sys.stdout)
_logger = _log.getLogger(__name__)
curr_path = pathlib.Path(__file__).parent.absolute()


def confusion_matrix(y_true, y_preds, labels, model_name=None):
    """
    Wrapper for confusion matrix computation, visualisation and storing

    Parameters
    ----------
    y_true : true labels dataframe
    y_preds : predicted labels dataframe
    labels : label orders to be used
    model_name : model nome to store visualisation besides the model used
    """
    rst = _cm(y_true, y_preds, normalize='true', labels=labels)
    palette = sns.diverging_palette(20, 220, as_cmap=True)
    _plt.figure(figsize=(10,5))
    sns.heatmap(rst, xticklabels=labels, yticklabels=labels, cmap=palette, annot=True)
    if model_name:
        sp = _os.path.join(_os.path.join(curr_path, '../models/', model_name), 'confusion_matrix.png')
        _logger.info("saving to : {0}".format(sp))
        _plt.savefig(sp, dpi=400)

def feature_importance(feat_imp, feats, model_name=None):
    """
    Wrapper for feature importance visualisation and storing

    Parameters
    ----------
    feat_imp : feature importance of the model
    feats : columns of the feature dataset
    model_name : model nome to store visualisation besides the model used
    """
    feature_importance = 100.0 * (feat_imp / feat_imp.max())
    sorted_idx = _np.argsort(feat_imp)
    pos = _np.arange(sorted_idx.shape[0]) + .5
    # plt.subplot(1, 2, 2)
    _plt.figure(figsize=(8, 18))
    _plt.barh(pos, feat_imp[sorted_idx], align='center')
    _plt.yticks(pos, feats[sorted_idx])
    _plt.title('Feature Importance')
    if model_name:
        sp = _os.path.join(_os.path.join(curr_path, '../models/', model_name), 'feature_importance.png')
        _logger.info("saving to : {0}".format(sp))
        _plt.savefig(sp, dpi=400)
    _plt.show()
