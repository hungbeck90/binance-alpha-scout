from binance_client import get_market_data


def analyze_market(symbol="BTCUSDT"):
    data = get_market_data(symbol)

    change = data["change_percent"]
    price = data["price"]
    high = data["high_24h"]
    low = data["low_24h"]

    # Determine market trend
    if change >= 3:
        trend = "Strong Bullish"
    elif change >= 1:
        trend = "Bullish"
    elif change <= -3:
        trend = "Strong Bearish"
    elif change <= -1:
        trend = "Bearish"
    else:
        trend = "Neutral"

    # Calculate current price position in 24H range
    price_range = high - low

    if price_range > 0:
        range_position = ((price - low) / price_range) * 100
    else:
        range_position = 50

    # Determine momentum
    if range_position >= 75:
        momentum = "Strong"
    elif range_position >= 50:
        momentum = "Positive"
    elif range_position >= 25:
        momentum = "Weak"
    else:
        momentum = "Very Weak"

    # Simple risk assessment
    if abs(change) >= 5:
        risk = "High"
    elif abs(change) >= 2:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        **data,
        "trend": trend,
        "momentum": momentum,
        "risk": risk,
        "range_position": range_position,
    }


def print_report(symbol="BTCUSDT"):
    report = analyze_market(symbol)

    print("\n================================")
    print("      BINANCE ALPHA SCOUT")
    print("================================")

    print(f"\nAsset: {report['symbol']}")
    print(f"Price: ${report['price']:,.2f}")
    print(f"24H Change: {report['change_percent']:.2f}%")

    print("\n--- MARKET ANALYSIS ---")

    print(f"Trend: {report['trend']}")
    print(f"Momentum: {report['momentum']}")
    print(f"Risk Level: {report['risk']}")

    print(
        f"Price Position: "
        f"{report['range_position']:.1f}% of 24H range"
    )

    print("\n--- AGENT INSIGHT ---")

    if report["trend"] in ["Strong Bullish", "Bullish"]:
        print(
            "The asset is showing positive market momentum. "
            "The agent recommends monitoring continuation "
            "and potential volatility."
        )

    elif report["trend"] in ["Strong Bearish", "Bearish"]:
        print(
            "The asset is experiencing negative momentum. "
            "The agent recommends increased caution and "
            "monitoring downside risk."
        )

    else:
        print(
            "The market is currently neutral. "
            "The agent recommends waiting for stronger "
            "directional confirmation."
        )

    print("\nEducational analysis only — not financial advice.")
    print("================================\n")


if __name__ == "__main__":
    print_report("BTCUSDT")