import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
from joblib import dump

# load the diabetes dataset
print("Loading Data...")
diabetes = pd.read_csv('logistic-regression/diabetes.csv')

# separate features and labels
X, y = diabetes[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, diabetes['Diabetic'].values

# split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# set regularization hyperparameter
reg = 0.01

# train a logistic regression model
print('Training a logistic regression model with regularization rate of', reg)
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train, y_train)

# calculate accuracy
y_hat = model.predict(X_test)
print('Accuracy:',accuracy_score(y_test, y_hat))

# calculate AUC
y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test,y_scores[:,1])
print('AUC: ' + str(auc))

# save model
dump(model, 'logistic-regression/diabetes-model.joblib')