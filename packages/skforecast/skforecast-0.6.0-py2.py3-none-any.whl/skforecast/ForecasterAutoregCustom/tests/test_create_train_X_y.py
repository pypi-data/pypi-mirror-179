# Unit test create_train_X_y ForecasterAutoregCustom
# ==============================================================================
import re
import pytest
import numpy as np
import pandas as pd
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from sklearn.linear_model import LinearRegression


def create_predictors(y): # pragma: no cover
    """
    Create first 5 lags of a time series.
    """
    lags = y[-1:-6:-1]
    return lags


def test_create_train_X_y_exception_when_len_y_is_less_than_window_size():
    """
    Test exception is raised when length of y is less than self.window_size +1.
    """
    forecaster = ForecasterAutoregCustom(
                     regressor      = LinearRegression(),
                     fun_predictors = create_predictors,
                     window_size    = 10
                 )
                 
    err_msg = re.escape(
                (f'`y` must have as many values as the windows_size needed by '
                 f'{forecaster.create_predictors.__name__}. For this Forecaster the '
                 f'minimum length is {forecaster.window_size + 1}')
            )
    with pytest.raises(ValueError, match = err_msg):
        forecaster.create_train_X_y(y=pd.Series(np.arange(5)))


@pytest.mark.parametrize("y                        , exog", 
                         [(pd.Series(np.arange(50)), pd.Series(np.arange(10))), 
                          (pd.Series(np.arange(10)), pd.Series(np.arange(50))), 
                          (pd.Series(np.arange(10)), pd.DataFrame(np.arange(50).reshape(25,2)))])
def test_create_train_X_y_exception_when_len_y_is_different_from_len_exog(y, exog):
    """
    Test exception is raised when length of y is not equal to length exog.
    """
    forecaster = ForecasterAutoregCustom(
                     regressor      = LinearRegression(),
                     fun_predictors = create_predictors,
                     window_size    = 5
                 )

    err_msg = re.escape(
                (f'`exog` must have same number of samples as `y`. '
                 f'length `exog`: ({len(exog)}), length `y`: ({len(y)})')
              )
    with pytest.raises(ValueError, match = err_msg):
        forecaster.create_train_X_y(y=y, exog=exog)


def test_create_train_X_y_exception_when_y_and_exog_have_different_index():
    """
    Test exception is raised when y and exog have different index.
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = create_predictors,
                    window_size    = 5
                )

    err_msg = re.escape(
                    ('Different index for `y` and `exog`. They must be equal '
                     'to ensure the correct alignment of values.')      
                )
    with pytest.raises(ValueError, match = err_msg):
        forecaster.fit(
            y=pd.Series(np.arange(10), index=pd.date_range(start='2022-01-01', periods=10, freq='1D')),
            exog=pd.Series(np.arange(10), index=pd.RangeIndex(start=0, stop=10, step=1))
        ) 


def test_create_train_X_y_output_when_y_is_series_10_and_exog_is_None():
    """
    Test the output of create_train_X_y when y=pd.Series(np.arange(10)) and 
    exog is None.
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = create_predictors,
                    window_size    = 5
                )
    results = forecaster.create_train_X_y(y=pd.Series(np.arange(10, dtype=float)))
    expected = (pd.DataFrame(
                    data = np.array([[4., 3., 2., 1., 0.],
                                     [5., 4., 3., 2., 1.],
                                     [6., 5., 4., 3., 2.],
                                     [7., 6., 5., 4., 3.],
                                     [8., 7., 6., 5., 4.]]),
                    index   = np.array([5, 6, 7, 8, 9]),
                    columns = ['custom_predictor_0', 'custom_predictor_1',
                               'custom_predictor_2', 'custom_predictor_3',
                               'custom_predictor_4']
                ),
                pd.Series(
                    np.array([5., 6., 7., 8., 9.]),
                    index = np.array([5, 6, 7, 8, 9]),
                    name = 'y'
                )
               )     

    for i in range(len(expected)):
        if isinstance(expected[i], pd.DataFrame):
            pd.testing.assert_frame_equal(results[i], expected[i])
        elif isinstance(expected[i], pd.Series):
            pd.testing.assert_series_equal(results[i], expected[i])
        else:
            assert (results[i] == expected[i]).all()


