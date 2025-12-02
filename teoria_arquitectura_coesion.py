# tenemos un equipo de 10 personas y ahi que actualizar los carritos de la compra
# incovenientes, teams no deja rastreo facil con muchas personas, mail es mas trabajo 
# escrivir mail para cada persona


# coesion -> habilidad de un elemento de un componente tenga sentido en ese componente 
# acopladas -> grado de dependencia entre módulos sea el minimo possible

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


# Cohesion funcional
def calcular_promedio(nums):
    return sum(nums) / len(nums)

def calcular_min(nums):
    return min(nums)

def calcular_max(nums):
    return max(nums)

# Cohesion secuencial
def obtener_datos():
    return "123,456,789"

def parsear_datos(raw):
    return list(map(int, raw.split(",")))

def procesar_secuencia():
    raw = obtener_datos()
    datos = parsear_datos(raw)
    return sum(datos)

# Cohesion comunicacional
def cargar_cliente(cliente_id):
    return {"id": cliente_id, "nombre": "Pedro", "saldo": 100}

def actualizar_saldo(cliente, nuevo_saldo):
    cliente["saldo"] = nuevo_saldo

def imprimir_cliente(cliente):
    print(f"Cliente: {cliente['nombre']} - Saldo: {cliente['saldo']}")

# Cohesion procedural (banera amarilla)
def abrir_archivo():
    print("Archivo abierto.")

def procesar_archivo():
    print("Archivo procesado.")

def cerrar_archivo():
    print("Archivo cerrado.")

def pipeline_archivo():
    abrir_archivo()
    procesar_archivo()
    cerrar_archivo()

# Cohesion temporal (bandera roja)
def inicializar_logs():
    print("Logs inicializados.")

def cargar_configuracion():
    print("Configuración cargada.")

def abrir_conexion_bd():
    print("BD conectada.")

def startup():  # Si cambio el orden se rompe)
    inicializar_logs()
    cargar_configuracion()
    abrir_conexion_bd()

# Cohesion semantica o logica (no es bandera roja, a veces es inevitable)
def manejar_evento_click(evento):
    print("Procesando click")

def manejar_evento_tecla(evento):
    print("Procesando tecla")

def manejar_evento_redimension(evento):
    print("Procesando redimensionamiento")

def despachar_evento(evento, tipo):
    if tipo == "click":
        manejar_evento_click(evento)
    elif tipo == "tecla":
        manejar_evento_tecla(evento)
    elif tipo == "resize":
        manejar_evento_redimension(evento)

# Cohesion accidental (siempre bandera muy roja)
def convertir_a_mayusculas(texto):
    return texto.upper()

def calcular_impuesto(precio):
    return precio * 0.21

def lanzar_dado():
    import random
    return random.randint(1, 6)
 