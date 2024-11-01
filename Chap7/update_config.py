# update_config.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import json
from pathlib import Path

# Read config file and return dictionary
def read_config(file='config.json'):
    path = Path(file)                   # Create Path object
    config = {}                         # Default to empty config
    with path.open('r') as f:           # Open config file to read
        txt = f.read()                  # Read contents
        config = json.loads(txt)        # Parse config
    return config                       # Return

# Write config file
def write_config(config, file='config.json'):
    path = Path(file)                   # Create Path object
    txt = json.dumps(config, indent=4)  # Serialize with indent
    with path.open('w') as f:           # Open config file to write
        f.write(txt)                    # Write serialized config

# Load config. Modify frequency. Save config.
def set_config_frequency(freq, file='config.json'):
    config = read_config(file)          # Read and parse config file
    config["frequency"] = freq          # Update dictionary
    write_config(config)                # Write config file

# Test
if __name__ == '__main__':
    set_config_frequency(7200)
