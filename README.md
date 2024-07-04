# TFM - FIWARE Deployment

Este repositorio contiene la configuración para desplegar un entorno FIWARE utilizando Docker Compose. Este entorno incluye varios servicios de FIWARE, como Orion Context Broker, Quantum Leap, IoT Agent, y bases de datos necesarias para su funcionamiento.

## Contenido

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Servicios Incluidos](#servicios-incluidos)
- [Requisitos Previos](#requisitos-previos)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Verificación del Despliegue](#verificación-del-despliegue)
- [Diagrama del Entorno](#diagrama-del-entorno)
- [Comandos de Servicios](#comandos-de-servicios)
- [Licencia](#licencia)

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
