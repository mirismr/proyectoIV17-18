[![Build Status](https://travis-ci.org/mirismr/proyectoIV17-18.svg?branch=master)](https://travis-ci.org/mirismr/proyectoIV17-18)

[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://agendalearning.herokuapp.com/)

Este es el repositorio de mi proyecto personal para la asignatura Infrestructura Virtual. En este [enlace](https://mirismr.github.io/proyectoIV17-18/) se encuentra información extra del proyecto (documentación interesante, etc).

## Descripción
Para el proyecto de la asignatura he decidido realizar un bot de *Telegram* que permita consultar la agenda de un determinado día. Además, también incorporará la funcionalidad de permitir modificar la misma, añadiendo o eliminando tareas que ya se hayan completado. El proyecto está pensado de forma personal para administrar una agenda orientada a llevar un seguimiento de clases particulares, donde el profesor podría consultar la hora, el sitio, si la clase es online o presencial, el nombre del alumno, la materia, etc.
El despliegue en la nube se hará con *Heroku*. Además para los test de integración contínua se usará *TravisCI*.

## Servicios requeridos
- API de *Telegram*.
- Lenguaje de alto nivel: *Python*.
- Base de datos: *sqlite3* y *PostgreSQL*, donde se almacenarán todos los datos requeridos para gestionar las clases.

## Tests
Para la realización de los tests en *Python* he usado la librería *Unitest* dado su simplicidad y que no requiere ninguna instalación extra.

## Integración contínua
Podemos ver la configuración de *TravisCI* en el [siguiente enlace](https://mirismr.github.io/proyectoIV17-18/).

## Despliegue
Podemos ver la configuración de *Heroku* en el [siguiente enlace](https://mirismr.github.io/proyectoIV17-18/).