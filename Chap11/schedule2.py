# schedule2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio, time

# Resources available
# available = {'robot':['Robby'], 'store':['Corner'], 'instrument':['Inst1']}
# available = {'robot':['Robby'], 'store':['Corner'], 'instrument':['Inst1','Inst2']}
available = {'robot':['Robby'], 'store':['Corner'], 'instrument':['Inst1','Inst2','Inst3']}

# Helper to return elapsed time in fractions of a second
start = time.time()
def et(): 
    return round(time.time() - start, 1)

# Wait until all resources are available and acquire them
async def acquire(resources):
    # Check if one of each resource is available 
    while not all([len(available[res]) > 0 for res in resources]):
        # Release to allow other processing
        await asyncio.sleep(0.1)
    
    # Acquire the first of each available resource 
    # and return a dictionary of acquired resources
    return {res:available[res].pop(0) for res in resources}

# Release resources
def release(acquired):
    for res in acquired.keys():
        available[res].append(acquired[res])

# Move sample from store to instrument with robot
async def instrument_to_store(sample, robot, store, instr):
    print(f'({et()}): {robot} started moving {sample} from {instr} to {store}.')
    await asyncio.sleep(1)
    print(f'({et()}): {robot} finished moving {sample} from {instr} to {store}.')

# Move sample to instrument to store with robot
async def store_to_instrument(sample, robot, store, instr):
    print(f'({et()}): {robot} started moving {sample} from {store} to {instr}.')
    await asyncio.sleep(1)
    print(f'({et()}): {robot} finished moving {sample} from {store} to {instr}.')

# Analyze sample with instrument
async def analyze_sample(sample, instr):
    print(f'({et()}): {instr} started analyzing {sample}.')
    await asyncio.sleep(4)
    print(f'({et()}): {instr} finished analyzing {sample}.')

# Run test procedure on one sample
async def test_sample(sample):
    
    # Wait for resources
    res = await acquire(['robot', 'store', 'instrument'])
    robot, store, instr = res['robot'], res['store'], res['instrument']
    
    # Move from store to instrument with robot
    await store_to_instrument(sample, robot, store, instr)
    
    # Release resources
    release({'robot':robot, 'store':store})

    # Analyze sample with instrument
    await analyze_sample(sample, instr)

    # Wait for resources and unpack
    res = await acquire(['robot', 'store'])
    robot, store = res['robot'], res['store']
    
    # Move from instrument to store
    await instrument_to_store(sample, robot, store, instr)
    
    # Release resources
    release({'robot':robot, 'store':store, 'instrument': instr})

async def main():
    tasks = [test_sample(f's{i}') for i in range(96)]
    await asyncio.gather( *tasks )

    # t1 = test_sample('s1')
    # t2 = test_sample('s2')
    # t3 = test_sample('s3')
    # await asyncio.gather( t1, t2, t3 )

if __name__ == '__main__':
    asyncio.run( main() )
    
    # asyncio.run(run_all_async(['s1', 's2', 's3']))

# # Run all samples asynchronously
# async def run_all_async(samples):
#     async with asyncio.TaskGroup() as tg:
#         for samp in samples:
#             tg.create_task( test_sample(samp) )
            
