# data_download.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from aiohttp import web

# Create and initialize routes table
# Add static default route to data directory with file index.
routes = web.RouteTableDef()
routes.static('/', 'data', show_index=True)

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
