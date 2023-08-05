'''
from enkanetworkcard import aioencbanner
import time

client = encbanner.EnkaGenshinGeneration(dowload = True) 
client.FIX_ASYNCIO_WIN = True

b = client.start(uids = "811455610",  template  = 2)

b = client.profile(uid = 724281429, image = True)
'''

from enkanetworkcard import aioencbanner
import asyncio

async def card():
    ENC = aioencbanner.EnkaGenshinGeneration(namecard = True)
    return await ENC.start(uids = 829702635, template = 2)

result = asyncio.run(card()) 

print(result)
