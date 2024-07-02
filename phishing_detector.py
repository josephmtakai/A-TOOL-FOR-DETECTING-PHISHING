import joblib
import re
import numpy as np

# Load the trained model
clf = joblib.load('phishing_detector.pkl')

# Feature extraction function
def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(url.count('.'))  # Number of dots
    features.append(int('https' in url))  # Use of HTTPS
    features.append(len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', url)))  # Special characters count
    return features

# Function to predict if a URL is phishing
def predict_phishing(url):
    features = np.array(extract_features(url)).reshape(1, -1)
    prediction = clf.predict(features)
    return 'Phishing' if prediction == 1 else 'Legitimate'

# Test the tool
url = input('Enter a URL to check: ')
result = predict_phishing(url)
print(f'The URL is {result}')
