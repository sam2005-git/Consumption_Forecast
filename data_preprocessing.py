# data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    # Fill missing values
    data = data.fillna(data.mean())
    # Scale features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data
