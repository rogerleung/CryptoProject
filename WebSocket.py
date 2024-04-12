# WebSocket Stream Client
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient
import logging
import time

def message_handler(_, message):
    logging.info(message)

my_client = SpotWebsocketStreamClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()