from django.contrib import admin
from .models import Pregunta, Opcion, Persona, Talle, Autoridad


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo')


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
	list_display = ('pregunta', 'titulo', 'votos')


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	pass


@admin.register(Talle)
class TalleAdmin(admin.ModelAdmin):
	pass


@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
	pass
