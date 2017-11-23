from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.eventos.forms import EventoForm
from apps.eventos.models import Evento
# Create your views here.

def index(request):
	return render(request, 'eventos/index.html')


def evento_view(request):
	if request.method == 'POST':
		form = EventoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('eventos:index')
	else:
		form = EventoForm()
	return render(request, 'eventos/eventos_form.html' , {'form':form})

def eventos_list(request):
	evento = Evento.objects.all().order_by('id')
	contexto = {'eventos':evento}
	return render(request, 'eventos/eventos_list.html', contexto)

def eventos_edit(request, id_evento):
	evento = Evento.objects.get(id=id_evento)
	if request.method == 'GET':
		form = EventoForm(instance=evento)
	else:
		form = EventoForm(request.POST, instance=evento)
		if form.is_valid():
			form.save()
		return redirect('eventos:evento_listar')
	return render(request, 'eventos/eventos_form.html', {'form':form})

def eventos_delete(request, id_evento):
	evento = Evento.objects.get(id=id_evento)
	if request.method == 'POST':
		evento.delete()
		return redirect('eventos:evento_listar')
	return render(request, 'eventos/eventos_delete.html', {'eventos':evento})


#Views baseadas em classes
class EventoList(ListView):
	model = Evento
	template_name = 'eventos/eventos_list.html'

class EventoCreate(CreateView):
	model = Evento
	form_class = EventoForm
	template_name = 'eventos/eventos_form.html'
	success_url = reverse_lazy('eventos:evento_listar')

class EventoUpdate(UpdateView):
	model = Evento
	form_class = EventoForm
	template_name = 'eventos/eventos_form.html'
	success_url = reverse_lazy('eventos:evento_listar')

class EventoDelete(DeleteView):
	model = Evento
	template_name = 'eventos/eventos_delete.html'
	success_url = reverse_lazy('eventos:evento_listar')