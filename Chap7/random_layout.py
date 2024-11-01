# random_layout.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import random, openpyxl

# Generate 24 sample names in quadruplicate
samples = [f'S{i:02d}' for i in range(1, 25)] * 4
random.shuffle( samples )

# Generate all well locations as (row, column) pairs and randomize
coords = [(r,c) for r in range(2, 10) for c in range(2,14)]

# Create, fill, and save a Workbook with sample names
wb = openpyxl.Workbook()
ws = wb.active

# Write row and column titles
for i in range(8): ws.cell(i+2, 1).value = chr(i+65)
for i in range(12): ws.cell(1, i+2).value = i+1

# Write sample ids to Cells
for i in range(len(coords)):
    ws.cell(*coords[i]).value = samples[i]

# Save file and close Workbook
wb.save('plate_map.xlsx')
wb.close()
