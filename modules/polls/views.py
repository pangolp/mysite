from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Pregunta


class IndexView(LoginRequiredMixin, ListView):
	model = Pregunta
	template_name = 'pregunta/index.html'
	context_object_name = 'preguntas'


class PreguntaDetail(LoginRequiredMixin, DetailView):
	model = Pregunta
	template_name = 'pregunta/detalle.html'
	context_object_name = 'pregunta'


# Sirve para crear un formulario y dar de alta una Pregunta fuera del admin
class PreguntaCreate(LoginRequiredMixin, CreateView):
	model = Pregunta
	fields = ['titulo']
	template_name = 'pregunta/create.html'
	success_url = reverse_lazy('polls:index')


class PreguntaUpdate(LoginRequiredMixin, UpdateView):
	model = Pregunta
	fields = ['titulo']
	template_name = 'pregunta/update.html'
	success_url = reverse_lazy('polls:index')


class PreguntaDelete(LoginRequiredMixin, DeleteView):
	model = Pregunta
	template_name = 'pregunta/delete.html'
	success_url = reverse_lazy('polls:index')
