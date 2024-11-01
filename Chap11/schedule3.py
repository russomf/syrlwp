# schedule3.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Added serial port task with automatic sample scheduling
import asyncio, time, serial

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

async def instrument_to_store(sample, robot, store, instr):
    print(f'({et()}): {robot} started moving {sample} from {instr} to {store}.')
    await asyncio.sleep(1)
    print(f'({et()}): {robot} finished moving {sample} from {instr} to {store}.')

async def store_to_instrument(sample, robot, store, instr):
    print(f'({et()}): {robot} started moving {sample} from {store} to {instr}.')
    await asyncio.sleep(1)
    print(f'({et()}): {robot} finished moving {sample} from {store} to {instr}.')

async def measure_sample(sample, instr):
    print(f'({et()}): {instr} started measuring {sample}.')
    await asyncio.sleep(4)
    print(f'({et()}): {instr} finished measuring {sample}.')

# Run one sample synchronously
async def task_async(sample):
    
    # Wait for resources
    res = await acquire(['robot', 'store', 'instrument'])
    robot, store, instr = res['robot'], res['store'], res['instrument']
    
    # Await move
    await store_to_instrument(sample, robot, store, instr)
    
    # Release resources
    release({'robot':robot, 'store':store})

    # Wait for sample to be measured with given resources
    await measure_sample(sample, instr)

    # Wait for resources
    res = await acquire(['robot', 'store'])
    robot, store = res['robot'], res['store']
    
    # Await move
    await instrument_to_store(sample, robot, store, instr)
    
    # Release resources
    release({'robot':robot, 'store':store, 'instrument': instr})

def sync_function():
    print(f'({et()}): sync_function() start.')
    time.sleep(5)
    print(f'({et()}): sync_function() end.')

# Wait for a barcode and schedule sample for analysis
async def read_and_schedule():
    buff = b''                                      # Init byte buffer
    while True:                                     # Poll serial port
        buff += port.read(100)                      # Read bytes and append to buffer
        idx = buff.find(b'\r')                      # Look for complete barcode
        if idx >= 0:                                # If found...
            barcode = buff[:idx].decode('utf-8')    # Decode barcode
            buff = buff[idx+1:]                     # Strip bytes from front
            loop = asyncio.get_running_loop()       # Get main async event loop           
            loop.create_task( task_async(barcode) ) # Schedule sample
        await asyncio.sleep(1)                      # Asynchronous sleep

if __name__ == '__main__':
    start = time.time()                             # Init timer
    port = serial.Serial('COM4', 115200, timeout=0) # Open port with no timeout
    asyncio.run( read_and_schedule() )              # Get started
    port.close()

# Running a synchronous function in an asynchronus event loop
# This helps us integrate non-asynchronous code into the async framework, for example:
# Legacy libraries that do no have an async implementation
# Functions that block execution
# CPU-bound tasks that must be integrated with IO-bound tasks
# async def sync_function_async():
#     loop = asyncio.get_running_loop()
#     await loop.run_in_executor(None, sync_function) # Runs function in its own thread
    
# Run all samples asynchronously
# async def run_all_async(samples):
#     async with asyncio.TaskGroup() as tg:
#         for samp in samples:
#             tg.create_task( task_async(samp) )

