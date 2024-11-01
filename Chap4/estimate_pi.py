# estimate_pi.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import random, math                 # Import helpers

darts = 1000                        # Darts to throw
hits  = 0                           # Count of hits

i = 0                               # Loop counter
while i < darts:                    # Stop when all darts thrown
    x = random.random() - 0.5       # Simulate dart landing position
    y = random.random() - 0.5
    dist = math.sqrt(x*x + y*y)     # Compute distance to center
    if dist < 0.5:                  # Hits dartboard when distance < radius 
        hits += 1                   # Count hits
    i += 1                          # Increment counter

pi = 4*hits/darts                   # Compute estimate
print(f'Pi estimate is {pi}')       # Print result
