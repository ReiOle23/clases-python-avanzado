# Arquitecturas

# las diferenciamos por sistemas distribuidos o monoliticos
# monolito:
# Ej. un unico repo con todo el codigo

# Modelo vista controlador (particionado tecnico)
# capa de vista
# capa de dominio(controladores)
# capa de persistencia

# domain driven design DDD (particionado por dominio)
# parte para inventorio
# parte para pasarela de pagos
# parte para registro usuarios

###### particionado por dominio, o por tecnico

# particionado tecnico cuando tenemos un sistema crud claro

# particionado por dominio cuando no tenemos sistema crud claro
# ej. si tenemos facturas o pagos que no tienen cruds

# desventajas de particionado tecnico
# - grado de acoplamiento es mayor en particionado tecnico
#   acoplamiento a nivel de datos tiene a ser monolitos y tener solo una base de datos
# - mas propenso a que exista codigo duplicado en la misma capa




# Silicon sanwiches como lo particionamos
# haria un sistema por dominio porque de crud solo tenemos los usuarios
# Pasarela de pagos, geolocalización, kpi mejor dividir por partes

# Implementación por capas(particionado tecnico)
# - api , urls, vistas, test vistas
# - core, domain(modelos), controlladores(servicios), test servicios
# - database

# Componentes
# - recetas
# - carrito de compra 
# - pagos
# - compra
# - ordenes y envio de reparto
# - promociones
# - localizacion
# - gestión de usuarios

# Componentes de DDD (No hay controlador)
# tenemos 

# - Pagos (controllador)
#   - promociones (controllador, )
#       
# - recetas (controllador, se vincula con )

# - inventario, lo que tenemos para hacer las recetas (No controllador)
# - ordenes y envio de reparto (controllador)
# - localizacion (controllador)

# - gestión de usuarios (controllador)
#   - carrito de compra (Se conecta solo con gestion de usuarios)

# # # v# # # # # # # # # # # 
# Patrones de arquitectura
# Monolitos:
# - Arquitectura por capas (MVC, DDD, Hexagonal)
    # - Consiste en tener un codigo separado por capas(abiertas o cerradas)
    # - cuando tengo mas de 4 capas y la logica de negocio es complicada se cierra.
    # - tener componentes compartidos (con un redis, clave valor) Por tema asyncronia o 
    # por evitar miles de peticiones a base de datos de descuentos(escalable)
    # Cuando usarla: Utilizar la mayoria , se puede cambiar a microservicios.
    # Bueno: Simple y barata.
    # Problemas: Ancho de banda
    # kuanta: 1, Es facil desplegar, No es elastico(no puedes adaptarte), 
    # dificultad Incremental, poco Modular(No puedo gestionar muchos componentes independiente)
    
    
# - Pipeline (sistema tecnico)
    # - Es una estructura que se define por dos componentes (input, output)
    # - Sequencial, codigo lineal
    # - Ej. Datos de pedido (pipe pedido, line pago) / n8n es pipeline
    # - Se basa en comunicaciones entre ellos
    # - Los filtros deben funcionar por si solos.
    # - Ej. tengo un mobil y quiero saber cuanto tiempo estoy. 
    # Tengo un proceso que me mira cuanto tiempo estoy con el mobil, esos datos los pasamos a otro filtro
    # que divide ese output con diccionarios distintos, lo pasamos (pipe) a otro filtro que los pasa a la base de datos.
    # Asincronia que mande una pipe a 3 filtros diferentes
    # kuanta: 1, Es facil desplegar, Redespliegue es complicado(desplegar filtros en orden), No es elastico, 
    # no tiene buena performance(si se cae un componente se caen todos), Modular(puedo gestionar muchos componentes independiente)
    # no es muy escalable
    # aplicar cuando los datos sean flujos de datos, que sean complicados ETL (no hay crud).
    # analisis de datos se aplica pipeline.
    
# - Kernel (nucleo)
    # - rompes el monolito con lo que necessitas.
    # - ej con django de sandwiches y queremos meter sistema de descuentos
    # - és independiente, entonces hacemos un componente partido que llamamos cuando lo necessitemos
    # - vscode el sistema de extensiones es un sistema kernel (instalas cuando lo necessitas)
    # - Django es un sistema de kernel, de nucleo
    # puede ser local (librerias de django) y llamadas que seria stripe que hacemos pasarela de pago
    # base de datos es el nucleo. Las extensiones se adaptan al nucleo. Contrato es estandar que definimos con el nucleo
    # y las extensiones para que no quiebre la base de datos
    # Particionado dominio y tecnico, kantas 1(despliegues), no es elastico, Modular facil de evolucionar, 
    # buena performance(solo dependen del nucleo), es barato, es dificil, poco escalable.
    # Cuando utilizarlo: 1. Clientes con necessidades totalmente distintas, 2. monolito que queremos romper en arquitectura distribuida,
    # 3. cuando queremos monolito pero queremos buena performance.
    

# Distribuidos:
# - Por eventos
    # - 

# - Orientado a servicios
    # - Taxonomia es como definimos 
    # - departamento de viajes, seguro de vida, legal, comercial
    # - todos son clientes, la taxonomia define como todos esos datos se comunican (tabla de tablas)
    # - Se utiliza en bancos
    # - Servicio viajes, servicio comercial, servicio tecnologia, etc
    # - servicios de infraestructura, servicios de applicacion, servicios de dominio, servicios de base de datos
    # cada servicio tiene su propia base de datos, que se conectan con la taxonomia definida
    # orquestración -> implica que los servicios vaian uno detras de otro (no te puedo dar un seguro si no tienes coche)
    # servicios de apoyo (orquestrador): conecta entre un servicio a otro para gestionar este problema.
    # todo se base en el orquestrador.
    # kuanta 1 (un despliegue), desplegar es muy complicado, cambios deven estar bien comunicados con taxonomia y orquestrador
    # la mas dificil de testear, muy buena escalando, muy elastica, es la mas cara de todas.
    
