# Binance Alpha Scout

Binance Alpha Scout is an AI-powered crypto market research agent built with **Binance Agent OS** and **Binance MCP**.

It retrieves live Binance market data, evaluates market conditions, and produces a concise research report with trend, momentum, risk, and AI-generated insight.

---

## 🚀 What It Does

Users can ask Alpha Scout to analyze trading pairs such as:

- BTCUSDT
- ETHUSDT
- BNBUSDT
- SOLUSDT

The agent retrieves live Binance market data through Binance Agent OS MCP and generates:

- Current price
- 24H percentage change
- 24H high
- 24H low
- 24H volume
- Trend classification
- Momentum classification
- Risk classification
- Short AI market insight

---

## 🧠 Architecture

```text
User
  ↓
AI Agent
  ↓
Binance Agent OS
  ↓
Binance MCP
  ↓
Live Binance Market Data
  ↓
Alpha Scout Reasoning
  ↓
Trend / Momentum / Risk
  ↓
AI Market Insight