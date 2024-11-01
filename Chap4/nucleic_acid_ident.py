# nucleic_acid_ident.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Query user
N = input('Enter a nucleic acid symbol: ')

# Condition and validate
N = N.upper().strip()

if len(N) != 1:
    print('Please enter one character only.')
else:
    # Use a nested conditional expression to identify the symbol
    result = 'a Pyrimidine' if N in ['T','C','U'] else 'a Purine' if N in ['G','A'] else 'not a nucleic acid symbol'
    print(f'{N} is {result}')
