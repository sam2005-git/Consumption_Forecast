# tests/unit_tests.py
import unittest
from forecast_model import load_data, train_model

class TestForecastModel(unittest.TestCase):
    def test_load_data(self):
        data = load_data('data/consumption_data.csv')
        self.assertIsNotNone(data)

    def test_train_model(self):
        data = load_data('data/consumption_data.csv')
        model = train_model(data)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
