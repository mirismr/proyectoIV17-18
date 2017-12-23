# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def InstallApp():
	# Descargamos el repositorio
	run('git clone https://github.com/mirismr/proyectoIV17-18.git')

	# Instalamos pip3
	run('sudo apt-get install -y python3-pip')

	# Instalamos las dependencias
	run('cd proyectoIV17-18/ && pip3 install -r requirements.txt')

def RemoveApp():
	# Borramos directorio repo
	run('sudo rm -rf ./proyectoIV17-18')

def StartApp():
	# Importamos las variables globales
	with shell_env(TOKEN=os.environ["TOKEN_BOT"]):
		# Iniciamos el servicio web
		run('cd ~/proyectoIV17-18/ && sudo -E python3 web.py',pty=False)