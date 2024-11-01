# shipping2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Query user when needed (days in future)
resp = input('How soon do you need the shipment? (days): ')

# Validate response
if not resp.isnumeric():
    print( "Error. Please enter a whole number of days.")
else:
    # Convert response to integers
    ndays = int(resp)
    
    # Carefully ordering permits the use of simpler expressions
    if ndays <= 0:
        print('Fastest delivery is 1 day (overnight).')
    elif ndays == 1:
        print("Use Overnight shipping.")
    elif ndays <= 3:
        print("Use First-Class shipping.")
    elif ndays <= 5:
        print("Use Ground shipping.")
    else:
        print("Use cheapest shipping method available.")