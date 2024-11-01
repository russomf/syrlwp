# convert.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Convert °F to °C
def F2C(F):
    C = (F - 32) / 1.8
    return C

# Convert °C to °F
def C2F(C):
    F = 1.8 * C + 32
    return F

# Invoke temperature conversion functions

# Prompt the user for Celsius
resp = input("Please enter a temperature in °C: ")

# Convert the response string to a float
C = float(resp)

# Convert the temperature and print the result
F = C2F(C)
print(f'{C}°C is {F}°F')

# Prompt the user for Fahrenheit
resp = input("Please enter a temperature in °F: ")

# Convert the response string to a float
F = float(resp)

# Convert the temperature and print the result
C = F2C(F)
print(f'{F}°F is {C}°C')
