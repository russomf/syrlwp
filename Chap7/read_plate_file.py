# read_plate_file.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Read an instrument data file that has a header of name-value pairs
# followed by a two-column table of data.
# The header area and the data area are separated by a blank line.
# Return a dictionary with all data, of the form
# {'User':..., 'Bar Code':..., 'Date':..., 'Readings': {'A01':..., 'A02':, ...}}

def read_plate_file(name):
    data = {'Readings': {}} # Collect file data
    section = 1             # Start with section 1
    
    with open(name, 'r') as file:
        for line in file:
            line = line.strip()
            
            # If reading header and find a black line, change section to 2
            if section == 1 and len(line) == 0:
                section = 2
                continue            # Move to next line
            
            # Perform parsing steps based on current section.
            # Extract name-value pair from header and add to dictionary.
            if section == 1:
                parts = line.split(':')
                data[parts[0].strip()] = parts[1].strip()
            
            # Convert data and add to Readings dictionary.
            elif section == 2:
                parts = line.split(',')
                data['Readings'][parts[0].strip()] = float(parts[1])
    
    return data

if __name__ == '__main__':
    file_data = read_plate_file('plate1.txt')
    print( file_data )
