# schedule1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio, time

# Helper to return elapsed time in fractions of a second
start = time.time()
def et():
    return round(time.time() - start, 1)

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
    # Resource names
    robot, store, instr = 'robot', 'store', 'instrument'
    
    # Move from store to instrument
    await store_to_instrument(sample, robot, store, instr)
    
    # Analyze sample
    await analyze_sample(sample, instr)
    
    # Move from instrument to store
    await instrument_to_store(sample, robot, store, instr)

async def main():
    t1 = test_sample('s1')
    t2 = test_sample('s2')
    t3 = test_sample('s3')
    await asyncio.gather( t1, t2, t3 )

if __name__ == '__main__':
    asyncio.run( main() )
    
    # Other options
    # run_all(['s1', 's2', 's3'])
    # asyncio.run(run_all_async(['s1', 's2', 's3']))
