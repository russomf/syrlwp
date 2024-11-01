# future.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sched, time

# Print elapsed time in seconds
start = time.time()                 # Save start time
def elapsed(tname):
    tstamp = time.time()
    print( f'Task {tname}. Elapsed time: {tstamp - start} seconds')

if __name__ == '__main__':
    
    # Start scheduler with timestamp as time function
    queue = sched.scheduler(time.time, time.sleep)
    
    # Schedule relative and absolute timed future events
    ev1   = queue.enter(5, 1, elapsed, argument=('First',))     
    ev2   = queue.enterabs(start+10, 1, elapsed, argument=('Second',))
    
    # Run until no more events scheduled
    queue.run()
