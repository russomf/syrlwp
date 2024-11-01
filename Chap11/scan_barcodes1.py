# scan_barcodes1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import serial

if __name__ == '__main__':
    # Create a Serial object with configuration parameter values.
    # Return after 10 seconds if no data is received.
    port = serial.Serial('COM4', 115200, timeout=10)

    while True:                                 # Infinite loop
        data = port.read(10)                    # Read max of 10 bytes
        print(data)                             # Print data

    port.close()                                # Clean up

    # while True:                                 # Infinite loop
    #     data = port.read(10)                    # Read max of 10 bytes
    #     # data = port.read_until(expected=b'\r')  # Wait until \r byte is found
    #     barcode = data.decode('utf8')           # Decode bytes to string
    #     if len(barcode) == 0: break             # Break out of loop if empty
    #     print(barcode)                          # Print barcode
