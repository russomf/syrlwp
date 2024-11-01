# log.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from datetime import datetime

def log(msg, name='log.txt'):
    with open(name, 'a') as file:
        file.write(f'{datetime.now():%Y-%m-%d %I:%M:%S %p}, {msg}\n')
