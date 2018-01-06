# -*- coding: utf-8 -*-
import sqlite3
import requests
import telebot
import os
import funcionalidades_bd as bd
import modelos_objetos as objetos
from datetime import date
import time

TOKEN = os.environ["TOKEN_BOT"]

bot = telebot.TeleBot(TOKEN)

bd.create_tables()

lugar = ''
precio = 0.0
materia = ''
hora = ''

nombre = ''
email = ''
movil = ''

dia = 1
mes = 1


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")


@bot.message_handler(commands=['programar'])
def programar_clase(message):
	cid = message.chat.id

	msg = bot.reply_to(message, 'Introduzca el lugar de la clase')
	bot.register_next_step_handler(msg, process_lugar_step)

def process_lugar_step(message):
	try:
		chat_id = message.chat.id
		global lugar
		lugar = message.text
		#user = User(name)
		#user_dict[chat_id] = user
		msg = bot.reply_to(message, 'Introduzca el precio: ')
		bot.register_next_step_handler(msg, process_precio_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_precio_step(message):
	try:
		chat_id = message.chat.id
		global precio
		precio = float(message.text)
		#user = User(name)
		#user_dict[chat_id] = user
		msg = bot.reply_to(message, 'Introduzca la materia: ')
		bot.register_next_step_handler(msg, process_materia_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_materia_step(message):
	try:
		chat_id = message.chat.id
		global materia
		materia = message.text
		#user = User(name)
		#user_dict[chat_id] = user
		msg = bot.reply_to(message, 'Introduzca la hora: ')
		bot.register_next_step_handler(msg, process_hora_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')


def process_hora_step(message):
	try:
		chat_id = message.chat.id
		global hora
		hora = message.text
		
		msg = bot.reply_to(message, 'Clase registrada. Introduzca los datos del alumno. Nombre: ')
		bot.register_next_step_handler(msg, process_nombre_step)
		
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_nombre_step(message):
	try:
		chat_id = message.chat.id
		global nombre
		nombre = message.text
		
		msg = bot.reply_to(message, 'Introduzca el email: ')
		bot.register_next_step_handler(msg, process_email_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_email_step(message):
	try:
		chat_id = message.chat.id
		global email
		email = message.text
		
		msg = bot.reply_to(message, 'Introduzca el movil: ')
		bot.register_next_step_handler(msg, process_movil_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_movil_step(message):
	try:
		chat_id = message.chat.id
		global movil
		movil = message.text

		msg = bot.reply_to(message, 'Introduzca el dia: ')
		bot.register_next_step_handler(msg, process_dia_step)		
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_dia_step(message):
	try:
		chat_id = message.chat.id
		global dia
		dia = int(message.text)

		msg = bot.reply_to(message, 'Introduzca el mes: ')
		bot.register_next_step_handler(msg, process_mes_step)		

	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_mes_step(message):
	try:
		chat_id = message.chat.id
		global mes
		mes = int(message.text)

		clase = objetos.Clase(lugar, precio, materia, hora)
		bd.insertar_clase(clase)

		alumno = objetos.Alumno(email, nombre, movil)
		
		bd.insertar_alumno(alumno)

		fecha = date(2018, mes, dia)
		bd.programar_clase(clase, alumno, fecha)

		bot.send_message(chat_id, 'Alumno insertado y clase programada.\n Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy')
	except Exception as e:
		bot.reply_to(message, 'oooops')


		
@bot.message_handler(commands=['todas'])
def obtener_todas(message):
	cid = message.chat.id

	clases_obtenidas = bd.obtener_clases()

	for a in clases_obtenidas:
		bot.send_message(cid, "Sitio: "+a.sitio)
		bot.send_message(cid, "Precio: "+str(a.precio))
		bot.send_message(cid, "Materia: "+a.materia)
		bot.send_message(cid, "Hora: "+a.hora)
	
	bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")

@bot.message_handler(commands=['hoy'])
def obtenr_clases_hoy(message):
	cid = message.chat.id

	mes = int(time.strftime("%m"))
	dia = int(time.strftime("%d"))

	try:
		clases_obtenidas = bd.obtener_clases_programadas(date(2018, mes, dia))

		for a in clases_obtenidas:
			bot.send_message(cid, "Clase:")
			bot.send_message(cid, "Sitio: "+a.sitio)
			bot.send_message(cid, "Precio: "+str(a.precio))
			bot.send_message(cid, "Materia: "+a.materia)
			bot.send_message(cid, "Hora: "+a.hora)
	except Exception as e:
		bot.send_message(cid, "No hay clases para hoy")
	finally:	
		bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")


bot.polling(none_stop=True) # siempre activo