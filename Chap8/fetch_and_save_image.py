# fetch_and_save_image.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Requesting and saving binary data
import requests, sys

def fetch_and_save_image(mname, fname):
    # Substitute name into URL
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{mname}/record/PNG?record_type=3d'

    # Perform the HTTP request and check status
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Unexpected response: {resp.reason}')
        sys.exit()
        
    # Save returned binary data to a file
    with open(fname, 'wb') as file:
        for chunk in resp.iter_content(chunk_size=128):
            file.write(chunk)
            
    print(f'Image saved to {fname}')

if __name__ == '__main__':
    # Validate parameter
    if len(sys.argv) < 2:
        print("Please pass a PubChem molecule name and an optional image file name")
        sys.exit()
        
    # Get molecule name parameter
    mname = sys.argv[1].strip()
    
    # Get file name parameter or create a default name based on molecule name
    if len(sys.argv) >= 3:
        fname = sys.argv[2].strip()
    else:
        fname = f'{mname}.png'
    
    # Invoke function
    fetch_and_save_image(mname, fname)
