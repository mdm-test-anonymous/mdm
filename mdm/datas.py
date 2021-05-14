import pandas as _pd
import numpy as _np
import os as _os
from sklearn.model_selection import train_test_split as _split
import logging as _log
import sys as _sys

_log.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                     level=_log.INFO, stream=_sys.stdout)

_logger = _log.getLogger(__name__)

def get(path, filename):
    """
    Imports datas from data path

    Parameters
    ----------
    path : path to data folder
    filename : name of the data file

    Returns
    -------
    Dataframe of data
    """
    return _pd.read_csv(_os.path.join(path, filename), sep=",")

def transform(data):
    """
    Transforms data and creates new features

    Parameters
    ----------
    data : dataframe to be tranformed

    Returns
    -------
    Transformed data
    """
    _logger.info("log volume")
    data['log_volume'] = _np.log(data['height'] * data['width'] * data['depth'])
    _logger.info("log density")
    data['log_density'] = _np.log(data['weight'] / data['height'] * data['width'] * data['depth'])
    _logger.info("log weight")
    data['log_weight'] = _np.log(data['weight'])
    return data

def split(data, target, pct_test=0.2):
    """
    Creates train dev and test datasets

    Parameters
    ----------
    data : dataframe to be splitted
    target : target column to be seperated in y
    pct_test : percentage to for dev and test

    Returns
    -------
    X_train, y_train, X_dev, y_dev, X_test, y_test Dataframes
    """

    cols = [i for i in data.columns if i not in target]

    train, test = _split(data, test_size=pct_test)
    dev, test = _split(test, test_size=0.5)

    _logger.info("train size : {0}".format(len(train)))
    _logger.info("dev size : {0}".format(len(dev)))
    _logger.info("test size : {0}".format(len(test)))



    X_train, y_train = train[cols], train[target]
    X_dev, y_dev = dev[cols], dev[target]
    X_test, y_test = test[cols], test[target]

    return X_train, y_train, X_dev, y_dev, X_test, y_test
