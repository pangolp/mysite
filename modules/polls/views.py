from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Pregunta


class IndexView(ListView):
	model = Pregunta
	template_name = 'polls/index.html'
	context_object_name = 'preguntas'


class PreguntaDetail(DetailView):
	model = Pregunta
	template_name = 'polls/detalle.html'
	context_object_name = 'pregunta'
