# BrigadeTaskScheduler

BrigadeTaskScheduler es un sistema de gestión de recursos diseñado para coordinar y optimizar las actividades de brigadas que realizan revisiones y reparaciones. Este proyecto se enfoca en la asignación eficiente de tareas a brigadas con el objetivo de minimizar el tiempo de resolución y el consumo de recursos.

## Descripción

El sistema se desarrolla en Python y utiliza estructuras de datos como colas para representar las brigadas y las tareas. Cada tarea está representada por un objeto con valores pseudo-aleatorios que indican la duración estimada de la tarea y los recursos necesarios para completarla. Por otro lado, cada brigada está representada por un objeto que contiene recursos disponibles y combustible que se consume durante las actividades.

## Características

- Gestión de tareas: asignación de tareas a las brigadas adecuadas en función de la disponibilidad de recursos y la ubicación.
- Optimización de recursos: minimización del tiempo y los recursos utilizados para completar las tareas.
- Simulación de espacio de trabajo: emulación de un área de trabajo inicialmente representada por una cuadrícula de 10000x10000.

## Uso

El sistema se ejecuta como una aplicación de consola. Se debe proporcionar la información de las tareas y las brigadas, y el sistema calculará la asignación óptima de tareas a las brigadas.

## Instalación

1. Clona el repositorio: `git clone https://github.com/tu_usuario/BrigadeTaskScheduler.git`
2. Navega al directorio del proyecto: `cd BrigadeTaskScheduler`
3. Ejecuta la aplicación: `python main.py`
