# check1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

measurement = int( input("Enter measurement: ") )

if measurement < 1 or measurement > 10:
    print(f'{measurement} is out of range.')
