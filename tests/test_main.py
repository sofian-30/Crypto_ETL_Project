# tests/test_main.py

import unittest
from main import extract_data, transform_data
import pandas as pd

class TestCryptoETL(unittest.TestCase):

    def test_extract_data(self):
        data = extract_data()
        # Vérifie si les données extraites sont une liste de dictionnaires
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertIn("name", data[0])

    def test_transform_data(self):
        # Simule des données similaires aux données extraites
        sample_data = [
            {
                "name": "Bitcoin",
                "symbol": "btc",
                "current_price": 50000,
                "market_cap": 1000000000,
                "total_volume": 200000000,
                "high_24h": 50500,
                "low_24h": 49500
            }
        ]
        df = transform_data(sample_data)
        # Vérifie que le DataFrame est bien formaté
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), ["name", "symbol", "current_price", "market_cap", "total_volume", "high_24h", "low_24h"])
        self.assertEqual(df.iloc[0]["name"], "Bitcoin")

if __name__ == "__main__":
    unittest.main()
