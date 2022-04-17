import asyncio
import websockets
import settings


async def echo(websocket):
    async for message in websocket:
        print(message)
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, settings.WEBSOCKET_HOST, settings.WEBSOCKET_PORT):
        await asyncio.Future()

print(settings.WEBSOCKET_HOST)
asyncio.run(main())