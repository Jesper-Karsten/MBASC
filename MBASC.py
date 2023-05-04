import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import argparse
import os, contextlib, warnings
import numpy as np

if __name__ == "__main__":
    # Parsing the argument
    parser = argparse.ArgumentParser(description='Provide AGN-SFG classification given multi-wavelength data.')
    parser.add_argument('filename')
    args = parser.parse_args()

    # Parsing the filename
    filename = args.filename
    data = pd.read_csv(filename)

    # Checking the columns and seeing if we already have a model for this, else we need to train a new one
    # TODO: save models, now I just retrain them over and over out of laziness
    columns = data.columns

    # If there is a id column we use that for output
    if 'id' in columns:
        ids = data['id']
    else:
        ids = np.arange(len(data))

    # First check which valid columns we have
    possible_columns = ['redshift', 'nuv', 'u', 'g', 'r', 'i', 'z', 'y', 'j', 'h', 'k', 'ch1',
       'ch2', 'ch3', 'ch4', 'mips24', 'pacs100', 'pacs160', 'spire250',
       'spire350', 'spire500', 'radiototal', 'radiopeak']

    # Converting to lowercase, in case users mess up
    columns_lower = [x.lower() for x in columns]

    valid_columns_test = [c1 for c1, c2 in zip(columns, columns_lower) if c2 in possible_columns]
    valid_columns_train = [c2 for c1, c2 in zip(columns, columns_lower) if c2 in possible_columns]

    print(f"Will use the following wavebands/redshift:{valid_columns_test}")

    data = data[valid_columns_test]

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
    train_data = pd.read_csv('data/data.csv')

    # Selecting X and y data, where y is whether it's an AGN or not
    X = train_data.drop(columns=['Field', 'AGN'])
    y = train_data[['Field', 'AGN']]

    # Only selecting X columns that are also in the testing data
    X = X[valid_columns_train]

    # Splitting so that we have a validation set for early stopping
    X_train, X_val, y_train, y_val = train_test_split(X, y[['AGN', 'Field']], train_size=0.8,
                                                      stratify=y[['AGN', 'Field']])
    # Training the new model
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
            model = lgb.LGBMModel(**params, early_stopping_rounds=10).fit(X_train, y_train['AGN'],
                                                                          eval_set=[(X_train, y_train['AGN']),
                                                                                    (X_val, y_val['AGN'])])

    # DataFrame for output
    pred = model.predict(data)
    AGN = np.rint(pred)

    results = pd.DataFrame(np.array([ids, pred, AGN]).T, columns=['id', 'output', 'AGN'])
    results.to_csv(f'output/results.csv', index=False)

    # Saving the trained model
    #bst.save_model('models/test.txt', num_iteration=bst.best_iteration)