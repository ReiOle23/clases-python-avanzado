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
    # - Servicio viages, servicio comercial, servicio tecnologia, etc
    # - servicios de infraestructura, servicios de applicacion, servicios de dominio, servicios de base de datos
    # cada servicio tiene su propia base de datos, que se conectan con la taxonomia definida
    # orquestración -> implica que los servicios vaian uno detras de otro (no te puedo dar un seguro si no tienes coche)
    # servicios de apoyo (orquestrador): conecta entre un servicio a otro para gestionar este problema.
    # todo se base en el orquestrador.
    # kuanta 1 (un despliegue), desplegar es muy complicado, cambios deven estar bien comunicados con taxonomia y orquestrador
    # la mas dificil de testear, muy buena escalando, muy elastica, es la mas cara de todas.
    
# - Microservicios
    # - 

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
    
# - Basado en espacio


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
        