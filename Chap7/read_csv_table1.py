# read_csv_table1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys

# Read a table of comma-delimited data and assemble as a list of lists
def read_csv_table1(name, sep=','):
    table = []                              # To hold data as rows
    with open(name, 'r', encoding='utf-8') as file:    # Split and strip titles
        titles = [title.strip() for title in file.readline().split(',')]
        table.append( titles )              # Add column titles to table
        while (line := file.readline()):    # Walrus operator to detect EOF
            row = [float(item) for item in line.split(sep)] # Split and convert
            table.append( row )             # Add row data to table
    return table                            # Return table as list of lists

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide CSV file name')
        sys.exit()
    tbl = read_csv_table1(sys.argv[1])
    for row in tbl:
        print(row)
