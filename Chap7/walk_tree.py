# walk_tree.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from pathlib import Path
import sys

# Walk the current directory, list files, and recurse into subdirectories
def walk_tree(top='.'):
    # Expand top directory and get some formatting parameters
    top     = Path(top)                             # Create Path object
    abspath = top.absolute()                        # Get absolute path
    offset  = len(abspath.parts)                    # Save initial depth
    
    # Visit all files and directories from top down to all tree leaves
    for path, dirs, files in top.walk():
        abspath = path.absolute()                   # Expand to absolute path
        base    = abspath.parts[-1]                 # Base path name
        depth   = len(abspath.parts)                # Depth in file system
        print(f'{"   "*(depth-offset)}┖─ {base}/')
        
        # Get file name and metadata
        # Print files using extended characters: ┃ ┖ ┠ ─ with depth indent
        for file in files:
            file_path = path / file                 # Join root path and file
            metadata = file_path.stat()             # Get metadata
            fsize    = metadata.st_size             # Size in bytes
            print(f'{"   "*(depth+1-offset)}┠─ {file} ({fsize} bytes)')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter a path")
        sys.exit()
    walk_tree(sys.argv[1])
