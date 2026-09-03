from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from agent import analyze_market

app = FastAPI(title="Binance Alpha Scout")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Binance Alpha Scout</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 60px auto;
                background: #0b0e11;
                color: white;
            }

            h1 {
                color: #f0b90b;
            }

            input {
                padding: 12px;
                font-size: 16px;
                width: 250px;
            }

            button {
                padding: 12px 20px;
                font-size: 16px;
                background: #f0b90b;
                border: none;
                cursor: pointer;
                font-weight: bold;
            }

            .card {
                margin-top: 30px;
                background: #181a20;
                padding: 25px;
                border-radius: 12px;
            }
        </style>
    </head>

    <body>

        <h1>Binance Alpha Scout</h1>

        <p>
            AI-powered crypto market research agent built
            with Binance Agent OS.
        </p>

        <input id="symbol" value="BTCUSDT">

        <button onclick="analyze()">
            Analyze Market
        </button>

        <div id="result" class="card">
            Enter a trading pair and click Analyze Market.
        </div>

        <script>
            async function analyze() {

                const symbol =
                    document.getElementById("symbol").value;

                document.getElementById("result").innerHTML =
                    "Analyzing market...";

                const response =
                    await fetch("/analyze?symbol=" + symbol);

                const data = await response.json();

                document.getElementById("result").innerHTML = `
                    <h2>${data.symbol}</h2>

                    <p>
                        <b>Price:</b>
                        $${data.price.toLocaleString()}
                    </p>

                    <p>
                        <b>24H Change:</b>
                        ${data.change_percent.toFixed(2)}%
                    </p>

                    <p>
                        <b>Trend:</b>
                        ${data.trend}
                    </p>

                    <p>
                        <b>Momentum:</b>
                        ${data.momentum}
                    </p>

                    <p>
                        <b>Risk Level:</b>
                        ${data.risk}
                    </p>

                    <p>
                        <b>24H Range Position:</b>
                        ${data.range_position.toFixed(1)}%
                    </p>

                    <hr>

                    <small>
                        Educational market analysis only.
                        Not financial advice.
                    </small>
                `;
            }
        </script>

    </body>
    </html>
    """


@app.get("/analyze")
def analyze(symbol: str = Query(default="BTCUSDT")):
    return analyze_market(symbol.upper())