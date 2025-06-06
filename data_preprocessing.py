import os
import pandas as pd

def load_data(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        data = pd.read_csv(file_path)
    elif ext == ".xlsx":
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Invalid file extension. Only .csv or .xlsx are supported.")
    return data

def handle_missing_values(data, strategy):
    if strategy == "Mean Imputation":
        data = data.fillna(data.mean(numeric_only=True))
        data = data.fillna(data.mode().iloc[0])
    elif strategy == "Drop Rows":
        data = data.dropna()
    elif strategy == "Drop Columns":
        data = data.dropna(axis=1)
    return data

def select_features_and_target(data, feature_cols, target_col):
    X = data[feature_cols].copy()
    y = data[target_col].copy()
    return X, y
