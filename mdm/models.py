import sys as _sys
from sklearn.model_selection import RandomizedSearchCV as _rnd_search
from sklearn.ensemble import GradientBoostingClassifier
import numpy as _np
import os as _os
from sklearn.metrics import accuracy_score as _acc
import pickle as _pkl
import logging as _log
import seaborn as sns
from sklearn.metrics import confusion_matrix as _cm
from matplotlib import pyplot as _plt
import pathlib
_log.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                     level=_log.INFO, stream=_sys.stdout)
_logger = _log.getLogger(__name__)
sns.set()
curr_path = pathlib.Path(__file__).parent.absolute()


def save(model, name):
    """
    Saves model into the model folder of the package

    Parameters
    ----------
    model : model to be saved
    name : name of the sub folder containing the model
    """
    sp = _os.path.join(curr_path, '../models', name)
    if not _os.path.exists(sp):
        _os.makedirs(sp)
    _pkl.dump(model, open(_os.path.join(sp, 'model.pkl'), 'wb'))
    _logger.info("saved to : {0}".format(sp))

def load(name):
    """
    Loads model from the model folder of the package

    Parameters
    ----------
    name : model name also subfolder name to find the model to be loaded
    """
    sp = _os.path.join(curr_path, '../models', name)
    model = _pkl.load(open(_os.path.join(sp, 'model.pkl'), 'rb'))
    _logger.info("loaded from : {0}".format(_os.path.join(sp, name)))
    return model

def train(X_train, y_train, X_dev, y_dev):
    """
    Train wrapper for the grandient boosting model with optimal parameters from the random search

    Parameters
    ----------
    X_train : train features dataframe
    y_train : train labels dataframe
    X_dev : dev features dataframe
    y_dev : dev labels dataframe

    Returns
    -------
    dev accuracy of the trained model
    trained model
    """
    mdl = GradientBoostingClassifier(max_depth=6, max_features=4, min_samples_leaf=6,
                           n_estimators=73)
    mdl.fit(X_train, y_train)
    y_pred = mdl.predict(X_dev)
    acc = _acc(y_dev,y_pred)
    _logger.info("accuracy : {0}".format(acc))
    return acc, mdl

def evaluate(model, X, y):
    """
    Evaluation accuracy wrapper

    Parameters
    ----------
    model : model to be used
    X : features dataset
    y : labels dataset

    Returns
    -------
    accuracy of the evaluated model on dataset
    """
    y_pred = model.predict(X)
    acc = _acc(y,y_pred)
    _logger.info("accuracy : {0}".format(acc))
    return acc

def predict(model, X):
    """
    Prediction wrapper

    Parameters
    ----------
    model : model instance to be used to predict
    X : feature dataframe for prediction

    Returns
    -------
    predicted labels
    """
    y_pred = model.predict(X)
    return y_pred
