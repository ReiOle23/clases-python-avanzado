from multiprocessing import Pool, cpu_count

def elevar_cuadrado(numero):
    resultado = numero ** 2
    print(f"[Proceso {numero}] - {numero}^2 = {resultado}")
    return resultado

if __name__ == "__main__":
    numeros = list(range(1, 9))
    cpus = cpu_count()
    print(cpus)
    # with Pool(4) as p:
    with Pool(cpus-1) as p:
        # p.map(elevar_cuadrado, numeros)
        r = p.map(elevar_cuadrado, numeros)
        
    print(r)
    for res in r:
        print(res)
        
# from multiprocessing import Pool, cpu_count

# def elevated_values(value1: int, value2:int) -> int:
#     return value1 ** value2

# if __name__ == "__main__":
#     values = [(100,200),(30,50),(40,5),(300,10),(150,40)]
#     p = Pool(cpu_count())
#     with p as pool:
#         results = pool.starmap(elevated_values, values)
        
#     for res in results:
#         print(res) 