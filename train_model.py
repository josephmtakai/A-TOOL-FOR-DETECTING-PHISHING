import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import re
import joblib
import os

# Check if the dataset exists
file_path = 'urls.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist. Please ensure the dataset is in the correct location.")

# Load the dataset
data = pd.read_csv(file_path)

# Feature extraction function
def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(url.count('.'))  # Number of dots
    features.append(int('https' in url))  # Use of HTTPS
    features.append(len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', url)))  # Special characters count
    return features

# Apply feature extraction to the dataset
X = np.array([extract_features(url) for url in data['url']])
y = data['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Save the trained model
model_path = 'phishing_detector.pkl'
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")
