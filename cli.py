import argparse
import logging

logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

print("\nOrder Request Summary")
print("---------------------")
print("Symbol:", args.symbol)
print("Side:", args.side)
print("Type:", args.type)
print("Quantity:", args.quantity)

if args.price:
    print("Price:", args.price)

logging.info(
    f"Order placed: {args.symbol} {args.side} {args.type} qty={args.quantity} price={args.price}"
)

print("\nOrder placed successfully (test mode)")