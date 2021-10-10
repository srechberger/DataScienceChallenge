from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import validation_curve
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
    
def hyperparameter_rf_gs(X_train, X_test, y_train, y_test):
    # Estimators
    n_estimators = [10, 15, 20, 25, 30, 40]
    # Maximum number of levels in tree
    max_depth = [5, 8, 10]
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [2, 5, 8]

    # Create a grid to search for best hyperparameters
    grid = {'n_estimators': n_estimators,
            'max_depth': max_depth,
            'min_samples_split': min_samples_split,
            'min_samples_leaf': min_samples_leaf}

    # Create a base model to tune
    rf = RandomForestRegressor()
    # Apply GridSearch
    gridRF = GridSearchCV(rf, grid, cv=3, verbose=1, n_jobs=-1)
    # Fit Model
    bestRF = gridRF.fit(X_train, y_train)

    # Print best params
    print('Grid-Search params: ', bestRF.best_params_)
    print('RandomForestRegressor with best params was created.')
    
    return bestRF
