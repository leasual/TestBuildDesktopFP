import asyncio
import aiohttp

from src.network.API import API
from src.network.model import Gateway


# documents https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
# content = """[{"id": "E0:69:78:58:22:A4:32:CE","internalipaddress": "192.168.192.34","internalport": "8080",
# "macaddress": "E0:69:78:58:22:A4:32:CE","name": "RaspBee GW"}]"""


class LoginViewModel:

    async def searchGateway(self, function):
        async with aiohttp.ClientSession() as session:
            while not self.cancelSearch:
                future = asyncio.ensure_future(API.searchGateway(session, "https://phoscon.de/discover"))
                result = await future
                future.add_done_callback(function)
                await asyncio.sleep(1)

    def taskCallback(self, gateways):
        print("task callback")
        # print("gateway size= {} cancel= {}".format(len(gateways), self.cancelSearch))
        # if len(gateways) != 0:
        #     self.cancelSearch = True
        # else:
        #     for model in gateways:
        #         print("model json= {}".format(model))
        #         gateway = Gateway(**model)
        #         print("gateway {}".format(gateway))

    def __init__(self, cancelSearch: bool = False):
        self.cancelSearch = cancelSearch
        print("init login viewmodel")
        asyncio.run(self.searchGateway(self.taskCallback))
        print("execute request by asyncio")
