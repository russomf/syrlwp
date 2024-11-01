# check2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

resp = input("Enter measurement: ")

# Proceed only if entry is numeric
if not resp.isnumeric():
    print('Error. Please enter numeric digits only.')
else:
    # Convert string to float
    measurement = int(resp)
    if measurement < 1 or measurement > 10:
        print(f'{measurement} is out of range')
    else:
        print('Proceed with computation')
