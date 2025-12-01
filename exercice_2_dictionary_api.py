# heredar este diccionario y crear un Diccionario web con get async que le vamos a meter una lista de url i tiene que ir capturando
# esas url al lado de su resultado
# keys urls, values con data, status_code y headers
from teoria_apis import Diccionario
import aiohttp, asyncio

class DiccionarioWeb(Diccionario):
    
    def __init__(self, urls:str):
        super().__init__()
        self._urls = urls
        
    
    def add_response_obj(self, key:str, values: aiohttp.ClientResponse):
        if not key or not values:
            return
        status_code = values.status
        headers = values.headers
        content = values.content
        self.__setitem__(key, {
            'status_code': status_code,
            'headers': dict(headers),
            'content': content
        })
    
    def save_results(self, data: list[tuple[str,aiohttp.ClientResponse]]):
        for response in data:
            if response:
                self.add_response_obj(response[0],response[1])
        
    async def scrap_urls(self):
        session_timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=session_timeout) as session:
            tasks = [self.get_url_response(session, url) for url in self._urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            self.save_results(results)
        
    async def get_url_response(self, session: aiohttp.ClientSession ,url: str):
        try:
            print(f"Getting response from: {url} ...")
            async with session.get(url) as response:
                print(f"Response from {url} ")
                return (url, response)
        except asyncio.TimeoutError:
            print("Long operation timed out on ",url)
            return None
        except Exception as e:
            print(f"Failed on getting response of url {url}, errors: {e}")
            return None

        
if __name__ in "__main__":
    urls = [
        'https://httpbin.org/json',                    
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://api.github.com/users/github',          
        'https://catfact.ninja/fact',                   
        'https://api.coindesk.com/v1/bpi/currentprice.json', 
        'https://dog.ceo/api/breeds/image/random',      
        'https://api.publicapis.org/entries',
        'https://official-joke-api.appspot.com/random_joke', 
        'https://api.spacexdata.com/v4/launches/latest', 
        'https://httpbin.org/user-agent'  
    ]
    object = DiccionarioWeb(urls)
    asyncio.run(object.scrap_urls())
    print("Print Diccionario responses object: ",object)
    