import websockets

async def receive_data(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            # Receive data from the WebSocket
            data = await websocket.recv()
            print(f"Received data: {data}")

import nest_asyncio
nest_asyncio.apply()