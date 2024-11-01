# for1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

data = [2.34, 2.01, 1.99, 2.26, 2.13, 1.95, 2.05, 1.98]
squares = []                # Used to collect squares
for x in data:              # Access each element
    squares.append( x*x )   # Square each element and collect
ssq = sum(squares)          # Sum 
print(ssq)                  # Print
