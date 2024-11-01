# while1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

data = [2.34, 2.01, 1.99, 2.26, 2.13, 1.95, 2.05, 1.98]

sum = 0.0
i = 0                       # Initialize counter
while i < len(data):        # Test for execution of the while block
    sum += data[i]*data[i]  # Compute square and add to sum
    i += 1                  # Increment counter
print(sum)
