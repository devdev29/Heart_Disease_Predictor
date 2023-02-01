import pandas as pd
import numpy as np
import pickle

# Importing the dataset
dataset = pd.read_csv('ML/HD2.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of the missing values
from sklearn.impute import SimpleImputer
inputer = SimpleImputer(missing_values=np.nan, strategy="mean")
inputer.fit(X[:, :15])
X[:, :15] = inputer.transform(X[:, :15])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(
    n_estimators=30, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

with open('./ML/heart_disease_classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)

with open('./ML/scaler.pkl', 'wb') as f:
    pickle.dump(sc, f)