# binance_futures_trading_bot.py

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# 🔐 Dummy API keys (replace with real ones after KYC)
api_key = "DUMMY_API_KEY_123456"
api_secret = "DUMMY_SECRET_KEY_654321"

# 🔗 Connect to Binance Futures Testnet
client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

def place_order(symbol, side, order_type, quantity):
    print("\n📦 Order Summary:")
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_MARKET if order_type == "MARKET" else ORDER_TYPE_LIMIT,
            quantity=quantity,
            price="30000" if order_type == "LIMIT" else None,
            timeInForce="GTC" if order_type == "LIMIT" else None
        )
        print("✅ Order placed successfully!")
        print(order)
    except BinanceAPIException as e:
        print(f"❌ Binance API Error: {e.message}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    print("🔁 Binance Futures Trading Bot (Testnet Version)\n")
    
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Order type (MARKET or LIMIT): ").upper()
    quantity_input = input("Enter quantity (e.g., 0.001): ")

    try:
        quantity = float(quantity_input)
        place_order(symbol, side, order_type, quantity)
    except ValueError:
        print("❌ Quantity must be a number!")

if __name__ == "__main__":
    main()


