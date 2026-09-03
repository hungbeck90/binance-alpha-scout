import requests


BASE_URL = "https://api.binance.com"


def get_market_data(symbol="BTCUSDT"):
    symbol = symbol.upper()

    url = f"{BASE_URL}/api/v3/ticker/24hr"

    response = requests.get(
        url,
        params={"symbol": symbol},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return {
        "symbol": data["symbol"],
        "price": float(data["lastPrice"]),
        "change_percent": float(data["priceChangePercent"]),
        "high_24h": float(data["highPrice"]),
        "low_24h": float(data["lowPrice"]),
        "volume": float(data["volume"]),
        "quote_volume": float(data["quoteVolume"]),
    }


if __name__ == "__main__":

    market = get_market_data("BTCUSDT")

    print("\n=== BINANCE ALPHA SCOUT ===")
    print(f"Symbol: {market['symbol']}")
    print(f"Price: ${market['price']:,.2f}")
    print(f"24H Change: {market['change_percent']:.2f}%")
    print(f"24H High: ${market['high_24h']:,.2f}")
    print(f"24H Low: ${market['low_24h']:,.2f}")
    print(f"Volume: {market['volume']:,.2f}")