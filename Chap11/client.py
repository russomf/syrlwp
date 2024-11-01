# client.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio
import aiohttp

# Server address
URL = "ws://localhost:8080/ws"

# Create client WebSocket and connect.
# Start async methods to manage connection send and receive.
async def main():
    client = aiohttp.ClientSession()
    async with client.ws_connect(URL) as ws:
        await asyncio.gather( incoming(ws), outgoing(ws) )

# Handle incoming messages
async def incoming(ws):
    async for msg in ws:
        # Print received message and re-prompt user.
        print(f'\nReceived: {msg.data}\nEnter command: ', end='')

        # Close connection
        if msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
            break

# Prompt and send outgoing messages
async def outgoing(ws):
    while True:
        msg = await asyncio.to_thread(input, "Enter command: ")
        await ws.send_str(msg)

if __name__ == '__main__':
    asyncio.run( main() )

# async def prompt_and_send(ws):
#     new_msg_to_send = input('Type a message to send to the server: ')
#     if new_msg_to_send == 'exit':
#         print('Exiting!')
#         raise SystemExit(0)
#     await ws.send_str(new_msg_to_send)

# async def main():
#     session = aiohttp.ClientSession()
#     async with session.ws_connect(URL) as ws:

#         # await prompt_and_send(ws)
        
#         async for msg in ws:
#             print('Message received from server:', msg)
#             await prompt_and_send(ws)

#             if msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
#                 break

# if __name__ == '__main__':
#     # print('Type "exit" to quit')
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(main())
#     asyncio.run( main() )
