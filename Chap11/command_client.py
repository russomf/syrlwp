# command_client.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Stubs for remote command execution
import requests

# Global URL for the command server
command_server = 'http://192.168.1.155:8080'

# Count files on remote computer
def count_files():
    url = f'{command_server}/count_files'   # Form URL
    resp = requests.get(url)                # Invoke command
    if resp.status_code == 200:             # Check response
        return int(resp.text)               # Return response
    else:
        return -resp.status_code            # Negative error status

# Check if a data file exists on remote computer
def file_exists(fname):
    url = f'{command_server}/exists/{fname}'
    resp = requests.get(url)                # Invoke command
    if resp.status_code == 200:             # Check response
        return bool(resp.text)              # Return response
    else:
        return False                        # Error status
    
if __name__ == '__main__':
    print( count_files())
    print( file_exists("plate1.txt") )
    print( file_exists("plate0.txt") )