# - Microservicios
    # - surge de la idea de DDD, contexto limitado
    # servicios lo mas pequeño possibles, con su propia base de datos, para meterlos en contenedores
    # mediante colas asyn se comunican entre ellos
    # Capa de exterior(servicios api), capa interior(servicios que se dedican a hacer cosas pequeñas)
    # arquitectura distribuida porque cada una corre en su propio contexto
    # te permite servicios con lenguajes y bases de datos diferentes.
    # Son eficientes para escalar horizontalmente, pero verticalmente no
    # la idea és que sean lo mas granulaes possibles, el gran reto son las transacciones entre ellos
    # sobretodo en base de datos.
    # Solucion al caos de comunicacion entre ellos: aislar lo mas possible o hacemos una arquitectura dedicada a ello.
    # patron sidecar, servicio dentro de otro para tener una capa intermedia entre dos microservicios.
    # service mesh, red entera de servicios.
    # orquestracion y coreografia
    # orquestracion: servicio conector entre grupos de servicios(se dividen por dominio). seria un Mediador
    # coreografia: comunica los servicios entre si en un orden sincrono. Seria un Broker
    # kubernetes es un orquestrador
    # ansible es un coreografiador
    # Si queremos mantener la consistencia de la base de datos, utilizamos patron saga que cuenta las transacciones que se hacen
    # para que se ordenen en un orden logico.
    # Para rastrear errores necessitare un service mesh para rastrear transacciones.
    # por dominio, quantas: numero de microservicios*contenedores*capas, coste es caro, no tiene mucha performance
    # implementaciones son sencillas, son todos idempotentes, testeo super dificil, redespliegue y escalabilidad muy buenos.

# Especiales:
# - Basado en servicios (mezcla monolito y distribuido) (particionado de dominio)
    # - Tiene interfaz de datos en comun
    # - api de pagos, api de recetas, api de mails y todas estan conectadas a la misma base de datos y al mismo frontal
    # Base de datos compartida
    # - Se puede tener interfaz para web y para mobil.
    # Tiene sentido utilizar un gateway (se encarga de enviar info entre interfaces y base de datos)
    # kantas n(interfaces), facil de redesplegar componentes y dificil de desplegar base de datos e interfaz de usuario
    # elastica pero no tanto(por la base de datos), capacidad de evolucion = a la de nucleo, Es modular pero comunicaciones entre servicios
    # Mas cara que un monolito, pero no muy cara, facil de testear, confiable(si se cae algo puedes arreglarlo facil)
    # Problema: tener en cuenta el orden de las transacciones
    # Cuando utilizar: en DDD es lo mas comun, buena arquitectura cuando se aplica bien.
    
# - Basado en eventos(espacio)
    # patron asyncrono
    # No es tipo crud
    # sistema de subastas, te tienes que adaptar al estado de las apuestas
    # por eso utilizamos eventos, y se van comunicando entre ellos.
    # Dos topologias: Broker -> mas senzilla, Mediador -> mas complicada.
    # ej de evento: Geofence, evento que hace un radio de 30 metros de seguridad.
    # si el mobil de agresor entra en esos 30 metros, envia notificacion por la red al dispositivo
    # del cliente para saber que esta alli.
    # Topologia Broker:
    # Todos los eventos estan conectados con un Broker. Kafka, define topicos(ej. Pajaros),
    # productores de eventos(ej. Fotografos), consumidores(ej. aficionados a los pajaros)
    # asincronia entre productores, broker y consumidores.
    # broker recibe y envia
    # No todos los eventos tienen que pasar por broker
    # todos los servidores son brokers de eventos
    # los topics pueden tener mas de 1 evento
    # es asyncrono todo, para evitar, con el broker metemos un orquestrador de estado para ver como va cada evento.
    # interfaces graficas para que nos enseñe, red panda.
    # desacoplado, es muy escalable, elastico, areglar errores rapido(puedo desplegar evento rapido),
    # muy complejo de entender, la transaccion es fragil, es muy complicado hacer rollback de un evento.
    # Topologia de Mediador
    # Mediador que gestiona eventos. Como una cola asyncrona, envia por canales el evento.
    # toda comunicacion passa por el mediador(broker), (mediadores secundarios o terciarios)
    # mediadores serian como capas(particionado por dominio)
    # suele ser mas complejo que el de Broker, py manejo de errores con flower
    # particionado tecnico, quanta(numero de servicios), compleja pero simple, altamente modular, escalable


# cosas criticas
# La red nunca es fiable
# ancho de banda no es infinito (cuidar tamaño de peticiones)
# La latencia nunca és 0 (por eso asyncronia)
# la red no es segura
# topologia siempre puede cambia
# la red no es gratuita
# la red no es homogenea
# siempre que consideremos un patron de arquitectura lo haremos en base a la base de datos


# Sistema de apuestas deportivas
    # - Arquitectura por capas
        # Componente Gestion de usuario
        # Componente Apuestas 
        # componente Pagos
        # Componente Calculador de recompensa

    # - Pipeline
        # Componente Generar Apuesta -> Componente Pago -> Componente Guardar apuesta 
        #                                               -> componente calculo de recompensa
    
    # - Kernel
        # Componente base (gestion Usuario, base de datos)
        # Extension pago
        # Extension calculo
        


# en una arquitectura basada en servicios es facil hacer cambios
# examen es tipo test 20 preguntas 8 de codigo, 8 arquitectura y 4 de diseño(algo de diseño que este mal)
# certificacion es tipo test y tipo practica


