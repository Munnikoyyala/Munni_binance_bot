"""
OCO (One-Cancels-the-Other) Order Simulation

Usage:
    python src/advanced/oco.py BTCUSDT BUY 0.001 65000 59000

This means:
 - Place a Take-Profit (TP) limit order at 65,000
 - Place a Stop-Loss (SL) limit order at 59,000
"""

import argparse
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logger import get_logger
from utils import validate_symbol, validate_side, validate_quantity

logger = get_logger('oco_orders')

def place_oco_order(api_key, api_secret, symbol, side, quantity, take_profit, stop_loss):
    """
    Simulates an OCO order: one take-profit and one stop-loss.
    If one is hit, the other is canceled.
    """
    logger.info(f"Placing OCO order for {symbol} {side} {quantity}")
    logger.info(f"Take-Profit at {take_profit}, Stop-Loss at {stop_loss}")

    # Simulated response
    response = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "take_profit": take_profit,
        "stop_loss": stop_loss,
        "status": "OCO_ORDER_PLACED"
    }

    logger.info(f"OCO order response: {response}")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate an OCO order")
    parser.add_argument("symbol", help="Trading pair symbol, e.g. BTCUSDT")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("quantity", help="Order quantity")
    parser.add_argument("take_profit", help="Take-profit price")
    parser.add_argument("stop_loss", help="Stop-loss price")
    args = parser.parse_args()

    # Validate inputs
    if not validate_symbol(args.symbol):
        logger.error("Invalid symbol.")
        raise SystemExit(1)
    if not validate_side(args.side):
        logger.error("Invalid side. Use BUY or SELL.")
        raise SystemExit(1)
    if not validate_quantity(args.quantity):
        logger.error("Invalid quantity.")
        raise SystemExit(1)

    place_oco_order(None, None, args.symbol.upper(), args.side.upper(), args.quantity, args.take_profit, args.stop_loss)
