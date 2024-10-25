# tests/selenium_test.py
from selenium import webdriver
import unittest

class TestWebInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_forecast_page_load(self):
        self.driver.get('http://localhost:5000')  # Replace with actual URL
        self.assertIn("Forecast", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
