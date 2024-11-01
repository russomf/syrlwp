# check3.py
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
    
    # Validate and print useful error message
    if measurement < 1:
        print('Measurement values cannot be less than 1.')
    elif measurement > 10:
        print('Measurement values cannot be greater than 10.')
    else:
        print('Proceed with computation.')
