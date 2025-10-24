"""
Place a MARKET order using command line (demo version).
Usage:
    python src/market_orders.py BTCUSDT BUY 0.001
"""

import argparse
from logger import get_logger
from utils import get_api_keys, validate_symbol, validate_side, validate_quantity

logger = get_logger('market_orders')

def place_market_order(api_key, api_secret, symbol, side, quantity):
    """
    This function simulates a market order placement.
    Later you can replace this with Binance API code.
    """
    logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")
    # Simulated response
    resp = {
        "orderId": 123456,
        "status": "FILLED",
        "symbol": symbol,
        "side": side,
        "executedQty": quantity
    }
    logger.info(f"Order response: {resp}")
    return resp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Place a market order')
    parser.add_argument('symbol', help='Trading pair symbol, e.g., BTCUSDT')
    parser.add_argument('side', help='BUY or SELL')
    parser.add_argument('quantity', help='Order quantity')
    args = parser.parse_args()

    # Validate inputs
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

    # Place order
    place_market_order(api_key, api_secret, args.symbol.upper(), args.side.upper(), args.quantity)
