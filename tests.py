import funcionalidades_bd, modelos_bd
import modelos_objetos as objeto
import unittest
from datetime import date
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
		alumno = objeto.Alumno('prueba1@gmail.com', 'prueba1', 'prueba1p1', '+34123456778', 'informacion prueba1')
		
		self.assertEqual(alumno, alumno_obtenido, "Obtener perfil alumno")
		cursor.execute("DELETE FROM alumnos WHERE email = 'prueba1@gmail.com'")
		
	def test_insertar_clase(self):
		
		alumno = objeto.Alumno("prueba@email.com", "nombre", "apellidos", "movil", "informacion")
		clase = objeto.Clase("online", 10.5, "prueba", False)
		
		funcionalidades_bd.insertar_clase(clase)
		funcionalidades_bd.insertar_alumno(alumno)

		funcionalidades_bd.programar_clase(clase, alumno, date(1991,3,21))

		clase_funcion = funcionalidades_bd.obtener_clase_programada(date(1991,3,21))

		id_ultima = modelos_bd.clases.select().order_by(modelos_bd.clases.id.desc()).get()

		borrar = modelos_bd.realizadas.get(modelos_bd.realizadas.identificador == id_ultima.id)
		borrar.delete_instance()

		borrar = modelos_bd.clases.get(modelos_bd.clases.id == id_ultima.id)
		borrar.delete_instance()

		borrar = modelos_bd.alumnos.get(modelos_bd.alumnos.email == "prueba@email.com")
		borrar.delete_instance()

		self.assertEqual(clase, clase_funcion, "Insertar clase programada")
		


if __name__ == '__main__':
	unittest.main()