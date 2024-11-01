# async_demo.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio, time

# Helper to return elapsed time in fractions of a second
start = time.time()
def et():
    return round(time.time() - start, 1)

# One asynchronous task execution
async def do_task(n):
    print(f'{et()} Begin task {n}')
    await asyncio.sleep(3)
    print(f'{et()} End task {n}')

# Failed asynchronous execution. Still executes sequentially.
# async def task_sequence():
#     await do_task(1)
#     await do_task(2)
#     await do_task(3)

# All asynchronous tasks gathered into an executing task group
async def task_sequence():
    await asyncio.gather( 
        do_task(1), 
        do_task(2), 
        do_task(3)
    )

# Another way
# async def task_sequence():
#     # Not reliable. TaskGroups hold weak references only.
#     # Tasks may be garbage collected at any time.
#     # Otherwise, must keep references to Task objects.
#     # For reliable "fire-and-forget" background tasks, gather them in a collection.
#     tasks = set()
#     async with asyncio.TaskGroup() as tg:
#         tasks.add( tg.create_task( do_task(1) ) )
#         tasks.add( tg.create_task( do_task(2) ) )
#         tasks.add( tg.create_task( do_task(3) ) )
    
if __name__ == '__main__':
    asyncio.run( task_sequence() )
