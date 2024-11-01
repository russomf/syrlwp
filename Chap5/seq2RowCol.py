# seq2RowCol.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Compute the row, col for a well in a rack 
# given a row-major sequence number starting with 1.
# Assume 12 columns in the rack as the default. 
def seq2RowCol(n, ncols=12):
    row = (n - 1) // ncols + 1
    col = (n - 1) % ncols + 1
    return row, col

# Test seq2RowCol()
seq = 13
row, col = seq2RowCol(seq)
print( f'Seq {seq} is at {row,col}')

row, col = seq2RowCol(seq, ncols=5)
print( f'Seq {seq} in rack with 5 cols is at {row,col}')

seq = 25
row, col = seq2RowCol(seq)
print( f'Seq {seq} is at {row,col}')

row, col = seq2RowCol(seq, ncols=10)
print( f'Seq {seq} in rack with 10 cols is at {row,col}')
