import argparse
import os
from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.logging_config import setup_logger

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    log_file = "market_order.log" if args.type == "MARKET" else "limit_order.log"
    logger = setup_logger("trading_bot", log_file)

    try:
        client = BinanceFuturesClient(API_KEY, API_SECRET)

        print("\nOrder Request:")
        print(vars(args))

        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Response:")
        print({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        })

        logger.info(f"Order Success: {response}")

    except Exception as e:
        logger.error(str(e))
        print("Order Failed:", str(e))

if __name__ == "__main__":
    main()