# 3 dimensiones (explicita, implicita, por que)

# Explicita
# Usuario y contraseña és explicito, fuera de logica de negocio de libros.
# Implicita, influencia en alguna necessidad de disseño
# Usuario y contraseña implicito, disseño tiene que adaptarse.
# Por que
# Sin Usuario y contraseña no podria funcionar.

# -------------------------------
# Persistencia de datos

# explicita
# definir una base de datos
# implicita
# Definir los modelos
# Por que
# de esta forma se mantienen los datos en el tiempo

# -------------------------------
# Sistema de errores

# explicita
# Vamos a disseñar un sistema de errores
# implicita
# implmenetar un sistema de login i elastic para subir los logs
# Por que
# para visualizar los possibles errores


# Caracteristicas operacionales
# como funciona (Ej. escalabilidad)
# - escalabilidad: ejemplo, usuarios multiplicamos * 10.
    # cache, o dividir base de datos, o indices en sql, utilizar docker, contenedores, sistemas elasticos
    # medidas: mirar la cpu, mirar el frontend(en que pantalla passan más tiempo estancados), tiempos de carga
# - robustez: capacidad que tiene un sistema de no quebrarse
    # condicion limite, caso que sbemos que puede dar error pero intentamos no llegar al fallo.
    # microservicios
    # medidas: mirar cuantos fallos hemos tenido en 1 año
# - availability: capacidad de ejecutarse en el momento que se requiera
# - performance: muchas metricas, bajar la latencia de operaciones del sistema (cuando los clientes nos indiquen que hay mucho tiempo de espera)
# - reliability: si el sistema es confiable o no

# Caracteristicas estructurales
# como se disseña (Ej. estabilidad)
# - mejorabilidad: facilidad de un codigo de mejorar
    # medidas: augmentamos capacidad del equipo para ver la facilidad del codigo
# - configurabilidad: capacidad de exportar datos de config facilmente
# - extensibilidad: si el sistema es extensible facilmente
# - portabilidad: capacidad de un sistema de funcionar en diferentes entornos
# - reusabilidad: todo lo que nos ayude a abstraer
# - localización: capacidad de sistema de traducir en diferentes idiomas
# - accessibilidad: capacidad de sistema para adaptarse a tipos de personas con incapacidades(ciegos)
# - autenticación: capacidad de un sistema de verificar quien es ese usuario
# - autorización: perfil del usuario.
# - privacidad: anonimizar datos sensibles, (base de datos).
# - seguridad: encripción, seguridad de roles, seguridad de datos ...

# - complejidad ciclomatica: métrica de software que cuantifica la complejidad lógica 
# de un programa midiendo el número de rutas de ejecución independientes a 
# través de su código fuente. Se utiliza para evaluar la calidad, el mantenimiento y 
# la capacidad de prueba de un programa, ya que un valor más alto indica una mayor 
# complejidad, lo que puede llevar a un mayor riesgo de errore



# # # # # # # # Catas # # # # # # # #
# Ecomerce de sandwiches en españa, que llegan en dos dias, usuarios millones en ciertos dias concretos
# Implementar un sistema de atencion al cliente
# las tiendas estan franquiciadas, tipo McDonalds
# Tienen planes para moverse en Portugal, Francia, Alemania

# Sistema de seguridad(facturas, contratos)
# Sistema de pagos
# Sistema de autenticación
# Sistema tiene que ser escalable
# Sistema robusto
# Sistema geografico de reparto
# Sistema de llamadas
# Sistema de localizacion(idiomas)
# Sistema portable sobretodo a los mobiles
# Sistema de datos de negocio
# Sistema de control de ofertas y productos

# Como va a impactar a nivel de ngocio
# - numero de usuarios segun fecha
# - si tenemos exito va a crecer el negocio y los usuarios
# - logistica en el negocio
# - sistema contabilidad si la persona quiere pagar en efectivo

# Caracteristicas explicitas
# - anonimizar datos sensibles, contratar empresa con auditoria que vaia mirando problemas de turno.

# Caracteristicas implicitas
# - vulnerabilidades que vaian surgiendo


# Escalabilidad
# Caracteristicas explicitas
# - diseñar un sistema que se adapte a la cantidad de usuarios del momento

# Caracteristicas implicitas
# - Utilizar contenedores en servers cloud para autoescalado segun peticiones


# sistemas escalables pero no elasticos
# elastico es que puedes decrecer

# explicito
# departamento que estudi los kpi necessarios para el negocio
# implicito
# implementamos un sistema de monitoracion de estos kpi