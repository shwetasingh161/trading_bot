# Binance Futures Testnet Trading Bot

This project is a simple Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Market Orders
- Limit Orders
- BUY and SELL support
- CLI input validation
- Logging of API requests and errors

## Setup

1. Install dependencies

pip install -r requirements.txt

2. Set API keys

set BINANCE_API_KEY=your_api_key
set BINANCE_API_SECRET=your_secret_key

3. Run examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000