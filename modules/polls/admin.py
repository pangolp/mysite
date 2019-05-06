from django.contrib import admin
from .models import Pregunta, Opcion


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'fecha')


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
	pass
