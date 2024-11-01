# C2F.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)
 
# Convert a temperature in Celsius to Fahrenheit.

# Prompt the user for Celsius
resp = input("Please enter a temperature in degrees C: ")

# Convert the response string to a float
C = float(resp)

# Convert to Fahrenheit
F = 1.8 * C + 32

# Output
print( f'{C} degrees C is {F} degrees F' )
