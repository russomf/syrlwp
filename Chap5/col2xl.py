# col2xl.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Convert a 1-based column number to an Excel column letter designation
def col2xl(col):
    lets = []                           # Collect letters
    while col > 0:                      # Continue while more to convert
        let = chr((col - 1) % 26 + 65)  # Next letter
        lets.insert(0, let)             # Prepend to list
        col = (col - 1) // 26           # Drop 1's position
    return ''.join(lets)                # Join and return

# Test col2xl()
print(col2xl(1), col2xl(26), col2xl(52), col2xl(1000))
