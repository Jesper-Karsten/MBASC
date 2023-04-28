import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # Parameters for running the model
    params = {
        'colsample_bytree': 0.5468,
        'learning_rate': 0.06369,
        'min_data_in_leaf': 1,
        'num_leaves': 46,
        'reg_alpha': 2.619,
        'reg_lambda': 7.873,
        'n_estimators': 100000,
        'feature_pre_filter': False,
        'objective': 'binary'
    }

    # Importing the data on which the model will be trained
    data = pd.read_csv('data/data.csv')

    # Selecting X and y data, where y is whether it's an AGN or not
    X = data.drop(columns=['Field', 'AGN'])
    y = data[['Field', 'AGN']]

    # Splitting so that we have a validation set for early stopping
    X_train, X_val, y_train, y_val = train_test_split(X, y[['AGN', 'Field']], train_size=0.8,
                                                      stratify=y[['AGN', 'Field']])

    # Training the new model
    train = lgb.Dataset(X_train, label=y_train['AGN'])
    val = lgb.Dataset(X_val, label=y_val['AGN'])

    bst = lgb.train(params, train, valid_sets=[val], early_stopping_rounds=10)

    # Saving the trained model
    bst.save_model('models/test.txt', num_iteration=bst.best_iteration)

    pass