# read_csv_table2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys, csv

def read_csv_table2(name):
    with open(name, 'r', encoding='utf-8') as file:
        rdr = csv.reader(file) #, delimiter=',', quotechar='"') # Create a reader that wraps the file
        table = []                  # To hold data as rows
        for row in rdr:             # CVS reader is an iterator
            table.append( row )     # Add row data to table
    return table

# Does not parse data correctly
# def read_csv_table2(name):
#     with open(name, 'r') as file:
#         for line in file:
#             items = line.split(',')
#             print( items )

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide CSV file name')
        sys.exit()
    tbl = read_csv_table2(sys.argv[1])
    for row in tbl:
        print(row)
