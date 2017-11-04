from peewee import *

db = SqliteDatabase('base_datos.db')

class BaseModel(Model):
	class Meta:
		database = db

class clases(BaseModel):
	id = PrimaryKeyField()
	sitio = CharField()
	precio = FloatField()
	materia = CharField()
	pagada = BooleanField()

class alumnos(BaseModel):
	email = CharField(primary_key=True)
	nombre = CharField()
	apellidos = CharField()
	movil = CharField()
	informacion = CharField()
	
class realizadas(BaseModel):
	identificador = ForeignKeyField(clases)
	email_alumno = ForeignKeyField(alumnos)
	fecha = DateField()

	class Meta:
		primary_key = CompositeKey('identificador', 'email_alumno')

#if __name__ == '__main__':
#	db.connect()

	#alumno = alumnos(email='bob@gmail.com', nombre='Bob', apellidos='apellidos', movil='12323233', informacion='dsasdasdsad')
	#filas = alumno.save()
	#print(filas)
	
	#alumnos_obtenidos = clases.select()
	#for a in alumnos_obtenidos:
	#	print(a.materia)
