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
	hora = CharField()

class alumnos(BaseModel):
	email = CharField(primary_key=True)
	nombre = CharField()
	movil = CharField()
	
class realizadas(BaseModel):
	identificador = ForeignKeyField(clases)
	email_alumno = ForeignKeyField(alumnos)
	fecha = CharField()

	class Meta:
		primary_key = CompositeKey('identificador', 'email_alumno')
