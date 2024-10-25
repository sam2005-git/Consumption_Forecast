# forecast_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump, load

# Load and preprocess data
def load_data(path):
    data = pd.read_csv(path)
    # Add any necessary preprocessing steps
    return data

# Train model
def train_model(data):
    X = data[['feature1', 'feature2']]  # replace with actual features
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    dump(model, 'model.joblib')  # Save the model
    return model

# Make predictions
def predict(model, X):
    return model.predict(X)

if __name__ == "__main__":
    data = load_data('data/consumption_data.csv')
    model = train_model(data)
    print("Model training complete. Model saved as 'model.joblib'")
