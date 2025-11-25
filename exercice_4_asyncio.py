import asyncio
from typing import TypeVar

T = TypeVar("T", int, float)

async def multiply(n: T, n2: T) -> T:
    return n*n2

async def main(pairs: list[tuple[T,T]]):
    tasks = [asyncio.create_task(multiply(*p)) for p in pairs]
    result = await asyncio.gather(*tasks)
    print("Resultados finales:", result)
    
if __name__ in "__main__":
    pairs = [(3, 4.2), (5, 6.7), (7, 8), (9, 10)]
    asyncio.run(main(pairs))
    
    
# import asyncio
# from typing import TypeVar

# T = TypeVar("T", int, float)

# async def multiplicar(a: T, b: T) -> T:
#     return a * b

# async def main():
#     pares = [(3, 4), (5, 6), (7, 8), (9, 10)]
#     tareas = [asyncio.create_task(multiplicar(a, b)) for a, b in pares]
#     resultados = await asyncio.gather(*tareas)
#     print("Resultados finales:", resultados)

# if __name__ == "__main__":
#     asyncio.run(main()) 