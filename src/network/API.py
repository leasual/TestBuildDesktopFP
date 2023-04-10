import requests


class API(object):
    api_prefix = "http://"
    api_host = "localhost"
    api_token = ""
    api_password = ""

    # singleton implement
    # def __init__(self):
    #     if not hasattr(API, "_first_init"):
    #         print("__init__")
    #         API._first_init = True
    #
    # def __new__(cls, *args, **kwargs):
    #     print("__new__")
    #     if not hasattr(API, "_instance"):
    #         print("create new instance")
    #         API._instance = object.__new__(cls)
    #     return API._instance

    @staticmethod
    async def searchGateway(session, url):
        async with session.get(url) as resp:
            gateways = await resp.json()
            print("gateways= {}".format(gateways))
            return gateways
