# duplicate_files.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import hashlib
from pathlib import Path

# Hash a file and return unique digest
def hash_file(path):
    sha256 = hashlib.sha256()               # Create a SHA256 hash object
    with path.open('rb') as file:
        while block := file.read(65536):    # Read 64KB byte blocks      
            sha256.update(block)            # Update the hash with bytes.
    return sha256.hexdigest()               # Compute and return unique digest

# Walk the current directory, list files, and recurse into subdirectories
# Return a list of lists containing file duplicates
def find_duplicates(top='.'):
    top     = Path(top)                     # Create Path object
    abspath = top.absolute()                # Get absolute path
    digest_dict = {}                        # Initial digest dictionary

    # Walk all files and directories
    for path, dirs, files in abspath.walk():
        for file in files:                  # Iterate over all files
            file_path = path / file         # Join path and file
            
            digest = hash_file(file_path)   # Get full path and digest
            if digest in digest_dict:       # Add to dictionary of lists
                digest_dict[digest].append(file_path)
            else:
                digest_dict[digest] = [file_path]

    # Filter to lists with length > 1 and return
    dups = [digest_dict[k] for k in digest_dict if len(digest_dict[k]) > 1]
    return dups

if __name__ == '__main__':
    dups = find_duplicates('.')
    
    # Print identified duplicates
    for dup in dups:
        print('---')
        for file in dup:
            print(file)
