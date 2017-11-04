# -*- coding: utf-8 -*-
import sqlite3
import requests
import telebot
import os
import funcionalidades_bd as bd

TOKEN = os.environ["TOKEN_BOT"]

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")


@bot.message_handler(commands=['programar'])
def programar_clase(message):
	cid = message.chat.id

	clase = objetos.Clase("online", 10.5, "mates", False)
	bd.insertar_clase(clase)
	bot.send_message(cid, "La clase se insertó correctamente. \n\nIntroduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")

@bot.message_handler(commands=['hoy'])
def programar_clase(message):
	cid = message.chat.id

	clases_obtenidas = bd.obtener_clases()
	for a in clases_obtenidas:
		bot.send_message(cid, "Sitio: ", a.sitio)
		bot.send_message(cid, "Precio: ", a.precio)
		bot.send_message(cid, "Materia: ", a.materia)
		bot.send_message(cid, "Pagada: ", a.pagada)
	
	bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")


bot.polling(none_stop=True) # siempre activo