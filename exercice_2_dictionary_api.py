# heredar este diccionario y crear un Diccionario web con get async que le vamos a meter una lista de url i tiene que ir capturando
# esas url al lado de su resultado
# keys urls, values con data, status_code y headers
from exercice_1_dictionary_class import Diccionario
import aiohttp, asyncio

class DiccionarioWeb(Diccionario):
    
    def __init__(self, urls:str):
        super().__init__()
        self._urls = urls
        
        
    async def scrap_urls(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_url(session, url) for url in self._urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for n in results:
                print("---------", n)
        
    async def get_url(self, session: aiohttp.ClientSession ,url: str):
        print(url)
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
        try:
            async with session.get(url) as response:
                status_code = response.status_code
                headers = response.headers
                data = await response.text()
                return (url,status_code,headers,data)
                # self.__setitem__(url, (status_code,headers,data))
        except:
            Exception("Failed on getting response of url:",url)

        
if __name__ in "__main__":
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/post",
        "https://jsonplaceholder.typicode.com/posts",
        "https://api.github.com/users/github",
        "https://pokeapi.co/api/v2/pokemon/pikachu",
        "https://catfact.ninja/fact",
        "https://official-joke-api.appspot.com/random_joke",
        "https://api.coindesk.com/v1/bpi/currentprice.json",
        "https://restcountries.com/v3.1/name/spain",
        "https://dog.ceo/api/breeds/image/random"
    ]
    object = DiccionarioWeb(urls)
    asyncio.run(object.scrap_urls())
    print(object._data)