# scope2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import time

# Print seconds elapsed since start
def print_elapsed():
    print( time.time() - start)

# Attempt to reset start
def reset_start():  # The start variable is global
    global start
    start = time.time()

start = time.time() # Record the current time
time.sleep(1)       # Sleep for one second
print_elapsed()     # Print the seconds elapsed
reset_start()       # Reset start time
time.sleep(1)       # Sleep for one second
print_elapsed()     # Print the seconds elapsed
