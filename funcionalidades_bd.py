import sqlite3

def insertar_alumno(alumno):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	#claves externas
	conexion.execute("PRAGMA foreign_keys = ON")
	try:
		cursor.execute("INSERT INTO alumnos VALUES(?, ?, ?, ?, ?)", alumno)
		conexion.commit()
	except sqlite3.IntegrityError as e:
		print('Error de integridad en la base de datos')

def obtener_alumno(email_alumno):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	resultado=''
	#comprobar que email_alumno existe
	cursor.execute('SELECT * FROM alumnos WHERE email=?', [email_alumno])

	for registro in cursor:
		resultado+=str(registro)

	return str(resultado)

def insertar_clase(clase):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	#claves externas
	conexion.execute("PRAGMA foreign_keys = ON")
	try:
		cursor.execute("INSERT INTO clases VALUES(?, ?, ?, ?, ?)", clase)
		conexion.commit()
	except sqlite3.IntegrityError as e:
		print('Error de integridad en la base de datos')

def obtener_clase(identificador):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	resultado=''
	#comprobar que identificador existe
	cursor.execute('SELECT * FROM clases WHERE identificador=?', [identificador])

	for registro in cursor:
		resultado+=str(registro)

	return str(resultado)

def programar_clase(detalles):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	#claves externas
	conexion.execute("PRAGMA foreign_keys = ON")
	try:
		cursor.execute("INSERT INTO realizadas VALUES(?, ?, ?, ?)", detalles)
		conexion.commit()
	except sqlite3.IntegrityError as e:
		print(str(e))
		print('Error de integridad en la base de datos')

def obtener_clase_programada(fecha):
	conexion = sqlite3.connect('base_datos.db')
	cursor = conexion.cursor()
	resultado=''
	#comprobar que fecha existe
	cursor.execute('SELECT * FROM realizadas WHERE fecha=?', [fecha])

	for registro in cursor:
		resultado+=str(registro)

	return str(resultado)


if __name__ == '__main__':
	#alumno3 = ("alumno3@gmail.com", "alumno3", "alumno3ap1 alumno3ap2", "+34123456788", "informacion alumno3")
	#insertar_alumno(alumno3);
	#alumno_consulta = obtener_alumno("alumno@gmail.com")
	#print(str(alumno_consulta))

	#clase1 = ("1", "online", "10.5", "informatica", "0")
	#insertar_clase(clase1);
	#consulta = obtener_clase(1)
	#print(str(consulta))

	#detalles = ("23/07/1996", "1", "alumno1@gmail.com", "14:20")
	#programar_clase(detalles)

	clase = obtener_clase_programada("23/07/1996")
	print(str(clase))


