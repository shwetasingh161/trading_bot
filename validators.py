import argparse
import os

from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import *
from bot.logging_config import setup_logger


def main():

    logger = setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        client = BinanceClient(api_key, api_secret).get_client()

        print("\nOrder Request Summary")
        print("--------------------")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)

        if args.type == "MARKET":

            response = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            if not args.price:
                raise ValueError("LIMIT order requires price")

            response = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nOrder Response")
        print("----------------")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

        logger.info(response)

        print("\nOrder placed successfully!")

    except Exception as e:

        logger.error(str(e))
        print("Order failed:", str(e))


if __name__ == "__main__":
    main()