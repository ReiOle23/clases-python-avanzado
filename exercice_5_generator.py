# generator with a list that returns uppercase
uppercase_gen = (c.upper() for c in ["Barcelona", "Madrid", "Coruña", "Valencia"])
print(uppercase_gen) # generator
print(list(uppercase_gen))

# generator explicit
def nombres_mayus(lista_nombres):
    for n in lista_nombres:
        yield n.upper()
    
print(nombres_mayus)
print(list(nombres_mayus(["Barcelona", "Madrid", "Coruña", "Valencia"])))