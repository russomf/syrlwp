# while2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

data = [2.34, 2.01, 1.99, 2.26, 2.13, 1.95, 2.05, 1.98]

# Assume overall min and max to be the first list item
min, max = data[0], data[0]
i = 0                       # Initialize counter
while i < len(data):        # Test for repetition of code block
    if data[i] < min:       # Test for better minimum
        min = data[i]       # Improve overall minimum
    if data[i] > max:       # Test for better maximum
        max = data[i]       # Improve overall maximum
    i += 1                  # Increment counter

print([min, max])
