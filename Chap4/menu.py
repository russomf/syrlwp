# menu.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Print menu options
print('''
Choose an option:
1. Do thing 1
2. Do thing 2
3. Exit
''')

# Get response from user
while True:
    # Query for response
    resp = input('Enter an option: ')
    
    # Validate
    if not resp.isnumeric():
        print('Please enter 1, 2 or 3')
        continue        # Try again
    option = int(resp)    
    if option < 1 or option > 3:
        print('Please enter 1, 2, or 3')
        continue        # Try again
    
    # Break out of loop on valid option
    break

print(f'Option {option} chosen')
