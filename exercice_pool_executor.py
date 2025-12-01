# Crea 5 tareas que simulen diferentes operaciones (suma, resta, multiplicación, etc.) con diferentes tiempos de ejecución. 
# Las treas deberian ser tipo callback y deberias de poder ver sus resultados por separado (es decir son tareas independientes)

# cuando digo 5 pueden ser 10, 1000, etc... ya sabes
# La idea es usar hilos o procesos, de acuerdo a lo que juzgues necesario, para hacelro eficiente
import math
import time
from concurrent.futures import ProcessPoolExecutor


def calculadora(n1:int, n2:int, operation:callable):
    t0 = time.perf_counter()
    value = operation(n1,n2)
    elapsed = time.perf_counter() - t0
    return (operation.__name__,value,elapsed)

def sumar(n1, n2):
    """Suma simple - muy rápida"""
    return n1 + n2

def multiplicar(n1, n2):
    """Multiplicación - muy rápida"""
    return n1 * n2

def potencia(n1, n2):
    """Potencia - rápida a moderada"""
    return n1 ** n2

def raiz_cuadrada(n1, n2):
    """Raíz cuadrada de la suma - moderada"""
    return math.sqrt(abs(n1 + n2))

def trigonometrica(n1, n2):
    """Operaciones trigonométricas - moderada"""
    return math.sin(n1) * math.cos(n2) + math.tan(n1 + 0.1)

def logaritmica(n1, n2):
    """Logaritmos - moderada"""
    return math.log(abs(n1) + 1) * math.log(abs(n2) + 1)

def factorial_suma(n1, n2):
    """Factorial de números pequeños - lenta"""
    return math.factorial(int(abs(n1) % 10)) + math.factorial(int(abs(n2) % 10))

def iterativa_simple(n1, n2):
    """Iteración simple - moderada a lenta"""
    resultado = 0
    for i in range(int(abs(n1) % 1000)):
        resultado += math.sqrt(i + 1) * math.sin(i)
    return resultado + n2

def iterativa_compleja(n1, n2):
    """Iteración con cálculos complejos - lenta"""
    resultado = 0
    for i in range(int(abs(n1) % 5000)):
        resultado += math.sqrt(i + 1) * math.sin(i) * math.log(i + 1)
    return resultado / (abs(n2) + 1)

def muy_pesada(n1, n2):
    """Cálculo muy intensivo - muy lenta"""
    resultado = 0
    iteraciones = int(abs(n1) % 10000)
    for i in range(1, iteraciones + 1):
        resultado += (math.sqrt(i) * math.sin(i) * math.cos(i)) / (math.log(i + 1) + 1)
    return resultado * math.exp(n2 % 5)

if __name__ in "__main__":
    funciones = [
        sumar, multiplicar, potencia, raiz_cuadrada, trigonometrica,
        logaritmica, factorial_suma, iterativa_simple, iterativa_compleja, muy_pesada
    ]
    
    with ProcessPoolExecutor(max_workers=4) as pool:
        futuros = [pool.submit(calculadora, 1000,36,f) for f in funciones]
        
    for f in futuros:
        funct_name, value, elapsed = f.result()
        print(funct_name," value is ", value, " with time ",elapsed)