# labels.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

resp = input('Enter a comma-separated list of well labels: ')
items = resp.split(' ')

labels = []                 # List to accumulate formatted labels
i = 0                       # Init index counter
while i<len(items):         # Continue for each list element
    lbl = items[i].upper()  # Format each item
    if len(lbl) >= 2:       # Valid if at least two characters
        labels.append(lbl)  # Accumulate valid formatted labels
    i += 1                  # Increment counter

print(labels)
