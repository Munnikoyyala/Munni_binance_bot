import os
from dotenv import load_dotenv

# Load .env file if exists
load_dotenv()

def get_api_keys():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    return api_key, api_secret


def validate_symbol(symbol: str) -> bool:
    # Check symbol like BTCUSDT
    return isinstance(symbol, str) and symbol.endswith('USDT') and len(symbol) > 4


def validate_side(side: str) -> bool:
    return side.upper() in ('BUY', 'SELL')


def validate_quantity(qty: str) -> bool:
    try:
        q = float(qty)
        return q > 0
    except Exception:
        return False
