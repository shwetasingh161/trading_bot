import logging


def place_market_order(client, symbol, side, quantity):

    logging.info(f"Placing MARKET order {symbol} {side} {quantity}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return order


def place_limit_order(client, symbol, side, quantity, price):

    logging.info(f"Placing LIMIT order {symbol} {side} {quantity} at {price}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    return order