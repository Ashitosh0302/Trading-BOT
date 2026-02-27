from flask import Flask, render_template, request
import os
from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.logging_config import setup_logger

app = Flask(__name__)

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            symbol = request.form["symbol"]
            side = request.form["side"]
            order_type = request.form["type"]
            quantity = float(request.form["quantity"])
            price = request.form.get("price")

            price = float(price) if price else None

            log_file = "market_order.log" if order_type == "MARKET" else "limit_order.log"
            logger = setup_logger("web_bot", log_file)

            client = BinanceFuturesClient(API_KEY, API_SECRET)

            response = create_order(
                client,
                symbol,
                side,
                order_type,
                quantity,
                price
            )

            result = {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice")
            }

            logger.info(response)

        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run()