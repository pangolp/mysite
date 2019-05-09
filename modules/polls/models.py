from django.db import models


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