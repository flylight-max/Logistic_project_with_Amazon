
try:
    import pandas as pd
except ImportError as e:
    print(f"Error importing pandas: {e}")
    raise
def orig_train_test_df(orig_df,train_df,test_df,col_name):
    """Returns a pandas DataFrame with a column 'Dataset' containing the name of the dataset 
    and a column 'col_name' containing the corresponding values of each dataset of the col_name.
    Args:
        orig_df, train_df, test_df (pandas DataFrame): the DataFrames you want to combine.
        col_name (string): The name of the column you want to combine.
    """
    my_dict = {"Dataset":[], col_name:[]}
    for value in orig_df[col_name]:
        my_dict["Dataset"].append(orig_df.name)
        my_dict[col_name].append(value)
    for value2 in train_df[col_name]:
        my_dict["Dataset"].append(train_df.name)
        my_dict[col_name].append(value2)
    for value3 in test_df[col_name]:
        my_dict["Dataset"].append(test_df.name)
        my_dict[col_name].append(value3)
    col_name_df = pd.DataFrame(my_dict)
    return col_name_df

import matplotlib.pyplot as plt
from sklearn.model_selection import KFold,cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE
def visu_cv_score(models,X_train,y_train):
    """Returns a boxplot comparing the the value scores (using KFold)
    of the regression models chosen among this list:
    LinearRegression, Ridge, Lasso and DecisionTreeRegressor.
    Args:
        models (dict): A dictionnary where keys correspond to the names of the 
    models and the values are the instantiated models.
        X_train, y_train (2D numpy arrays): features and target values respectively 
    after having splitted the dataset to a train dataset and a test dataset.
    """
    results = []
    for model in models.values():
        kf = KFold(n_splits=6, random_state=1984, shuffle=True)
        cv_results = cross_val_score(model,X_train, y_train, cv=kf)
        results.append(cv_results)
    plt.boxplot(results, labels=models.keys())
    plt.ylabel("CV R²")
    plt.xlabel("Model")
    plt.show()

def rmse_regression_models(models,X_train,y_train,X_test,y_test):
    """Print the rmse of each model from models.
    Args:
        models (dict): A dictionnary where keys correspond to the names of the 
    models and the values are the instantiated models.
        X_train,y_train,X_test,y_test (np arrays): np arrays of features (X) and target variables (y)
    after having spliting the original dataset. 
    """
    for name,model in models.items():
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        rmse= MSE(y_test,y_pred) ** (1/2)
        print("{} Test set rmse: {}".format(name,rmse))

from datetime import datetime
def to_datetime(df, column_name, date_format):
    """Switch a time object to a datetime format and then specify to the selected time.
    Args:
        df (pandas dataframe): your dataset in a DataFrame format.
        column_name (str): the name of the column you want to switch to datetime.
        date_format (str): the format your column is. For example, "%b" your dates
    are months written in abbrev like "Jan".
    """
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)