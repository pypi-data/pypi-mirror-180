"""
This module is for classification algorithms. Total 13 algorithms are using for now. E.g,
{"LogisticRegression", "DecisionTreeClassifier", "RandomForestClassifier", "SVC", "VotingClassifier",
"KNeighborsClassifier", "GradientBoostingClassifier", "AdaBoostClassifier", "RidgeClassifier", 
"BaggingClassifier", "SGDClassifier", "LinearSVC", "XGBClassifier"}

Module Name: imathlogic
Author: Sayan Roy
Date: 10/12/2022
GitHub Repo: https://github.com/Sayan-Roy-729/iMathLogic
PyPI URL: https://pypi.org/project/iMathLogic 
"""

import time

import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn import linear_model
from sklearn import neighbors
from sklearn import ensemble
from sklearn import tree
from sklearn import svm

import xgboost

from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from tqdm import tqdm


class Classification:
    """
    This class helps to in fitting to most of the all popular classification algorithms that are used
    in different Machine Learning / Data Science projects. The used models for this class are 
    {"LogisticRegression", "DecisionTreeClassifier", "RandomForestClassifier", "SVC", "VotingClassifier",
    "KNeighborsClassifier", "GradientBoostingClassifier", "AdaBoostClassifier", "RidgeClassifier", 
    "BaggingClassifier", "SGDClassifier", "LinearSVC", "XGBClassifier"}, total 13 algorithms.

    Examples
    --------
    >>> from imathlogic.Supervised import Classification
    >>> from sklearn.datasets import load_breast_cancer
    >>> data = load_breast_cancer() 
    >>> X    = data.data
    >>> y    = data.target
    >>> clf  = Classification()
    >>> clf.fit(X, y)
    >>> print(clf.get_results_)
                            Algorithms    Time Taken    Accuracy    Precision      Recall    F1 Score
        0       DecisionTreeClassifier      0.009014    1.000000     1.000000    1.000000    1.000000
        1       RandomForestClassifier      0.224400    1.000000     1.000000    1.000000    1.000000
        2   GradientBoostingClassifier      0.642356    1.000000     1.000000    1.000000    1.000000
        3           AdaBoostClassifier      0.174056    1.000000     1.000000    1.000000    1.000000
        4                XGBClassifier      0.069702    1.000000     1.000000    1.000000    1.000000
        5            BaggingClassifier      0.075832    0.994728     0.997191    0.994398    0.995792
        6             VotingClassifier      0.330959    0.973638     0.964674    0.994398    0.979310
        7              RidgeClassifier      0.004987    0.959578     0.941799    0.997199    0.968707
        8           LogisticRegression      0.031917    0.949033     0.948087    0.971989    0.959889
        9         KNeighborsClassifier      0.021941    0.947276     0.943089    0.974790    0.958678
        10                   LinearSVC      0.029920    0.933216     0.920844    0.977591    0.948370
        11                         SVC      0.015957    0.922671     0.902314    0.983193    0.941019
        12               SGDClassifier      0.004446    0.920914     0.921622    0.955182    0.938102
    """

    def __init__(self) -> None:
        # define the algorithms
        self.__algos = {
            "LogisticRegression": linear_model,
            "DecisionTreeClassifier": tree,
            "RandomForestClassifier": ensemble,
            "SVC": svm,
            "VotingClassifier": ensemble,
            "KNeighborsClassifier": neighbors,
            "GradientBoostingClassifier": ensemble,
            "AdaBoostClassifier": ensemble,
            "RidgeClassifier": linear_model,
            "BaggingClassifier": ensemble,
            "SGDClassifier": linear_model,
            "LinearSVC": svm,
            "XGBClassifier": xgboost,
        }

        # store the performance of the models
        self.__acc_score = {}
        # time taken for the model
        self.__time_taken = {}
        # store the precision scores of the models
        self.__precision_scores = {}
        # store the recall scores of the models
        self.__recall_scores = {}
        # store the f1 scores of the model
        self.__f1_score = {}


    # train the different models and store the models' performance
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        This method helps to train the model one by one. Depending upon the dataset, it can take some time.
        """
        # type checking; only numpy ndarray and pandas DataFrame are allowed
        if (type(X) != np.ndarray and type(X) != pd.DataFrame) and \
            (type(y) != np.ndarray and type(y) != pd.DataFrame):
            raise TypeError("The X and y should be NumPy array")
        # check that both dependent and independent variables have same number of records
        elif X.shape[0] != y.shape[0]:
            raise ValueError("The dependent and independent variables should have same number of records.")


        ## Check total missing values for dependent and independent variables
        if (type(X) == np.ndarray and np.sum(np.isnan(X)) > 0) or \
            (type(y) == np.ndarray and np.sum(np.isnan(y)) > 0):
            raise ValueError("X or y or both have NaN contain NaN")
        elif (type(X) == pd.DataFrame and np.sum(X.isnull().sum().values) > 0) or \
            (type(y) == pd.DataFrame and np.sum(y.isnull().sum().values) > 0):
            raise ValueError("X or y or both contain NaN")

        ## Now train the models and store the performance
        for algo in tqdm(self.__algos):
            # start counting how much time will take by this model
            start = time.time()
            if algo == "VotingClassifier":
                estimators = [
                    ("lr", linear_model.LogisticRegression()), 
                    ("rf", ensemble.RandomForestClassifier()), 
                    ("knn", neighbors.KNeighborsClassifier()), 
                    ("dt", tree.DecisionTreeClassifier()), 
                    ("svm", svm.SVC())
                ]
                model = getattr(self.__algos[algo], algo)(estimators = estimators, voting="hard")

            else:
                model = getattr(self.__algos[algo], algo)()
            
            # train the model
            model.fit(X, y)
            # prediction time
            y_pred = model.predict(X)
            # store the accuracy/model performance of the model
            self.__acc_score[algo] = accuracy_score(y, y_pred)
            # store the precision score of the model
            self.__precision_scores[algo] = precision_score(y, y_pred)
            # store the recall score of the model
            self.__recall_scores[algo] = recall_score(y, y_pred)
            # store the f1 score of the model
            self.__f1_score[algo] = f1_score(y, y_pred)
            # end the time calculation and store the result
            self.__time_taken[algo] = time.time() - start

    @property
    def get_results_(self, sorting_order: str = "Accuracy", ascending: bool = False) -> pd.DataFrame:
        """
        Summary of the models' performances. This property returns a pandas DataFrame.

        Parameters
        ----------
        sorting_order : str, optional, {"Accuracy", "Precision", "Recall", "F1 Score"} (default = "Accuracy")
            By-default the summary of the models' performance are sorted based on the training accuracy in 
            descending order if the "ascending" parameter is false. But you can change the value.

        ascending : bool, optional, {True, False} (default = False)
            By-default the result will show in descending order. Make it "True" to get in the ascending order.

        Returns
        -------
        Performance of the models as pandas dataframe. 
        """
        data = {
            "Algorithms": list(self.__acc_score.keys()),
            "Time Taken": list(self.__time_taken.values()),
            "Accuracy": list(self.__acc_score.values()),
            "Precision": list(self.__precision_scores.values()),
            "Recall": list(self.__recall_scores.values()),
            "F1 Score": list(self.__f1_score.values())
        }
        return pd.DataFrame(data = data).sort_values(sorting_order, ascending=ascending).reset_index(drop=True)

if __name__ == "__main__":
    titanic_df = pd.read_csv("train.csv")
    titanic_df["Family"] = titanic_df["SibSp"] + titanic_df["Parch"]
    titanic_df = titanic_df[["Survived", "Pclass", "Sex", "Age", "Family", "Fare", "Embarked"]]
    titanic_df = titanic_df.drop(columns = ["Sex", "Embarked"], axis=1)
    titanic_df = titanic_df.dropna()
    X = titanic_df.drop(columns = ["Survived"])
    y = titanic_df["Survived"]

    data = load_breast_cancer()
    X = data.data
    y = data.target
    obj = Classification()
    obj.fit(X, y)
    print(obj.get_results_)