def test_create_train_X_y_output_when_y_is_series_10_and_exog_is_series():
    """
    Test the output of create_train_X_y when y=pd.Series(np.arange(10)) and 
    exog is a pandas series
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = create_predictors,
                    window_size    = 5
                )
    results = forecaster.create_train_X_y(
                y = pd.Series(np.arange(10, dtype=float)),
                exog =  pd.Series(np.arange(100, 110, dtype=float), name='exog')
              )
    expected = (pd.DataFrame(
                    data = np.array([[4., 3., 2., 1., 0., 105.],
                                     [5., 4., 3., 2., 1., 106.],
                                     [6., 5., 4., 3., 2., 107.],
                                     [7., 6., 5., 4., 3., 108.],
                                     [8., 7., 6., 5., 4., 109.]]),
                    index   = np.array([5, 6, 7, 8, 9]),
                    columns = ['custom_predictor_0', 'custom_predictor_1',
                               'custom_predictor_2', 'custom_predictor_3',
                               'custom_predictor_4', 'exog']
                ),
                pd.Series(
                    np.array([5., 6., 7., 8., 9.]),
                    index = np.array([5, 6, 7, 8, 9]),
                    name = 'y'
                )
               )       

    for i in range(len(expected)):
        if isinstance(expected[i], pd.DataFrame):
            pd.testing.assert_frame_equal(results[i], expected[i])
        elif isinstance(expected[i], pd.Series):
            pd.testing.assert_series_equal(results[i], expected[i])
        else:
            assert (results[i] == expected[i]).all()


def test_create_train_X_y_output_when_y_is_series_10_and_exog_is_dataframe():
    """
    Test the output of create_train_X_y when y=pd.Series(np.arange(10)) and 
    exog is a pandas dataframe with two columns.
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = create_predictors,
                    window_size    = 5
                )
    results = forecaster.create_train_X_y(
                y = pd.Series(np.arange(10, dtype=float)),
                exog = pd.DataFrame({
                            'exog_1' : np.arange(100, 110, dtype=float),
                            'exog_2' : np.arange(1000, 1010, dtype=float)
                })
              )
    expected = (pd.DataFrame(
                    data = np.array([[4., 3., 2., 1., 0., 105., 1005.],
                                     [5., 4., 3., 2., 1., 106., 1006.],
                                     [6., 5., 4., 3., 2., 107., 1007.],
                                     [7., 6., 5., 4., 3., 108., 1008.],
                                     [8., 7., 6., 5., 4., 109., 1009.]]),
                    index   = np.array([5, 6, 7, 8, 9]),
                    columns = ['custom_predictor_0', 'custom_predictor_1',
                               'custom_predictor_2', 'custom_predictor_3',
                               'custom_predictor_4', 'exog_1', 'exog_2']
                ),
                pd.Series(
                    np.array([5., 6., 7., 8., 9.]),
                    index = np.array([5, 6, 7, 8, 9]),
                    name = 'y'
                )
               )        

    for i in range(len(expected)):
        if isinstance(expected[i], pd.DataFrame):
            pd.testing.assert_frame_equal(results[i], expected[i])
        elif isinstance(expected[i], pd.Series):
            pd.testing.assert_series_equal(results[i], expected[i])
        else:
            assert (results[i] == expected[i]).all()

    
def test_create_train_X_y_exception_when_y_and_exog_have_different_length():
    """
    Test exception is raised when length of y and length of exog are different.
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = create_predictors,
                    window_size    = 5
                )

    y = pd.Series(np.arange(50))
    exog = pd.Series(np.arange(10))
    err_msg = re.escape((
                f'`exog` must have same number of samples as `y`. '
                f'length `exog`: ({len(exog)}), length `y`: ({len(y)})'
              ))
    with pytest.raises(ValueError, match = err_msg):
        forecaster.fit(y=y, exog=exog)

    y = pd.Series(np.arange(10))
    exog = pd.Series(np.arange(50))
    err_msg = re.escape((
                f'`exog` must have same number of samples as `y`. '
                f'length `exog`: ({len(exog)}), length `y`: ({len(y)})'
              ))
    with pytest.raises(ValueError, match = err_msg):
        forecaster.fit(y=y, exog=exog)

    y = pd.Series(np.arange(10))
    exog = pd.DataFrame(np.arange(50).reshape(25,2))
    err_msg = re.escape((
                f'`exog` must have same number of samples as `y`. '
                f'length `exog`: ({len(exog)}), length `y`: ({len(y)})'
              ))
    with pytest.raises(ValueError, match = err_msg):
        forecaster.fit(y=y, exog=exog)


def test_create_train_X_y_exception_fun_predictors_return_nan_values():
    """
    Test exception is raised when length of y and length of exog are different.
    """
    forecaster = ForecasterAutoregCustom(
                    regressor      = LinearRegression(),
                    fun_predictors = lambda y: np.array([np.nan, np.nan]),
                    window_size    = 5
                )
    err_msg = re.escape("`create_predictors()` is returning `NaN` values.")
    with pytest.raises(Exception, match = err_msg):
        forecaster.fit(y=pd.Series(np.arange(50)))