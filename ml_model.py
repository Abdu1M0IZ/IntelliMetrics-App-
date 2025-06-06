import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import (
    RandomForestClassifier, RandomForestRegressor, GradientBoostingRegressor
)
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, r2_score
)

def get_model(task_type, model_name, n_estimators=100, max_depth=None):
    if task_type == "Classification":
        if model_name == "Logistic Regression":
            return LogisticRegression(max_iter=1000)
        elif model_name == "Decision Tree Classifier":
            return DecisionTreeClassifier(max_depth=max_depth)
        elif model_name == "Random Forest Classifier":
            return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
        elif model_name == "K-Nearest Neighbors":
            return KNeighborsClassifier()
    else:
        if model_name == "Linear Regression":
            return LinearRegression()
        elif model_name == "Decision Tree Regressor":
            return DecisionTreeRegressor(max_depth=max_depth)
        elif model_name == "Random Forest Regressor":
            return RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
        elif model_name == "Gradient Boosting Regressor":
            return GradientBoostingRegressor(n_estimators=n_estimators, max_depth=max_depth, learning_rate=0.1)
    return None

def evaluate_classification(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    err_rate = 1 - acc
    prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    sens = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    # Specificity
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
        spec = tn / (tn + fp) if (tn + fp) != 0 else 0
    else:
        spec_values = []
        for i in range(cm.shape[0]):
            tn = np.sum(cm) - np.sum(cm[i, :]) - np.sum(cm[:, i]) + cm[i, i]
            fp = np.sum(cm[:, i]) - cm[i, i]
            spec_values.append(tn / (tn + fp) if (tn + fp) != 0 else 0)
        spec = np.mean(spec_values)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    return {
        'accuracy': acc,
        'error_rate': err_rate,
        'precision': prec,
        'recall': sens,
        'specificity': spec,
        'f1_score': f1,
        'confusion_matrix': cm
    }

def evaluate_regression(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return {
        'mse': mse,
        'rmse': rmse,
        'r2': r2
    }
