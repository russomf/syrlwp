# duration.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import time, random

# Wraps fn with new timing functionality
def duration(fn):
    def wrapper(*args, **kwargs):
        start = time.time()             # Record start time
        resp = fn(*args, **kwargs)      # Invoke decorated function
        elapsed = time.time() - start   # Compute elapsed time and print
        print(f'{fn.__name__} took {elapsed} seconds')
        return resp                     # Return original result
    return wrapper                      # Return decorated function

# Test decorated function
if __name__ == '__main__':
    # Decorate the original function
    @duration
    def dowork(x):
        time.sleep( 1 + random.random() )
        return 2*x

    # Invoke it
    print( dowork(1) )
    
# if __name__ == '__main__':
#     # @duration
#     # Original function
#     def dowork(x):
#         time.sleep( 1 + random.random() )
#         return 2*x

#     # Wrap dowork with timing
#     dowork_timed = duration(dowork)

#     # Invoke it
#     print( dowork_timed(1) )
