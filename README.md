# web machine learning Api

This repository contains to project web api and machine learning server.

Web Api:
you can see the history of the past analysis and perforce a new analysis.

##Analysis History
-iris.csv ML Algorithm: Decision Tree Classifier | Accuracy: 95.5556in 2020-03-09 18:06:12.954142

-iris.csv ML Algorithm: Gaussian NB | Accuracy: 95.5556in 2020-03-09 18:06:12.971154

##Perform new analysis
First you upload a file then start the analysis.

In summary of Machine Learning Analysis page you can find:
Name of the file you upload for your analysis and you can see the content of the file by clinking on view dataset button.
The detail of each model performance can be found here. The following a summary of the decision tree classifier results on iris.csv which can be found in the repository:

##Decision Tree Classifier
ML Algorithm: Decision Tree Classifier | Accuracy: 95.5556
Classification report

              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        16     
    versicolor     0.91      0.91      0.91        11 
    virginica      0.94      0.94      0.94        18

    accuracy                           0.96        45
    macro avg      0.95      0.95      0.95        45
    weighted avg   0.96      0.96      0.96        45

#Machine Learning Server
Performing following machine learning algorithms:
- Logistic Regression
- Linear Discriminant Analysis
- K Neighbors Classifier
- Decision Tree Classifier
- Gaussian NB
- Support Vector Machine

Finally for each model compute:
- Accuracy
- Precision
- Recall
- F1 score