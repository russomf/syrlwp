# read1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Read lines from a file
def read_lines(name):
    data = []                        # List to collect numbers
    with open(name, 'r') as file:    # Open file so it closes automatically
        for line in file:            # Read all lines from filer 
            item = float(line)       # Convert each line to a float
            data.append(item)        # Append floats to a list
    return data                      # Return list

if __name__ == '__main__':
    print( read_lines('data.txt') )
