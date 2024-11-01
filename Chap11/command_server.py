# command_server.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from aiohttp import web
from pathlib import Path

# Create routes table
routes = web.RouteTableDef()

# Create and initialize routes table
# Add static default route to data directory with file index.
routes = web.RouteTableDef()
routes.static('/', 'data', show_index=True)

# Count the number of files in the data directory
@routes.get('/count_files')                 # Associate URL with function
def count_files(req):
    fldr = Path('data')                     # Create a Path object
    num_files = len(list(fldr.iterdir()))   # Count files
    resp = web.Response()                   # Create a Response object 
    resp.text = str(num_files)              # Set its text content
    return resp                             # Return Response

# Check if a file exists given name
@routes.get('/exists/{name}')
def file_exists(req):
    data_fold = Path('data')                # Create a Path object
                                            # Find all file name matches
    matches = [f.name for f in data_fold.iterdir() 
               if f.name == req.match_info['name']]
    resp = web.Response()                   # If found one, 
    if len(matches) > 0:
        resp.text = "True"                  # return true.
    else:
        resp.text = ""                      # Otherwise, fail.
    return resp

# Launch server
if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
