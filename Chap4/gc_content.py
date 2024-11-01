# gc_content.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Data from https://bioinformatics.ccr.cancer.gov/docs/b4b/
seq = 'GGGTGATGGCCGCTGCCGATGGCGTCAAATCCCACCAAGTTACCCTTAACAACTTAAGGGTTTTCAAATAGA'

count = 0
for n in seq:
    if n in ('G','C'):
        count += 1
print(f'The sequence has a GC content of {count/len(seq)*100:.1f}%')
