# broadcast.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import aiohttp
from aiohttp import web

routes = web.RouteTableDef()            # Main table of routes
connected = set()                       # Current WebSocket connections

@routes.get('/')                        # Default route
async def index(req):
    return web.FileResponse('ui.html')  # Returns HTML page with WebSocket

@routes.get('/ws')                      # Connect a new websocket
async def websocket_handler(req):
    ws = web.WebSocketResponse()        # Create WebSocket
    await ws.prepare(req)               # Start WebSocket
    
    connected.add(ws)                   # Add WebSocket instance to set
    print(f'Connected: {req.remote} {hash(ws)} ({len(connected)})')
    
    async for msg in ws:                # Broadcast messages
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(f'Received: {msg.data}')
            for _ws in connected:
                if _ws != ws and not _ws.closed:
                    await _ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'Websocket exception: {ws.exception()}')

    # Close WebSocket, if not already closed, and remove from the set.
    if not ws.closed: ws.close()
    connected.remove(ws)
    print(f'Closed: {hash(ws)} ({len(connected)})')
    return ws

# Start HTTP server
if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
