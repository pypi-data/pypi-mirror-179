# Unit test __init__ ForecasterAutoregCustom
# ==============================================================================
import re
import pytest
import pandas as pd
import numpy as np
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor


def create_predictors(y): # pragma: no cover
    """
    Create first 5 lags of a time series.
    """
    
    lags = y[-1:-6:-1]
    
    return lags  


def test_init_exception_when_window_size_argument_is_string():
   """
   Test exception is raised when window_size is not an int.
   """
   window_size = '5'
   err_msg = re.escape(
                f'Argument `window_size` must be an int. Got {type(window_size)}.'
            )
   with pytest.raises(TypeError, match = err_msg):
        ForecasterAutoregCustom(
            regressor      = LinearRegression(),
            fun_predictors = create_predictors,
            window_size    = window_size
        )

def test_init_exception_when_fun_predictors_argument_is_string():
   """
   Test exception is raised when fun_predictors is not a callable.
   """
   fun_predictors = 'create_predictors'
   err_msg = re.escape(
                f'Argument `fun_predictors` must be a callable. Got {type(fun_predictors)}.'
            )
   with pytest.raises(TypeError, match = err_msg):
        ForecasterAutoregCustom(
            regressor      = LinearRegression(),
            fun_predictors = fun_predictors,
            window_size    = 5
        )

def test_init_exception_when_weight_func_argument_is_not_callable():
   """
   """
   weight_func = '---'
   err_msg = re.escape(
                f"Argument `weight_func` must be a callable. Got {type(weight_func)}."
            )
   with pytest.raises(TypeError, match = err_msg):
        ForecasterAutoregCustom(
            regressor      = LinearRegression(),
            fun_predictors = create_predictors,
            window_size    = 5,
            weight_func    = weight_func
        )


def test_init_exception_when_series_weights_is_provided_and_regressor_has_not_sample_weights():
   """
   """
   def weight_func(index): # pragma: no cover
        return np.ones_like(index)

   warn_msg = re.escape(
                f"Argument `weight_func` is ignored since regressor KNeighborsRegressor()"
                f" does not accept `sample_weight` in its `fit` method."
            )
   with pytest.warns(UserWarning, match = warn_msg):
        ForecasterAutoregCustom(
            regressor      = KNeighborsRegressor(),
            fun_predictors = create_predictors,
            window_size    = 5,
            weight_func    = weight_func
        )