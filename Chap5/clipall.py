# clipall.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Clip all components to [0, 255]
def clipall( *components ):
    clipbelow = 0                       # Count clips
    clipabove = 0
    
    # Helper function to clip one val to [0, 255]
    def clip(val):
        nonlocal clipbelow, clipabove   # Names in outer local scope
        
        val = round(val)                # Round to int
        if val < 0:
            val = 0                     # Clip from below
            clipbelow += 1              # Keep count
        elif val > 255:
            val = 255                   # Clip from above
            clipabove += 1              # Keep count
        return val
    
    # Clip all positional arguments and collect
    clipped = [clip(comp) for comp in components]
    
    # Print counts
    print(f'{clipbelow} clipped from below and {clipabove} clipped from above.')

    # Returned all clipped values
    return clipped

# Test
if __name__ == '__main__':
    print( clipall(259.2, 45.3, 129, 300, -1) )

    