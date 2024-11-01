# process_data.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import time

# Process and return a list of data values
def process_data(data):
    print(f'---\ndata: {data}')     # Print data argument
    
    try:                            # Try to process data
        start = time.time()         # Record the start time
        range = data[-1] - data[0]  # Process data list
        resp  = [el/range for el in data]
    except IndexError:
        print("Found an empty data list.")
        resp = []
    except ZeroDivisionError:
        print("Data has a zero-length range. No processing.")
        resp = data
    except:
        print("Something went wrong. Please check your data.")
        resp = None                 # Respond with None on another error
    else:
        print("No exceptions. Processing completed.")
    finally:
        # Always sleep and compute and print the elapsed time.
        time.sleep(0.1)
        elapsed = time.time() - start
        print(f'Elapsed time {elapsed}')
    
    return resp                     # Returned processed data

# Tests
if __name__ == '__main__':
    print(process_data([]))        # Test 1 - Empty list
    print(process_data([1]))       # Test 2 - Range error
    print(process_data({}))        # Test 3 - Wrong parameter type
    print(process_data([1,2,3]))   # Test 4 - No problems
