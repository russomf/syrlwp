# notify.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from watchfiles import watch, Change
from pathlib import Path

# Store program root path
rootpath = Path(".").absolute()

def display_changes(changes):
    for change in changes:                      # For all changes
        tchange, tpath = change                 # Unpack change parts
        path = Path(tpath)                      # Create a Path object
        relpath = path.relative_to(rootpath)    # Path relative to root
        
        if tchange == Change.added:             # On an addition
            print(f'Added {relpath}')
        elif tchange == Change.modified:        # On a modification
            print(f'Modified {relpath}')
        elif tchange == Change.deleted:         # On a deletion
            print(f'Deleted {relpath}')
    if not changes:
        print('No changes in this batch')

# Monitor a directory_path for changes and notify when detected
def notify(directory_path):
    for changes in watch(directory_path):          # A change was detected
        display_changes(changes)

# Monitor a directory_path for changes and notify when detected
# Monitor folder only, ignore subfolders
def notify_not_recursive(directory_path):
    for changes in watch(directory_path, recursive=False): # A change was detected
        display_changes(changes)

# Monitor multiple directory_paths for changes and notify when detected
def notify_multiple(*directory_paths):
    for changes in watch(*directory_paths):        # A change was detected
        display_changes(changes)

# Batch all changes over delay milliseconds.
# Always return changes after the same time period.
def notify_batch(directory_path, delay):
    for changes in watch(directory_path, step=delay, yield_on_timeout=True):
        display_changes(changes)

# Return True when path ends with ".txt"
def txt_only(change, spath):
    return spath.endswith(".txt")

# Report all changes on .txt files only.
# Report changes in current folders only. Do not monitor changes in subfolders.
def notify_txt(directory_path):
    for changes in watch(directory_path, watch_filter=txt_only, recursive=False):
        display_changes(changes)

if __name__ == '__main__':
    # notify('data')
    # notify_not_recursive('data')
    # notify_multiple('data', 'data2')
    # notify_batch('data', 10000)
    notify_txt('data')
