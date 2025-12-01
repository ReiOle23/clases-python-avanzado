import requests
from concurrent.futures import ThreadPoolExecutor

def request_url(url:str):
    try:
        response = requests.get(url)
        print(f"Request on {url} -> status {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Timout on {url}")
    except Exception as e:
        print(f"Could not get {url} Error ---> {e}")
            
if __name__ in "__main__":
    centenar_urls = [f"https://httpbin.org/get?p={i}" for i in range(100)]
    with ThreadPoolExecutor(max_workers=10) as pool:
        futuros = [pool.submit(request_url, url) for url in centenar_urls]
    for f in futuros:
        print(f.result())
        