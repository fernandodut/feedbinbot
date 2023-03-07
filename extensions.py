import websocket  # pip3 install websocket-client
# import json
# import pandas as pd

# df = pd.DataFrame()


def on_message(ws, message):
    # global df
    # out = json.loads(message)
    # # out = pd.DataFrame({'price': float(out['c'])}, index=[
    # #                    pd.to_datetime(out['E'], unit='ms')])
    # out = pd.DataFrame({
    #     # "e": "24hrTicker",        # Event type
    #     # "E": 1672515782136,       # Event time
    #     'symbol': out['s'],         # Symbol
    #     'price': float(out['c']),   # Last price
    #     'price_change': float(out['p']),  # Price change
    #     "price_change_percent": float(out["P"]),      # Price change percent
    #     # Weighted average price
    #     "weighted_average_price": float(out["w"]),
    #     # First trade(F)-1 price (first trade before the 24hr rolling window)
    #     "first_trade": float(out["x"]),
    #     "last_quantity": float(out["Q"]),          # Last quantity
    #     "best_bid_price": float(out["b"]),      # Best bid price
    #     "best_bid_quantity": float(out["B"]),          # Best bid quantity
    #     "best_ask_price": float(out["a"]),      # Best ask price
    #     "best_ask_quantity": float(out["A"]),         # Best ask quantity
    #     "open_price": float(out["o"]),      # Open price
    #     "high_price": float(out["h"]),      # High price
    #     "low_price": float(out["l"]),      # Low price
    #     # Total traded base asset volume
    #     "total_traded_base": float(out["v"]),
    #     # Total traded quote asset volume
    #     "total_traded_quote": float(out["q"]),
    #     # Statistics open time
    #     # "statistics_open_time": pd.to_datetime(out["O"], unit='ms'),
    #     # Statistics close time
    #     # "statistics_close_time": pd.to_datetime(out["C"], unit='ms'),
    #     # "first_trade_ID": float(out["F"]),             # First trade ID
    #     # "last_trade_Id": float(out["L"]),         # Last trade Id
    #     # Total number of trades
    #     "total_number_of_trades": float(out["n"])
    # },
    #     index=[pd.to_datetime(out['E'], unit='ms')])  # Event time
    # df = pd.concat([df, out], axis=0)
    # print(df)
    # df = df.tail(1)
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### CLOSED ###"*7)


def on_open(ws):
    print("BOT RUNNING || PRESS \"ctrl+C\" TO STOP")
    ws.send(our_msg)


def run_forever(ws):
    endpoint = 'wss://stream.binance.com:9443/ws'
    # endpoint = 'wss://api.gemini.com/v1/marketdata/BTCUSD'
    our_msg = json.dumps({
        'method': 'SUBSCRIBE',
        'params': ['btcusdt@ticker'],
        'id': 1
    })
    ws = websocket.WebSocketApp(
        endpoint,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)

    # ws.run_forever()
