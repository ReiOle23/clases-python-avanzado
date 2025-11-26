# patron estrategia
def ingresar(dinero):
    if dinero >100:
        print("Taxi")
    elif 20 < dinero <= 100:
        print("Bus")
    elif dinero <= 20:
        print("Caminar")
        
# generador que metes una palabra y te va dando sus letras
def letters_generator(word):
    word = word.replace(" ","")
    word_len = len(word)
    for l in word:
        yield l
        yield ord(l)
    yield word_len
    
g = letters_generator("Oleguer")

for l in g:
    print(l)