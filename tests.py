import funcionalidades_bd
import unittest
import sqlite3

class Test(unittest.TestCase):
	def test_bd(self):
		conexion = sqlite3.connect('base_datos.db')
		cursor = conexion.cursor()
		cursor.execute("DELETE FROM alumnos WHERE email = 'prueba@gmail.com'")
		cursor.execute("INSERT INTO alumnos VALUES('prueba@gmail.com', 'prueba', 'pruebap1', '+34123456778', 'informacion prueba')")
		conexion.commit()
		ultima_fila = cursor.lastrowid
		cursor.execute("DELETE FROM alumnos WHERE email = 'prueba@gmail.com'")
		self.assertEqual(ultima_fila,ultima_fila, "Conexion existosa")

	def test_obtener_alumno(self):
		conexion = sqlite3.connect('base_datos.db')
		cursor = conexion.cursor()
		cursor.execute("DELETE FROM alumnos WHERE email = 'prueba1@gmail.com'")
		cursor.execute("INSERT INTO alumnos VALUES('prueba1@gmail.com', 'prueba1', 'prueba1p1', '+34123456778', 'informacion prueba1')")
		conexion.commit()
		alumno_obtenido = funcionalidades_bd.obtener_alumno("prueba1@gmail.com")
		
		self.assertEqual("('prueba1@gmail.com', 'prueba1', 'prueba1p1', '+34123456778', 'informacion prueba1')", alumno_obtenido, "Obtener perfil alumno")
		cursor.execute("DELETE FROM alumnos WHERE email = 'prueba1@gmail.com'")
		
	def test_insertar_clase_programada(self):
		conexion = sqlite3.connect('base_datos.db')
		cursor = conexion.cursor()
		conexion.execute("PRAGMA foreign_keys = ON")
		cursor.execute("DELETE FROM realizadas WHERE clase_id='99' AND email_alumno='prueba2@gmail.com'")
		cursor.execute("DELETE FROM clases WHERE identificador='99'")
		cursor.execute("DELETE FROM alumnos WHERE email='prueba2@gmail.com'")
		clase1 = ("99", "online", "10.5", "informatica", "0")
		cursor.execute("INSERT INTO clases VALUES(?, ?, ?, ?, ?)", clase1)
		cursor.execute("INSERT INTO alumnos VALUES('prueba2@gmail.com', 'prueba2', 'prueba2p1', '+34123456778', 'informacion prueba2')")
		detalles = ("23/07/1996", "99", "prueba2@gmail.com", "14:20")
		cursor.execute("INSERT INTO realizadas VALUES(?, ?, ?, ?)", detalles)
		
		
		cursor.execute("DELETE FROM realizadas WHERE clase_id='99' AND email_alumno='prueba2@gmail.com'")
		conexion.commit()

		funcionalidades_bd.programar_clase(detalles)
		clase_funcion = cursor.execute("SELECT * FROM realizadas WHERE clase_id='99' AND email_alumno='prueba2@gmail.com'")
		
		cursor.execute("DELETE FROM realizadas WHERE clase_id='99' AND email_alumno='prueba2@gmail.com'")
		clase_manual = cursor.execute("SELECT * FROM realizadas WHERE clase_id='99' AND email_alumno='prueba2@gmail.com'")
		
		self.assertEqual(clase_manual, clase_funcion, "Obtener clase programada")
		


if __name__ == '__main__':
	unittest.main()