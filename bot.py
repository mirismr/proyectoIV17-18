# -*- coding: utf-8 -*-
import sqlite3
import requests
import telebot
import os
TOKEN = os.environ["TOKEN_BOT"]

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	bot.send_message(cid, "Introduzca acción que desea realizar. \nAcciones:\n1. /programar: Programar clase \n2. /hoy: clases pendientes para hoy")


@bot.message_handler(commands=['programar'])
def programar_clase(message):
	cid = message.chat.id

	con_bd = sqlite3.connect('base_datos.db')#psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
	#con_bd = psycopg2.connect(database='d6f0n6kc34qjo7',user=(os.environ["USR_BD"]),password=(os.environ["PASS_BD"]),host='ec2-54-225-117-56.compute-1.amazonaws.com')	
	cursor_cid = con_bd.cursor()


	cursor_cid.close()
	con_bd.close()


bot.polling(none_stop=True) # siempre activo