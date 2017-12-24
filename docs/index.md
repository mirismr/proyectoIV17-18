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
    pip3 install -r requirements.txt

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

Ahora si nos vamos a la web podemos ver el resultado:
![Build passed](img/1.png)


## Configuración despliegue en Heroku
Instalamos el toolbelt con el siguiente comando: `wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh`

Nos damos de alta en *Heroku*. Lo hacemos a través de su [página oficial](https://signup.heroku.com/?c=70130000001x9jEAAQ):

![Registro](img/2.png)

Una vez hecho esto, confirmamos la cuenta en el correo y establecemos la contraseña. Se nos redirigirá a la página inicial de *Heroku*:

![Logeados](img/3.png)

A continuación añadimos nuestra aplicación tal y como se muestra en la siguiente imagen:

![Añadir app](img/4.png)

Ahora enlazamos nuestro repositorio de *GitHub* con *Heroku*, indicando el nombre de nuestro repositorio. Además podemos automatizar el proceso de que cuando se haga un push se despliegue automáticamente (y pasando los test de *TravisCI*). El proceso se muestra en las siguientes imágenes:

![Enlace](img/5.png)

![Enlace](img/6.png)

![Enlace](img/7.png)

Lo siguiente que debemos hacer es crear una base de datos *PostgreSQL*. Para ello instalamos el *addon* de *PostgreSQL* en nuestra aplicación:

![Base de datos](img/8.png)

![Base de datos](img/9.png)

Una vez hecho esto, ya tenemos todo configurado respecto a lo que tenemos que hacer en la página de *Heroku*. A continuación, debemos crear en nuestro repositorio un archivo llamado `Procfile`, que contendrá la información acerca de lo que tiene que hacer *Heroku* para desplegar nuestra aplicación. En mi caso, será ejecutar el archivo `bot.py`, así que contendrá la siguiente línea de código:

`worker: python3 bot.py`

y `web: gunicorn web:app --log-file=-`

Una vez hecho esto, trabajaremos normal y haremos tantos push como deseemos. Si nos vamos a la página de log de *Heroku* veremos que nuestro bot está funcionando (Primera versión de prueba que solo imprime una cadena):

![Prueba despliegue bot](img/10.png)


Nota: Como nuestro despliegue no tiene sentido en la web (ya que solamente es un archivo .py ejecutándose que dará vida al bot) si accedemos a la dirección del [despliegue](https://agendalearning.herokuapp.com/) nos dará *status:ok*, pero basta con fijarnos en los logs para comprobar que efectivamente funciona.
También podemos comprobarlo en [*Telegram*](https://web.telegram.org/#/im?p=@agendaLearningBot).

## Instalación Docker

Seguimos los pasos de la [documentación de Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04).

Añadimos la clave GPG con `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -` y ejecutamos para añadir el repositorio `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`.

Actualizamos los repos `sudo apt-get update` y con `apt-cache policy docker-ce` vemos:

![Cache Docker](img/11.png)

Para instalar Docker introducimos el comando `sudo apt-get install -y docker-ce`:

![Instalar Docker](img/12.png)

Comprobamos que está activo:

![Instalar Docker](img/13.png)

## Usando Docker y DockerHub

Primero haremos las pruebas en local y a continuación usaremos *DockerHub*.

Lo primero de todo será crear el Dockerfile: 
~~~
FROM ubuntu:14.04
MAINTAINER Míriam Mengíbar Rodríguez <mirismr@correo.ugr.es>

ARG TOKEN_BOT
ENV TOKEN_BOT=$TOKEN_BOT


#Instalamos git
RUN sudo apt-get -y update
RUN sudo apt-get install -y git

#Clonamos el repositorio
RUN sudo git clone https://github.com/mirismr/proyectoIV17-18.git


#Instalamos las herramientas de python necesarias
RUN sudo apt-get -y install python3-setuptools
RUN sudo apt-get -y install python3-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python3-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get -y install python3-pip

#Instalamos los requerimientos necesarios
RUN cd proyectoIV17-18 && make install

EXPOSE 80
CMD cd proyectoIV17-18 && ./scriptDespliegue.sh
~~~

Este fichero se encargará de indicarle a Docker las dependencias y demás herramientas que necesita nuestra aplicación tener instaladas en el contenedor para que funcione.

Para la prueba en local, ejecutamos el comando `docker build -f Dockerfile -t contenedor-learningbot .`:

![Instalando en local](img/14.png)

Podemos ver como se ejecutarán todos los "pasos" de nuestro *Dockerfile*.
Cuando termine, podemos ver como se ha creado el contendor para nuestra aplicación:

![Instalando en local](img/15.png)

A continuación ejecutamos el comando `sudo docker run --env TOKEN_BOT=XXX -i -t contenedor-learningbot /bin/bash`, donde se ha omitido el token del bot por privacidad, y ejecutamos el bot:

![Instalando en local](img/16.png)

Podemos comprobar que funciona.

Para la disponibilidad en DockerHub, primero debemos registrarnos en la página de [Docker](https://hub.docker.com/), a través del sencillo formulario.
Nos llegará un correo de confirmación y ya estamos registrados.

Una vez hecho esto, nos dirigimos a "Settings" y, desde "Settings", a "Linked Accounts & Services". Elegimos GitHub, "Public and Private" y lo autorizamos:

![DockerHub](img/17.png)
![DockerHub](img/18.png)
![DockerHub](img/19.png)

Ahora nos dirigimos al menú "Create", "Create Automated Build". Seleccionamos GitHub de nuevo y el repositorio:

![DockerHub](img/20.png)
![DockerHub](img/21.png)

Quedando finalmente:

![DockerHub](img/22.png)

Para descargar y lanzar el contenedor ejecutamos: `sudo docker pull mirismr/proyectoiv17-18` y `sudo docker run --env TOKEN_BOT=XXX -i -t mirismr/proyectoiv17-18 /bin/bash`

## Despliegue en Zeit


Lo instalamos a través del comando `npm install now -g` según su [página](https://zeit.co/):

![Zeit](img/23.png)

A continuación, nos vamos al directorio donde esté el Dockerfile y ejecutamos `sudo now --public`:

![Zeit](img/24.png)

Ahora ejecutamos `now -e "TOKEN_BOT=XXX` para desplegarlo y obtener el link:

![Zeit](img/25.png)

## Despliegue en Azure

Azure nos permitirá desplegar nuestra aplicación en IaaS. Hemos podido realizar esta tarea gratuitamente gracias al código proporcionado por el profesor de la asignatura.

Primero debemos instalar Vagrant, que nos permitirá crear la máquina virtual. Yo ya la tenía instalada de la asignatura DAI. A continuación instalamos el plugin de Azure para Vagrant:

![Plugin](img/26.png)

A continuación, instalamos Ansible para automatizar el proceso:

![Ansible](img/27.png)

Y configuramos el fichero `var.yml` donde declaramos variables y dependencias del sistema:

~~~
project_name: proyectoIV17-18
project_repo: https://github.com/mirismr/proyectoIV17-18.git
project_path: .

system_packages:
  - build-essential
  - npm
  - git
~~~

Además, necesitaremos el fichero `playbook.yml`, el cual se encargará del provisionamiento de Ansible: instalar dependencias y clonar nuestro repo. Su contenido es el siguiente:

~~~
- hosts: all
  remote_user: vagrant
  vars_files:
    - var.yml
  gather_facts: no
  become: yes
  become_method: sudo
  tasks:
    - name: Instalar paquetes
      apt: pkg={{ item }} update-cache=yes cache_valid_time=3600
      with_items: "{{ system_packages }}"

    - name: Descargar fuentes
      git: repo={{project_repo}} dest={{proyect_path}} clone=yes force=yes
    - name: Run npm install
      npm: path={{proyect_path}}
~~~

En los ejercicios de los primeros temas, vimos como registrarnos en Azure. Una vez con la cuenta creada, tenemos que instalar el cliente:

![Cliente](img/28.png)

A continuación, hacemos login con el cliente para entrar con nuestra cuenta de Azure. Ésto se hace a través de un código que debemos introducir en la página web que el propio cliente nos proporciona:

![Login](img/29.png)

Entramos en el modo asm para poder descargamos el archivo del pase. Justo después lo importamos:

![Pase](img/30.png)

Una vez hecho esto, debemos crear los certificados de seguridad y darle permisos:

![Certificados](img/31.png)

Cuando lo hemos creado (archivo .cer), lo subimos a Azure a través del panel de administración:

![Certificado](img/32.png)

Y después crear la aplicación en Azure Active Directory:

![Aplicación](img/33.png)

Encontramos la información de la aplicación si hacemos click en ella.
Por último, tenemos que añadir la aplicación como usuario colaborador:

![Añadir aplicación colaborador](img/34.png)


Una vez configurado el portal, lo único que nos queda es modificar el fichero `Vagrantfile`, donde pondremos la configuración de la máquina virtual e instalar la máquina. El contenido de `Vagrantfile` es:
~~~
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacía
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0" #Ip privada
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    config.ssh.private_key_path = '~/.ssh/id_rsa'
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.vm_size = 'Basic_A0'
    azure.location = 'southcentralus'
    azure.tcp_endpoints = '80'
    azure.vm_name = "maquinaagendalearning"
    azure.resource_group_name= "agendaLearning"
    azure.tenant_id = ENV["AZURE_TENANT_ID"]
    azure.client_id = ENV["AZURE_CLIENT_ID"]
    azure.client_secret = ENV["AZURE_CLIENT_SECRET"]
    azure.subscription_id = ENV["AZURE_SUBSCRIPTION_ID"]


    
  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "./playbook.yml"
    ansible.verbose = "-vvvv"

    ansible.host_key_checking = false
  end

end
~~~

Para instalar la máquina ejecutamos `vagrant up --provider=azure`:

![Instalar](img/35.png)

![Instalar](img/36.png)

Necesitamos abrir el puerto 80 de la máquina:

![Abriendo puertos](img/37.png)

Para desplegar la aplicación cómodamente podemos usar Fabric. Así que hacemos varias funciones en el fichero `fabfile.py`. El contenido de éste es el siguiente:

~~~
# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def InstallApp():
    # Descargamos el repositorio
    run('git clone https://github.com/mirismr/proyectoIV17-18.git')

    # Instalamos herramientas
    run('sudo apt-get update')
    run('sudo apt-get -y install python3-setuptools')
    run('sudo apt-get -y install python3-dev')
    run('sudo apt-get -y install build-essential')
    run('sudo apt-get -y install python3-psycopg2')
    run('sudo apt-get -y install libpq-dev')
    run('sudo apt-get -y install python3-pip')

    # Instalamos las dependencias
    run('cd proyectoIV17-18/ && pip3 install -r requirements.txt')

def RemoveApp():
    # Borramos directorio repo
    run('sudo rm -rf ./proyectoIV17-18')

def StartApp():
    # Importamos las variables globales
    with shell_env(TOKEN=os.environ["TOKEN_BOT"]):
        # Iniciamos bot
        run('cd ~/proyectoIV17-18/ && python3 bot.py &')
        # Iniciamos el servicio web
        run('cd ~/proyectoIV17-18/ && sudo -E python3 web.py',pty=False)
~~~



Para comprobar que funciona nos metemos en la url:

![Comprobacion](img/38.png)