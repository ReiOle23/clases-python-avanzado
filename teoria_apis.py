# APi REST
# es un tipo de interfaz
# http methods (get, post, patch, delete)
# REST significa representación de objectos
# la api no tiene estado


# Threads de forma eficiente en las 20 primeras urls
import requests
from threading import Thread, Semaphore

def request_url(url:str):
    with Semaphore(10):
        try:
            response = requests.get(url)
            print(f"Request on {url} -> status {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"Timout on {url}")
        except Exception as e:
            print(f"Could not get {url} Error ---> {e}")
            
if __name__ in "__main__":
    centenar_urls = [f"https://httpbin.org/get?p={i}" for i in range(100)]
    threads = [Thread(target=request_url, args=(url,)) for url in centenar_urls]
    threads_started = []
    for t in threads:
        threads_started.append(t)
        t.start()
        
    for th in threads_started:
        t.join()
        