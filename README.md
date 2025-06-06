# IntelliMetrics-App-
Python-based ML pipeline using Pandas, scikit-learn, and Matplotlib to automate data ingestion,  imputation, feature selection, and model training for both classification and regression.

1. Overview
IntelliMetrics App is a graphical application (built in Python with Tkinter and various data science libraries) that allows users to:
1.	Upload a dataset (CSV or Excel –.xlsx).
2.	Handle missing values with various strategies (Drop Rows, Columns, or Mean Imputation).
3.	Select features and target variables.
4.	Choose a task type (Classification or Regression).
5.	Pick a machine learning model (e.g., Logistic Regression, Decision Tree, Random Forest, KNN for classification; Linear Regression, Decision Tree, Random Forest, Gradient Boosting for regression).
6.	Train and evaluate the model with automatically generated metrics and plots.

Libraries Required:
•	Os
•	Pathlib
•	Pandas
•	NumPy 
•	Scikit-learn 
•	Matplotlib 
•	Seaborn
•	OpenPyXL
•	Pillow

2. User Interface
 
3. Key Functionalities
a)	Upload Data
•	Action: Click the "Upload File" button.
•	 Supported Formats: .csv, .xlsx.
•	Outcome: Displays dataset size and previews column names.

b)	Handle Missing Values
•	Options:
o	Drop Rows: Remove rows with missing data.
o	Drop Columns: Remove columns with missing data.
o	Mean Imputation: Fill missing numeric values with the column mean.
•	Action: Select a strategy from the dropdown and apply.

c)	Select Features & Target
•	Features: Select one or more columns as input features.
•	Target: Choose a single column to predict.
•	Action: Use the multi-select list for features and dropdown for the target.

d)	Choose Model
•	Task Type: Select Classification or Regression.
•	Model Options:
o	Classification: Logistic Regression, Decision Tree, Random Forest, KNN.
o	Regression: Linear Regression, Decision Tree, Random Forest, Gradient Boosting.
•	Action: Choose the desired model from the dropdown.

e)	 Train & Evaluate
•	Action: Click the "Train Model" button.
•	Outcome: Displays evaluation metrics and relevant plots.


4. Evaluation Metrics

a)	 Classification Metrics
•	Accuracy: Proportion of correct predictions.
•	Error Rate: Proportion of incorrect predictions.
•	Confusion Matrix: Shows true vs. predicted classifications.
•	Precision: Accuracy of positive predictions.
•	Recall (Sensitivity): Ability to find all positive instances.
•	Specificity: Ability to identify negative instances correctly.
•	F1 Score: Balance between precision and recall.

b)	 Regression Metrics
•	Mean Squared Error (MSE): Average squared difference between actual and predicted values.
•	Root Mean Squared Error (RMSE): Square root of MSE, in the same units as the target.
•	R-Squared (R²): Proportion of variance explained by the model.


5. Example Scenarios – Iris Dataset 



Upload Dataset










Handling Missing Values
(Mean Imputation)











Selecting Features and Target











Choosing Model













Train and Evaluate

















6. Regression Analysis Comparison:
1.	Linear Regression:
mse: 0.1667
rmse: 0.4083
r2: 0.7584






2.	Decision Tree Regressor:
mse: 0.3024
rmse: 0.5499
r2: 0.5619






3.	Random Forest Regressor:
mse: 0.2554
rmse: 0.5053
r2: 0.6300






4.	Gradient Boosting Regressor:

mse: 0.3024
rmse: 0.5499
r2: 0.5619



The Linear Regression model performed the best on the Iris dataset, achieving the lowest MSE and RMSE, while also yielding the highest R².
