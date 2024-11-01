# schedule4.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Added websocket interface using aiohttp
import asyncio, time, aiohttp, json
from aiohttp import web

routes = web.RouteTableDef()            # Main table of routes
connected = set()                       # Current WebSocket connections

# Resources available
available = {'robot':['Robby'], 'store':['Corner'], 'instrument':['Inst1','Inst2','Inst3']}

# Helper to return elapsed time in fractions of a second
start = time.time()
def et():
    return round(time.time() - start, 1)

# Wait until resource is available and aquire it
async def acquire(resources):
    # Check if one of each resource is available 
    while not all([len(available[res]) > 0 for res in resources]):
        await asyncio.sleep(0.1)
    
    # Acquire the first of each resource and return dictionary
    return {res:available[res].pop(0) for res in resources}

def release(acquired):
    for res in acquired.keys():
        available[res].append(acquired[res])

async def instrument_to_store(sample, robot, store, loc, instr):
    await log(f'({et()}): {robot} started moving {sample} from {instr} to {store} location {loc}.')
    await asyncio.sleep(1)
    await log(f'({et()}): {robot} finished moving {sample} from {instr} to {store} location {loc}.')

async def store_to_instrument(sample, robot, store, loc, instr):
    await log(f'({et()}): {robot} started moving {sample} from {store} location {loc} to {instr}.')
    await asyncio.sleep(1)
    await log(f'({et()}): {robot} finished moving {sample} from {store} location {loc} to {instr}.')

async def measure_sample(sample, instr):
    await log(f'({et()}): {instr} started measuring {sample}.')
    await asyncio.sleep(4)
    await log(f'({et()}): {instr} finished measuring {sample}.')

# Run one sample synchronously
async def task_async(data):
    # Parse data
    items  = json.loads(data)
    sample = items['sample_id']
    loc    = items['sample_location']
    
    # Wait for resources
    res = await acquire(['robot', 'store', 'instrument'])
    robot, store, instr = res['robot'], res['store'], res['instrument']
    
    # Await move
    await store_to_instrument(sample, robot, store, loc, instr)
    
    # Release resources
    release({'robot':robot, 'store':store})

    # Wait for sample to be measured with given resources
    await measure_sample(sample, instr)

    # Wait for resources
    res = await acquire(['robot', 'store'])
    robot, store = res['robot'], res['store']
    
    # Await move
    await instrument_to_store(sample, robot, store, loc, instr)
    
    # Release resources
    release({'robot':robot, 'store':store, 'instrument': instr})

# Respond with main interface page
@routes.get('/')
async def index(req):
    return web.FileResponse('sample_scheduler.html')

# Connect websocket
@routes.get('/ws')
async def websocket_handler(req):
    ws = web.WebSocketResponse()    # Create WebSocket
    await ws.prepare(req)           # Start websocket
    
    connected.add(ws)               # Add WebSocket instance to set
    print(f'Connected: {req.remote} {hash(ws)} ({len(connected)})')
    
    async for msg in ws:            # Broadcast messages
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(f'Received: {msg.data}')
            
            # Schedule sample
            loop = asyncio.get_running_loop()
            loop.create_task( task_async(msg.data) )
            
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'Websocket exception: {ws.exception()}')

    # Close WebSocket, if not already closed, and remove from the set.
    if not ws.closed: ws.close()
    connected.remove(ws)
    print(f'Closed: {hash(ws)} ({len(connected)})')
    return ws

# Log messages
async def log(msg):
    print(msg)
    for _ws in connected:
        if not _ws.closed:
            await _ws.send_str(msg)

# Start HTTP server
if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
