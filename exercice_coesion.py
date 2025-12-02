
##### coesion funcional (no tiene dependencia)
# def calcular_promedio()
# def calcular_min()
# def calcular_max()

##### coesion sequencial (dependencia explicita)
# def obtener_datos()
# def parsear_datos()
# def procesar_secuencia():
    # raw = obtener_datos()
    # datos = parsear_datos()
    
##### coesion comunicacional (relacionados entre si, dependencia implicita )


##### coesion procedural (orden especifico de ejecucion (tiene sentido), solo el orden)

##### coesion temporal (orden especifico de ejecucion, pero no tiene sentido)

##### coesion logica (intentar evitar) (coesion semantica, pero no tecnica)

##### coesion coincidencia (codigo que no tiene nada que ver)


# coesion funcional
class Library():
    
    def add_book():
        print("New book added")
        
    def loan_book():
        print("Book loaned")

# coesion sequencial
def get_user():
    return User()
def get_book():
    return Book()
def loan_book():
    user = get_user()
    book = get_book()
    book.loan_to(user)

# coesion procedural
def set_book_to_user():
    print("set book")
def set_book_is_loaned(book):
    book.loaned(True)
def loan_book():
    get_book()
    set_book_to_user()
    set_book_is_loaned()

# coesion logica
def task_add_book(book):
    print(book)
    
def task_add_library(library):
    print(library)
    
def task_create_place():
    task_add_book()
    task_add_library()