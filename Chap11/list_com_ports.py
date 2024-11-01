# list_com_ports.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import serial.tools.list_ports

if __name__ == '__main__':
    # List all com ports
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port)
