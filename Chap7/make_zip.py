# make_zip.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from pathlib import Path
from zipfile import ZipFile

def zip_directory(archive, ext, top='.'):
    # Get all matching file path strings
    top = Path(top)
    file_paths = [str(f) for f in top.glob(f'*.{ext}')]

    # Create new zip archive
    with ZipFile(archive, 'w') as zip:
        # Add all files to zip archive
        for name in file_paths:
            zip.write(name)

if __name__ == '__main__':
    zip_directory('archive.zip', 'csv')
