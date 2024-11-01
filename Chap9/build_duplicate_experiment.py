# build_duplicate_experiment.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import random
import pandas as pd

# Build initial experiment DataFrame with duplicate tests and save
def build_duplicate_experiment(sfile='source_map.csv'):
    # Read Source Map into DataFrame
    sdf = pd.read_csv(sfile)

    # Generate DataFrame with randomized plate layout for testing
    # Duplicate source map using concat() method
    df = pd.concat( [sdf, sdf], ignore_index=True)
    
    # Add transfer volumes to 'vol' column. 100 mL each.
    df['vol'] = [100]*96
    
    # Generate well labels, shuffle randomly. Add to 'dest' column.
    dests = [f'{chr(i//12+65)}{i%12+1:02d}' for i in range(96)]
    random.shuffle(dests)
    df['dest'] = dests
    
    # Return generated DataFrame
    return df

if __name__ == '__main__':
    # To start analysis build the experiment DataFrame
    df = build_duplicate_experiment(sfile='source_map.csv')

    # Save entire experiment DataFrame to file for use in future
    df.to_csv('experiment.csv', index=False)

    # Write worklist for liquid handler
    wl = df[['src','dest','vol']]
    wl.to_csv('worklist.csv', index=False)

