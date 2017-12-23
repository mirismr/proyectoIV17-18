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
		run('python3 bot.py &')
		# Iniciamos el servicio web
		run('cd ~/proyectoIV17-18/ && sudo -E python3 web.py &',pty=False)
