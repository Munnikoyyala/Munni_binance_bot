"""
Place a LIMIT order using command line (demo version).
Usage:
    python src/limit_orders.py BTCUSDT BUY 0.001 62000
"""

import argparse
from logger import get_logger
from utils import get_api_keys, validate_symbol, validate_side, validate_quantity

logger = get_logger('limit_orders')

def place_limit_order(api_key, api_secret, symbol, side, quantity, price):
    """
    This function simulates a limit order placement.
    Later, it can be connected to Binance Testnet for real trades.
    """
    logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
    resp = {
        "orderId": 987654,
        "status": "NEW",
        "symbol": symbol,
        "side": side,
        "price": price,
        "origQty": quantity
    }
    logger.info(f"Order response: {resp}")
    return resp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Place a limit order')
    parser.add_argument('symbol', help='Trading pair, e.g. BTCUSDT')
    parser.add_argument('side', help='BUY or SELL')
    parser.add_argument('quantity', help='Order quantity')
    parser.add_argument('price', help='Limit price')
    args = parser.parse_args()

    # Validate user inputs
    if not validate_symbol(args.symbol):
        logger.error('Invalid symbol. Example valid symbol: BTCUSDT')
        raise SystemExit(1)

    if not validate_side(args.side):
        logger.error('Invalid side. Use BUY or SELL')
        raise SystemExit(1)

    if not validate_quantity(args.quantity):
        logger.error('Invalid quantity. Must be a positive number')
        raise SystemExit(1)

    api_key, api_secret = get_api_keys()
    if not api_key or not api_secret:
        logger.warning('API keys not found. Running in simulated mode.')

    # Place limit order
    place_limit_order(api_key, api_secret, args.symbol.upper(), args.side.upper(), args.quantity, args.price)
