import sqlite3
import modelos_bd as modelo
import modelos_objetos as objetos
from datetime import date

def create_tables():
	modelo.db.connect()
	modelo.db.create_tables([modelo.clases, modelo.alumnos, modelo.realizadas], True)

def conectar():
	modelo.db.connect()

def insertar_alumno(alumno):
	"""
	Funcion para insertar un alumno en la base de datos.
	"""
	modelo.alumnos.insert(email=alumno.email, nombre=alumno.nombre, apellidos=alumno.apellidos, movil=alumno.movil, informacion=alumno.informacion).execute()

def obtener_alumno(email_alumno):
	"""
	Funcion para obtener un alumno de la base de datos a partir de su email.
	"""
	resultado = modelo.alumnos.get(modelo.alumnos.email == email_alumno)

	return resultado

def insertar_clase(clase):
	"""
	Funcion para insertar una clase en la base de datos.
	"""
	modelo.clases.insert(sitio=clase.sitio, precio=clase.precio, materia=clase.materia, pagada=clase.pagada).execute()


def programar_clase(clase, alumno, fecha_pas):
	"""
	Funcion para registrar una futura clase en la base de datos.
	"""
	id_ultima = modelo.clases.select().order_by(modelo.clases.id.desc()).get()

	modelo.realizadas.insert(identificador=id_ultima.id,fecha=fecha_pas, email_alumno=alumno.email).execute()


def obtener_clase_programada(fecha):
	"""
	Funcion para, dada una fecha, obtener las clases para dicha fecha.
	"""
	resultado=modelo.realizadas.get(modelo.realizadas.fecha == fecha)

	clase = modelo.clases.get(modelo.clases.id == resultado.identificador.id)

	return clase

''' Obtiene todas las clases de la bd'''
def obtener_clases():
	clases_obtenidas = modelo.clases.select()

	return clases_obtenidas

#if __name__ == '__main__':
	
#	create_tables()
	#alumno = objetos.Alumno("email2@email.com", "nombre", "apellidos", "movil", "informacion")
	#insertar_alumno(alumno)
	

	#alumno = obtener_alumno("email2@email.com")
	#print(alumno.nombre)

	#clase = objetos.Clase("online", 10.5, "mates", False)
	#insertar_clase(clase)

	#programar_clase(clase, alumno, date(1996,3,21))
	#clase = obtener_clase_programada(date(1996,3,21))

	
	#clases_obtenidas = modelo.realizadas.select()
	#for a in clases_obtenidas:
	#	print(a.fecha)
	#	print(a.email_alumno.email)
	#	print(a.identificador.id)


