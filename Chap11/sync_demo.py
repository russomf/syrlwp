# sync_demo.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import time

# Helper to return elapsed time in fractions of a second
start = time.time()
def et():
    return round(time.time() - start, 1)

# One synchronous task
def do_task(n):
    print(f'{et()} Begin task {n}')
    time.sleep(3)
    print(f'{et()} End task {n}')

# All synchronous tasks
def task_sequence():
    do_task(1)
    do_task(2)
    do_task(3)

if __name__ == '__main__':
    task_sequence()
