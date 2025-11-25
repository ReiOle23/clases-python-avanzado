import asyncio

async def worker(n: int):
    print(f"Proceso {n} empieza")
    await asyncio.sleep(1)
    print(f"Proceso {n} termina")    
    
async def main():
    # Promise es una variable que puede haver llegado, que tengo o que llegará
    # .start()
    t1 = asyncio.create_task(worker(1))
    t2 = asyncio.create_task(worker(2))
    
    # .join()
    await asyncio.gather(t1,t2)
    
if __name__ in "__main__":
    asyncio.run(main()) # Primero corremos un bucle de eventos