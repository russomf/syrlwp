# scrape_shear_moduli.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import re, json, requests
from bs4 import BeautifulSoup

# Get the shear modulus data from the Wikipedia table and save to file
def update_shear_moduli(fname):
    # Fetch HTML from Wikipedia page with a table of material elastic properties
    url = 'https://en.wikipedia.org/wiki/Elastic_properties_of_the_elements_(data_page)'
    resp = requests.get(url)

    # Process HTML into a BeautifulSoup document
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Find all wikitables on the page. There are four.
    wikitables = soup.find_all('table', class_='wikitable')

    # Extract the fourth wikitable with shear modulus data
    tbl = wikitables[3]

    # Regular expression to match on a number with an optional decimal
    re_num = re.compile(r'\d+.{0,1}\d*')

    # Get all rows from the table
    trs = tbl.find_all('tr')

    # Process all rows of data.
    # Skip first row which holds column headers.
    data = {}
    for tr in trs[1:]:
        tds = tr.find_all('td')             # Get all columns and text
        txt = [td.get_text().strip() for td in tds]
        key = txt[2]                        # Get material name
        mat = re.search(re_num, txt[3])     # Try to extract number
        if mat:                             # If number found...
            data[key] = float(mat.group())  # ...add to dictionary
        
    # Serialize and save to file
    with open(fname, 'w') as file:
        file.write( json.dumps(data) )
        
    # Also return data
    return data

# Reload shear moduli data from file and return
def load_shear_moduli(fname):
    with open(fname, 'r') as file:
        sdata = file.read()
    return json.loads(sdata)

# Test the function by loading and printing the data
if __name__ == '__main__':
    update_shear_moduli('shear_moduli.json')
    moduli = load_shear_moduli('shear_moduli.json')
    print(moduli)
