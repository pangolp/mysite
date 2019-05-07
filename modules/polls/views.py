from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Pregunta


class IndexView(ListView):
	model = Pregunta
	template_name = 'polls/index.html'
	context_object_name = 'preguntas'


class PreguntaDetail(DetailView):
	model = Pregunta
	template_name = 'polls/detalle.html'
	context_object_name = 'pregunta'


# Sirve para crear un formulario y dar de alta una Pregunta fuera del admin
class PreguntaCreate(CreateView):
	model = Pregunta
	fields = ['titulo']
	template_name = 'polls/pregunta/create.html'
	success_url = reverse_lazy('polls:index')
