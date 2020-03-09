# ML Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import pandas as pd
import numpy as np


# Function to make predictions
def prediction(X_test, model):
    # Predicton on test with giniIndex
    y_pred = model.predict(X_test)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):

    # confusion_matrix_report = np.array2string(confusion_matrix(y_test, y_pred))

    accuracy = accuracy_score(y_test, y_pred) * 100
    accuracy = str(round(accuracy, 4))

    report = classification_report(y_test, y_pred)

    return accuracy, report


# Function to split the dataset
def splitdataset(data):
    # # Separating the target variable
    X = data.iloc[:, 0:-1]
    Y = data[data.columns[-1]]  # Select the last column as target

    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test


def perform_analysis(df):
    df_Xfeatures = df.iloc[:, 0:-1]
    df_Ylabels = df[df.columns[-1]]  # Select the last column as target
    # Model Building
    X = df_Xfeatures
    Y = df_Ylabels

    # prepare models
    models = []
    models.append(('Logistic Regression', LogisticRegression()))
    models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
    models.append(('K Neighbors Classifier', KNeighborsClassifier()))
    models.append(('Decision Tree Classifier', DecisionTreeClassifier()))
    models.append(('Gaussian NB', GaussianNB()))
    models.append(('SVM', SVC()))

    all_models_results = {}
    scoring = 'accuracy'
    for name, model in models:
        X, Y, X_train, X_test, y_train, y_test = splitdataset(df)
        result = model.fit( X_train, y_train)
        # Prediction using gini
        y_pred = prediction(X_test, model)
        accuracy, report = cal_accuracy(y_test, y_pred)
        msg = "ML Algorithm: %s | Accuracy: %s" % (name, accuracy)
        result = { "name": name, "results": msg, "report":report}
        all_models_results[name] = result

    return all_models_results


