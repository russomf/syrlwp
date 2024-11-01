# file_notify_async.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import asyncio
from watchfiles import awatch

async def main():
    async for changes in awatch('data'):
        print(changes)

if __name__ == '__main__':
    asyncio.run(main())
