import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class Classification:
    def __init__(self) -> None:
        # define the models with base parameters
        self.__logistic_reg = LogisticRegression()
        self.__decision_tree = DecisionTreeClassifier()
        self.__random_forest = RandomForestClassifier()

        # store the performance of the models
        self.__acc_score = {}
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if type(X) != np.ndarray or type(y) != np.ndarray:
            raise TypeError("The X and y should be NumPy array")
        elif X.shape[0] != y.shape[0]:
            raise ValueError("The dependent and independent variables should have same number of records.")

        # logistic regression
        self.__logistic_reg.fit(X, y)
        logistic_reg_accuracy = accuracy_score(y, self.__logistic_reg.predict(X))
        self.__acc_score["LogisticRegression"] = logistic_reg_accuracy

        # decision tree classifier
        self.__decision_tree.fit(X, y)
        decision_tree_accuracy = accuracy_score(y, self.__decision_tree.predict(X))
        self.__acc_score["DecisionTreeClassifier"] = decision_tree_accuracy

        # random forest classifier
        self.__random_forest.fit(X, y)
        random_forest_accuracy = accuracy_score(y, self.__random_forest.predict(X))
        self.__acc_score["RandomForestClassifier"] = random_forest_accuracy

        return self.__acc_score
