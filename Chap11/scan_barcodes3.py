# scan_barcodes3.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio, serial

# Wait for a barcode asynchronously
async def read_barcode():
    buff = b''                                      # Init byte buffer
    while True:                                     # Poll serial port
        buff += port.read(100)                      # Append to buffer
        if len(buff) > 0: print(f'Buffer: {buff}')  # Show buffer if non-zero
        idx = buff.find(b'\r')                      # Look for complete barcode
        if idx >= 0:                                # If found...
            barcode = buff[:idx].decode('utf-8')    # Decode barcode
            buff = buff[idx+1:]                     # Strip bytes from buffer
            print(f'Read {barcode}')
        await asyncio.sleep(1)                      # Asynchronous sleep

if __name__ == '__main__':
    # Create a Serial object with configuration parameter values.
    # Return immediately if no data is received.
    port = serial.Serial('COM4', 115200, timeout=0)
    asyncio.run( read_barcode() )               # Get started
    port.close()                                # Clean up
