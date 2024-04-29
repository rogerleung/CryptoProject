#! /usr/bin/python

"""unicorn-binance_websocket_test.py:

Example script that uses the library 'unicorn_binance_websocket_api' to listen
to multiple streams on a binance websocket.
https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api
"""
import signal
from typing import Type, Any
from pprint import pprint, pformat
import time
from unicorn_binance_websocket_api import BinanceWebSocketApiManager


def process_new_receives(stream_data: Any,
                         stream_buffer_name: bool = False) -> None:
    pprint(stream_data)


def start_ubwa() -> Type[BinanceWebSocketApiManager]:
    ubwa = BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['kline_15m'], ['btcusdt', 'ethbtc'],
                       process_stream_data=process_new_receives)
    return ubwa


if __name__ == "__main__":
    try:
        ubwa = start_ubwa()
        while True:
            print("###main thread is working###")
            time.sleep(5)
    except KeyboardInterrupt:
        # Ignore further keyboard interrupts.
        s = signal.signal(signal.SIGINT, signal.SIG_IGN)
        # Close WebSocketApiManager (stops all streams + monitoring API).
        ubwa.stop_manager_with_all_streams()
        time.sleep(2)  # Just so stream logger can process last message...
        # Restore keyboard interrupts.
        signal.signal(signal.SIGINT, s)
    finally:
        print("Exiting program.")
        SystemExit(0)