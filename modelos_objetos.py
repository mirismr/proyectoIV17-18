class Alumno:
	def __init__(self, e, n, m):
		self.email = e
		self.nombre = n
		self.movil = m

	def __eq__(self, other): 
		return self.email == other.email and self.nombre == other.nombre and self.movil == other.movil


class Clase:
	def __init__(self, n, a, m, i, h):
		self.sitio = n
		self.precio = a
		self.materia = m
		self.pagada = i
		self.hora = h
		
	def __eq__(self, other): 
		return self.sitio == other.sitio and self.precio == other.precio and self.materia == other.materia and self.pagada == other.pagada and self.hora == other.hora


