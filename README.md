 # :page_facing_up: TFM - Documentación FIWARE 
 
Este repositorio contiene la configuración para desplegar un entorno FIWARE utilizando Docker Compose. Este entorno incluye varios servicios de FIWARE, como Orion Context Broker, Quantum Leap, IoT Agent, y bases de datos necesarias para su funcionamiento.

## Contenido

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Servicios Incluidos](#servicios-incluidos)
- [Requisitos Previos](#requisitos-previos)
- [Configuración](#configuración)
- [Documentación y Despliegue](#documentación-y-despliegue)

## Descripción del Proyecto

El objetivo de este proyecto es proporcionar un entorno completo para la gestión de datos de IoT utilizando la plataforma FIWARE. Este entorno permite la integración de datos desde dispositivos IoT, el almacenamiento de datos históricos y la visualización de datos en tiempo real.

## Servicios Incluidos

### Orion Context Broker

Orion es el broker de contexto que gestiona y almacena la información de contexto. Se comunica con la base de datos MongoDB para el almacenamiento de datos.

### Quantum Leap

Quantum Leap se encarga de persistir la historia a corto plazo en CrateDB. Permite consultas avanzadas sobre los datos históricos.

### IoT Agent

El IoT Agent se configura para el protocolo UltraLight y maneja la comunicación con dispositivos IoT. Utiliza MongoDB para almacenar la información del dispositivo y Mosquitto como broker MQTT.

### MongoDB

MongoDB se utiliza como base de datos para almacenar los datos de contexto del Orion Context Broker y la información del IoT Agent.

### CrateDB

CrateDB se utiliza para el almacenamiento y consulta de datos históricos a corto plazo, manejados por Quantum Leap.

### Grafana

Grafana se utiliza para la visualización de datos en tiempo real. Se conecta a CrateDB para mostrar gráficos y paneles interactivos.

### Mosquitto

Mosquitto es un broker MQTT utilizado para la comunicación entre el IoT Agent y los dispositivos IoT.

## Requisitos Previos

- Docker
- Docker Compose

Asegúrate de tener instalados Docker y Docker Compose en tu sistema.

## Configuración

Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:

```env
ORION_VERSION=latest
ORION_PORT=1026
QUANTUMLEAP_PORT=8668
ULTRALIGHT_VERSION=latest
IOTA_NORTH_PORT=4041
MONGO_DB_VERSION=latest
MONGO_DB_PORT=27017
CRATE_VERSION=latest
GRAFANA_PORT=3000
GRAFANA_APP_PORT=3000
```

## Documentación y Despliegue

Este script, escrito en Bash, facilita la gestión de contenedores Docker para el entorno FIWARE, permitiendo crear, iniciar, detener y eliminar contenedores y recursos asociados. A continuación, se detalla su funcionamiento:

### Comprobación de Argumentos

El script primero verifica el número de argumentos pasados para determinar el comando de Docker Compose a utilizar. Si se pasan exactamente dos argumentos, se utiliza `docker-compose`; de lo contrario, se opta por `docker compose`. Además, si se invoca el script sin argumentos o con un número incorrecto de estos, se muestra un mensaje de error y se termina la ejecución.

### Funciones Principales

- **loadData**: Esta función se encarga de esperar a que los servicios MongoDB, Orion Context Broker, IoT Agent, CrateDB y Grafana estén disponibles. Una vez listos, ejecuta un contenedor Docker temporal para cargar datos de dispositivos provisionales en el entorno.

- **stoppingContainers**: Detiene los contenedores en ejecución utilizando el comando de Docker Compose determinado al inicio del script.

- **downContainers**: Similar a `stoppingContainers`, pero además elimina los contenedores, volúmenes, y redes asociadas, limpiando completamente el entorno.

- **displayServices**: Muestra los contenedores en ejecución y sus puertos, proporcionando una visión general del estado del entorno.

- **addDatabaseIndex**: Añade índices en las bases de datos MongoDB para optimizar las consultas realizadas por Orion Context Broker y el IoT Agent.

### Espera de Servicios

El script incluye varias funciones (`waitForMongo`, `waitForOrion`, `waitForIoTAgent`, `waitForCrateDB`, `waitForGrafana`) diseñadas para esperar a que un servicio específico esté completamente disponible antes de proceder. Esto se logra mediante la verificación del estado de salud del contenedor o la respuesta de una solicitud HTTP.

### Ejecución de Comandos

El script acepta los siguientes comandos como primer argumento:

- **start**: Inicia los contenedores y carga los datos provisionales.
- **stop**: Detiene los contenedores en ejecución.
- **create**: Prepara el entorno descargando las imágenes Docker necesarias.
- **down**: Detiene y elimina los contenedores, volúmenes, y redes.

Cada comando activa una serie de acciones específicas definidas en las funciones correspondientes.

### Uso

Para utilizar el script, en primer lugar se deben crear y descargar las imágenes de DockerHub con el siguiente comando:

```bash
./services create
```

A continuación, para desplegar el entorno de FIWARE se debe lanzar el siguiente comando:

```bash
./services start
```
