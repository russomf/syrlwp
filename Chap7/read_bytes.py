# read_bytes.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys

# Read a file and print bytes
def read_bytes(name):
    with open(name, 'rb') as file:          # Open as read binary
        bytes = file.read()                 # Read entire contents
        print( f'{name} contains {len(bytes)} bytes')
        for b in bytes:                     # Print each as decimal and bits
            print(f'{b} ({b:08b})', end=' ')
        print()

# Read a file and print UTF-8 encoded characters
def read_utf8(name):                        # Open file with UTF-8 encoding
    with open(name, 'r', encoding='utf-8') as file:
        cpoints = file.read()               # Read entire contents
        print( f'{name} contains {len(cpoints)} code points')
        for c in cpoints:                   # Print each code point
            print(c, end=' ')
        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter a file name")
        sys.exit()
    read_bytes(sys.argv[1])
    read_utf8(sys.argv[1])
