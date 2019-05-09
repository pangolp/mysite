from django.db import models


LISTA_CAMISAS = (
	('S', 'Pequeña'),
	('M', 'Mediano'),
	('L', 'Largo'),
	('XL', 'Extra largo'),
)

# Creamos la tabla pregunta
class Pregunta(models.Model):
	titulo = models.CharField(max_length=200, help_text='Queremos que guardes el titulo de la pregunta')
	creacion = models.DateTimeField(auto_now_add=True)
	modificacion = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'pregunta'
		verbose_name_plural = 'preguntas'
		# Esto ordena las preguntas por fecha donde trae las ultimas primero.
		ordering = ['-creacion']

	def __str__(self):
		return '%s' % (self.titulo)


class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200, help_text='Queremos que guardes el titulo de la opcion')
	votos = models.IntegerField(help_text='Votos de la opcion')

	class Meta:
		verbose_name = 'opcion'
		verbose_name_plural = 'opciones'
		ordering = ['votos']

	def __str__(self):
		return '%s' % (self.titulo)


class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	talle = models.CharField(max_length=1, choices=LISTA_CAMISAS)

	class Meta:
		db_table = 'personas'


class Talle(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return '%s' % (self.nombre)


class Autoridad(models.Model):
	nombre = models.CharField(max_length=50)
	talle = models.ForeignKey(Talle, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name_plural = 'autoridades'
