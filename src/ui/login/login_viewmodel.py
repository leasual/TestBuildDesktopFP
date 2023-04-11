
import aiohttp
import asyncio
import flet as ft

# documents https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
# content = """[{"id": "E0:69:78:58:22:A4:32:CE","internalipaddress": "192.168.192.34","internalport": "8080",
# "macaddress": "E0:69:78:58:22:A4:32:CE","name": "RaspBee GW"}]"""


class LoginViewModel:

    async def searchGateway(self, ):
        try:
            async with aiohttp.ClientSession() as session:
                while not self.cancelSearch:
                    # API.searchGateway(session, "https://phoscon.de/discover")
                    async with session.get("https://phoscon.de/discover") as resp:
                        gateways = await resp.json()
                        print("gateways= {}".format(gateways))
                        if len(gateways) == 0:
                            print("gateway size= {}", len(gateways))
                            self.serverIP = "192.168.31.130"
                            self.page.pubsub.send_all(f"{self.serverIP}")
                        else:
                            self.cancelSearch = True
                            for gateway in gateways:
                                print("gateway= {}".format(gateway))
                    await asyncio.sleep(1)
        except:
            print("search gateway error")

    def __init__(self, page: ft.Page):
        self.cancelSearch = False
        self.serverIP = ''
        self.page = page
