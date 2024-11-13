import requests
import pandas as pd
from sqlalchemy import create_engine
import os

# URL de l'API CoinGecko pour récupérer les informations de cryptomonnaies
COIN_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/mydatabase")

def extract_data():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(COIN_API_URL, params=params)
    data = response.json()
    return data

def transform_data(data):
    # Transformation des données en DataFrame
    crypto_data = {
        "name": [coin["name"] for coin in data],
        "symbol": [coin["symbol"] for coin in data],
        "current_price": [coin["current_price"] for coin in data],
        "market_cap": [coin["market_cap"] for coin in data],
        "total_volume": [coin["total_volume"] for coin in data],
        "high_24h": [coin["high_24h"] for coin in data],
        "low_24h": [coin["low_24h"] for coin in data]
    }
    df = pd.DataFrame(crypto_data)
    return df

def load_data(df):
    # Charger les données dans PostgreSQL
    engine = create_engine(DATABASE_URL)
    df.to_sql("crypto_data", engine, if_exists="replace", index=False)
    print("Données de cryptomonnaies chargées dans la base de données")

if __name__ == "__main__":
    data = extract_data()
    df = transform_data(data)
    load_data(df)
