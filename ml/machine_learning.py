# ML Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

import pandas as pd

def linear_regression_old(x_value, y_value):
    X = np.array(x_value).reshape(-1, 1)
    y = np.array(y_value).reshape(-1, 1)
    model = LinearRegression(normalize=True)
    reg = model.fit(X, y)
    return model, reg.intercept_, reg.coef_

def linear_regression(x_value, y_value):
    model = LinearRegression()
    reg = model.fit(x_value, y_value)
    return model, reg.intercept_, reg.coef_   

def train_test_split_1(dataset, x_name, y_name, test_size):
    X = dataset[x_name].values.reshape(-1, 1)
    y = dataset[y_name].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test

def population_visitors(df):

    df_selected = df[['City Population', 'Museum visitors']]
    df_selected.loc[:, 'City Population'] = pd.to_numeric(df_selected.loc[:, 'City Population'])
    df_selected.loc[:, 'Museum visitors'] = pd.to_numeric(df_selected.loc[:, 'Museum visitors'])
    df_clean = df_selected.dropna()

    x_population = df_clean['City Population'].to_numpy()
    y_visitor = df_clean['Museum visitors'].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split_1(df_clean, "City Population", "Museum visitors", 0.2)

    x_data_info = {"values": x_population.tolist(), "label": "City Population", "train":X_train, "test":X_test}
    y_data_info = {"values": y_visitor.tolist(), "label": "Museum Visitors", "train":y_train, "test":y_test}
    return x_data_info, y_data_info

def perform_analysis(df):
    x_data_info, y_data_info = population_visitors(df)
    model, intercept, coefficient = linear_regression(x_data_info['train'], y_data_info['train'])

    # Saving Results of Uploaded Files  to Sqlite DB
    intercept = round(intercept[0], 4)
    coefficient = round(coefficient[0][0], 4)
    name = 'LinearRegression'
    msg = "Name: %s, intercept:%f, coefficient:%f" % (name, intercept, coefficient)               
    model_info = {"name":name,"results":msg}
    
    return model_info