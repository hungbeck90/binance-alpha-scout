from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from agent import analyze_market

app = FastAPI(
    title="Binance Alpha Scout",
    description="AI-powered crypto market research companion.",
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Binance Alpha Scout</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;

            background:
                radial-gradient(
                    circle at top right,
                    rgba(240, 185, 11, 0.12),
                    transparent 32%
                ),
                #0b0e11;

            color: #f5f5f5;
        }

        .container {
            width: min(1120px, 92%);
            margin: 0 auto;
            padding: 42px 0 70px;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 45px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            font-size: 20px;
        }

        .logo {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            background: #f0b90b;
            color: #0b0e11;
            display: grid;
            place-items: center;
            font-weight: 900;
        }

        .status {
            display: inline-flex;
            align-items: center;
            gap: 8px;

            padding: 8px 12px;

            border: 1px solid #2b3139;
            border-radius: 999px;

            background: #181a20;
            color: #b7bdc6;

            font-size: 13px;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #0ecb81;
            box-shadow: 0 0 12px rgba(14, 203, 129, 0.65);
        }

        .hero {
            max-width: 820px;
            margin-bottom: 34px;
        }

        .eyebrow {
            color: #f0b90b;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        h1 {
            margin: 0;
            font-size: clamp(38px, 7vw, 68px);
            line-height: 1;
            letter-spacing: -2px;
        }

        .hero p {
            color: #929aa5;
            line-height: 1.7;
            font-size: 17px;
            max-width: 730px;
            margin-top: 20px;
        }

        .search-panel {
            background: rgba(24, 26, 32, 0.92);
            border: 1px solid #2b3139;
            border-radius: 18px;

            padding: 18px;

            display: flex;
            gap: 12px;

            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.25);
        }

        input {
            flex: 1;
            min-width: 0;

            padding: 16px 18px;

            color: white;
            background: #0b0e11;

            border: 1px solid #333943;
            border-radius: 12px;

            outline: none;

            font-size: 16px;
            font-weight: 700;

            text-transform: uppercase;
        }

        input:focus {
            border-color: #f0b90b;
            box-shadow: 0 0 0 3px rgba(240, 185, 11, 0.10);
        }

        button {
            border: none;
            border-radius: 12px;

            padding: 0 26px;

            background: #f0b90b;
            color: #101014;

            font-size: 15px;
            font-weight: 900;

            cursor: pointer;

            transition:
                transform 0.15s ease,
                opacity 0.15s ease;
        }

        button:hover {
            transform: translateY(-1px);
        }

        button:disabled {
            opacity: 0.55;
            cursor: wait;
        }

        .quick {
            display: flex;
            gap: 9px;
            flex-wrap: wrap;

            margin-top: 13px;
        }

        .quick button {
            background: #181a20;
            border: 1px solid #2b3139;

            color: #b7bdc6;

            padding: 8px 13px;

            font-size: 12px;
        }

        .quick button:hover {
            color: white;
            border-color: #f0b90b;
        }

        .result {
            margin-top: 28px;
        }

        .empty-state {
            padding: 55px 30px;

            text-align: center;

            background: #181a20;
            border: 1px solid #2b3139;
            border-radius: 18px;

            color: #848e9c;
        }

        .report {
            display: none;
        }

        .report-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 20px;

            margin-bottom: 18px;
        }

        .symbol {
            font-size: 28px;
            font-weight: 900;
        }

        .price {
            margin-top: 5px;

            font-size: 39px;
            font-weight: 800;

            letter-spacing: -1px;
        }

        .change {
            margin-top: 8px;
            font-size: 15px;
            font-weight: 800;
        }

        .positive {
            color: #0ecb81;
        }

        .negative {
            color: #f6465d;
        }

        .neutral {
            color: #f0b90b;
        }

        .source-badge {
            padding: 9px 12px;

            color: #f0b90b;
            background: rgba(240, 185, 11, 0.08);

            border: 1px solid rgba(240, 185, 11, 0.22);
            border-radius: 10px;

            font-size: 12px;
            font-weight: 800;

            text-align: center;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
        }

        .metric {
            background: #181a20;

            border: 1px solid #2b3139;
            border-radius: 16px;

            padding: 21px;
        }

        .metric-label {
            color: #848e9c;

            font-size: 12px;
            font-weight: 700;

            text-transform: uppercase;
            letter-spacing: 0.7px;
        }

        .metric-value {
            margin-top: 9px;

            font-size: 22px;
            font-weight: 900;
        }

        .range-card {
            margin-top: 14px;

            background: #181a20;
            border: 1px solid #2b3139;
            border-radius: 16px;

            padding: 22px;
        }

        .range-row {
            display: flex;
            justify-content: space-between;
            gap: 20px;

            margin-bottom: 12px;
        }

        .range-track {
            height: 9px;

            background: #2b3139;

            border-radius: 999px;
            overflow: hidden;
        }

        .range-fill {
            width: 0%;
            height: 100%;

            background: linear-gradient(
                90deg,
                #f0b90b,
                #ffd84d
            );

            border-radius: 999px;

            transition: width 0.5s ease;
        }

        .insight {
            margin-top: 14px;

            padding: 24px;

            background:
                linear-gradient(
                    135deg,
                    rgba(240, 185, 11, 0.09),
                    rgba(24, 26, 32, 1)
                );

            border: 1px solid rgba(240, 185, 11, 0.20);
            border-radius: 16px;
        }

        .insight-title {
            color: #f0b90b;

            font-weight: 900;
            margin-bottom: 10px;
        }

        .insight p {
            margin: 0;

            color: #d6d9dd;

            line-height: 1.65;
        }

        .architecture {
            margin-top: 38px;

            padding-top: 26px;

            border-top: 1px solid #232830;
        }

        .architecture-title {
            color: #848e9c;

            font-size: 12px;
            font-weight: 800;

            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .pipeline {
            display: flex;
            align-items: center;
            gap: 9px;
            flex-wrap: wrap;

            margin-top: 15px;

            color: #929aa5;
            font-size: 13px;
        }

        .pipeline span {
            padding: 8px 11px;

            background: #181a20;

            border: 1px solid #2b3139;
            border-radius: 9px;
        }

        .arrow {
            color: #f0b90b;
        }

        .note {
            margin-top: 25px;

            color: #5e6673;
            font-size: 12px;
            line-height: 1.6;
        }

        .error {
            display: none;

            margin-top: 20px;

            padding: 18px;

            background: rgba(246, 70, 93, 0.08);

            color: #f6465d;

            border: 1px solid rgba(246, 70, 93, 0.25);
            border-radius: 12px;
        }

        @media (max-width: 760px) {
            .topbar {
                align-items: flex-start;
                flex-direction: column;
            }

            .search-panel {
                flex-direction: column;
            }

            button {
                padding: 15px;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .report-header {
                flex-direction: column;
            }
        }
    </style>
</head>


<body>

<div class="container">

    <div class="topbar">

        <div class="brand">
            <div class="logo">A</div>
            Binance Alpha Scout
        </div>

        <div class="status">
            <span class="status-dot"></span>
            Alpha Scout Online
        </div>

    </div>


    <section class="hero">

        <div class="eyebrow">
            AI Market Intelligence
        </div>

        <h1>
            Scout the market.<br>
            Understand the signal.
        </h1>

        <p>
            Binance Alpha Scout transforms live crypto market data
            into a concise research snapshot covering trend,
            momentum, risk and market positioning.
        </p>

    </section>


    <section>

        <div class="search-panel">

            <input
                id="symbol"
                value="BTCUSDT"
                placeholder="Enter symbol e.g. BTCUSDT"
                autocomplete="off"
            >

            <button id="analyzeBtn" onclick="analyze()">
                Analyze Market
            </button>

        </div>


        <div class="quick">

            <button onclick="quickAnalyze('BTCUSDT')">
                BTCUSDT
            </button>

            <button onclick="quickAnalyze('ETHUSDT')">
                ETHUSDT
            </button>

            <button onclick="quickAnalyze('BNBUSDT')">
                BNBUSDT
            </button>

            <button onclick="quickAnalyze('SOLUSDT')">
                SOLUSDT
            </button>

        </div>

    </section>


    <div id="error" class="error"></div>


    <section class="result">

        <div id="empty" class="empty-state">

            <strong>Ready to scout.</strong>

            <p>
                Choose a trading pair and run Alpha Scout analysis.
            </p>

        </div>


        <div id="report" class="report">

            <div class="report-header">

                <div>

                    <div
                        id="reportSymbol"
                        class="symbol">
                        BTCUSDT
                    </div>

                    <div
                        id="reportPrice"
                        class="price">
                        $0
                    </div>

                    <div
                        id="reportChange"
                        class="change">
                        0%
                    </div>

                </div>


                <div class="source-badge">
                    COMPANION DASHBOARD<br>
                    BINANCE MARKET DATA
                </div>

            </div>


            <div class="grid">

                <div class="metric">

                    <div class="metric-label">
                        Trend
                    </div>

                    <div
                        id="trend"
                        class="metric-value">
                        —
                    </div>

                </div>


                <div class="metric">

                    <div class="metric-label">
                        Momentum
                    </div>

                    <div
                        id="momentum"
                        class="metric-value">
                        —
                    </div>

                </div>


                <div class="metric">

                    <div class="metric-label">
                        Risk Level
                    </div>

                    <div
                        id="risk"
                        class="metric-value">
                        —
                    </div>

                </div>

            </div>


            <div class="range-card">

                <div class="range-row">

                    <span>
                        24H Range Position
                    </span>

                    <strong id="rangeText">
                        0%
                    </strong>

                </div>


                <div class="range-track">

                    <div
                        id="rangeFill"
                        class="range-fill">
                    </div>

                </div>

            </div>


            <div class="insight">

                <div class="insight-title">
                    ✦ Alpha Scout Insight
                </div>

                <p id="insightText">
                    Waiting for market analysis.
                </p>

            </div>

        </div>

    </section>


    <section class="architecture">

        <div class="architecture-title">
            Agent OS Architecture
        </div>

        <div class="pipeline">

            <span>AI Agent</span>

            <div class="arrow">→</div>

            <span>Binance Agent OS</span>

            <div class="arrow">→</div>

            <span>Binance MCP</span>

            <div class="arrow">→</div>

            <span>Market Data</span>

            <div class="arrow">→</div>

            <span>Alpha Scout Reasoning</span>

        </div>

    </section>


    <div class="note">

        Companion dashboard for Binance Alpha Scout.
        The Agent OS workflow uses Binance MCP in the supported
        AI-agent environment. This dashboard provides a visual
        prototype of the market-analysis experience.

        <br><br>

        Educational market analysis only.
        Not financial advice.

    </div>

</div>


<script>

    const symbolInput =
        document.getElementById("symbol");

    symbolInput.addEventListener(
        "keydown",
        function(event) {

            if (event.key === "Enter") {
                analyze();
            }

        }
    );


    function quickAnalyze(symbol) {

        symbolInput.value = symbol;

        analyze();

    }


    function insightFor(data) {

        const change =
            data.change_percent.toFixed(2);

        const position =
            data.range_position.toFixed(1);

        let directionText;

        if (data.change_percent > 0) {

            directionText =
                `${data.symbol} is trading higher over the last 24 hours, ` +
                `with a ${change}% move.`;

        } else if (data.change_percent < 0) {

            directionText =
                `${data.symbol} is trading lower over the last 24 hours, ` +
                `with a ${change}% move.`;

        } else {

            directionText =
                `${data.symbol} is showing limited directional movement ` +
                `over the last 24 hours.`;

        }


        return (
            `${directionText} ` +
            `Alpha Scout classifies the current trend as ` +
            `${data.trend}, momentum as ${data.momentum}, ` +
            `and risk as ${data.risk}. ` +
            `Price is positioned at approximately ` +
            `${position}% of its 24-hour range.`
        );

    }


    async function analyze() {

        const symbol =
            symbolInput.value
                .trim()
                .toUpperCase();

        const analyzeBtn =
            document.getElementById("analyzeBtn");

        const errorBox =
            document.getElementById("error");


        if (!symbol) {

            errorBox.style.display = "block";

            errorBox.textContent =
                "Please enter a trading pair.";

            return;

        }


        errorBox.style.display = "none";

        analyzeBtn.disabled = true;

        analyzeBtn.textContent =
            "Scouting...";


        try {

            const response =
                await fetch(
                    "/analyze?symbol=" +
                    encodeURIComponent(symbol)
                );


            if (!response.ok) {

                throw new Error(
                    "Unable to retrieve market data."
                );

            }


            const data =
                await response.json();


            if (
                data.price === undefined ||
                data.change_percent === undefined
            ) {

                throw new Error(
                    "Unexpected market data response."
                );

            }


            document.getElementById("empty")
                .style.display =
                "none";

            document.getElementById("report")
                .style.display =
                "block";


            document.getElementById("reportSymbol")
                .textContent =
                data.symbol;


            document.getElementById("reportPrice")
                .textContent =
                "$" +
                Number(data.price)
                    .toLocaleString(
                        undefined,
                        {
                            maximumFractionDigits: 8
                        }
                    );


            const changeElement =
                document.getElementById(
                    "reportChange"
                );


            const prefix =
                data.change_percent > 0
                    ? "+"
                    : "";


            changeElement.textContent =
                prefix +
                data.change_percent.toFixed(2) +
                "% · 24H";


            changeElement.className =
                "change " +
                (
                    data.change_percent > 0
                        ? "positive"
                        : data.change_percent < 0
                            ? "negative"
                            : "neutral"
                );


            document.getElementById("trend")
                .textContent =
                data.trend;


            document.getElementById("momentum")
                .textContent =
                data.momentum;


            document.getElementById("risk")
                .textContent =
                data.risk;


            const range =
                Math.max(
                    0,
                    Math.min(
                        100,
                        Number(
                            data.range_position
                        )
                    )
                );


            document.getElementById("rangeText")
                .textContent =
                range.toFixed(1) + "%";


            document.getElementById("rangeFill")
                .style.width =
                range + "%";


            document.getElementById("insightText")
                .textContent =
                insightFor(data);

        }

        catch (error) {

            document.getElementById("report")
                .style.display =
                "none";

            document.getElementById("empty")
                .style.display =
                "block";

            errorBox.style.display =
                "block";

            errorBox.textContent =
                error.message +
                " Check the trading pair and try again.";

        }

        finally {

            analyzeBtn.disabled =
                false;

            analyzeBtn.textContent =
                "Analyze Market";

        }

    }

</script>

</body>
</html>
"""


@app.get("/analyze")
def analyze(symbol: str = Query(default="BTCUSDT")):
    return analyze_market(symbol.upper())