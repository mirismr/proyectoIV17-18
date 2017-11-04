class Alumno:
	def __init__(self, e, n, a, m, i):
		self.email = e
		self.nombre = n
		self.apellidos = a
		self.movil = m
		self.informacion = i

	def __eq__(self, other): 
		return self.email == other.email and self.nombre == other.nombre and self.apellidos == other.apellidos and self.movil == other.movil and self.informacion == other.informacion


class Clase:
	def __init__(self, n, a, m, i):
		self.sitio = n
		self.precio = a
		self.materia = m
		self.pagada = i
		
	def __eq__(self, other): 
		return self.sitio == other.sitio and self.precio == other.precio and self.materia == other.materia and self.pagada == other.pagada


