import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def linear(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=3)

    model = LinearRegression().fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))



def random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=3)

    model = RandomForestRegressor().fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))


def grad_boost(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=3)

    model = GradientBoostingRegressor().fit(X_train, y_train)
    return mean_squared_error(y_test, model.predict(X_test))

