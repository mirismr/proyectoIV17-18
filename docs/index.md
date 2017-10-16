# Proyecto de Infraestructura Virtual
Aquí se expondrá información extra del proyecto.

## Configuración TravisCI

Lo primero que debemos hacer es entrar en la [página de TravisCI](https://travis-ci.org/) y logearnos con nuestro perfil de *GitHub*. Damos permiso para poder trabajar con el servicio y elegimos el repositorio del proyecto.
A continuación, tal y como indican en esa misma página, debemos añadir el archivo `.travis.yml`, en el cual debemos incluir características interesantes de nuestro proyecto, por ejemplo: el lenguaje utilizado, cómo instalar las dependencias, realizar los tests, etc.

Lo primero que haremos será instalar las dependencias. Para ello, debemos tener un archivo llamado `requirements.txt`. En dicho archivo se incluyen las aplicaciones necesarias y la versión para nuestro proyecto. El comando que realizar esta tarea es `pip3 install -r requirements.txt`.

Para la realización de los tests simplemente debemos ejecutar el comando `python tests.py`, siendo `tests.py` el archivo donde se encuentran los tests de mi proyecto.

Así pues, para automatizar esta tarea, nos vamos a servir de un fichero *Makefile*:
~~~
install:
    pip install -r requirements.txt

tests:
    python3 tests.py
~~~

Por lo cual, nuestro archivo `.travis.yml` es:
~~~
language: python
python:
    - "3.0"

install: make install

script: make tests
~~~