from django import forms
from apps.eventos.models import Evento

class EventoForm(forms.ModelForm):

	class Meta:
		model = Evento
		fields = [
			'titulo',
			'lista_de_organizadores',
			'lista_de_promotores',
			'data_inicio',
			'data_fim',
			'horario_inicio',
			'horario_fim',
			'lista_de_patrocinadores',
		]
		labels = {
			'titulo': 'Título do Evento',
			'lista_de_organizadores': 'Lista de Organizadores',
			'lista_de_promotores': 'Lista de Promotores',
			'data_inicio': 'Data de ínicio do evento',
			'data_fim': 'Data de término do evento',
			'horario_inicio': 'Horário de início do evento',
			'horario_fim': 'Horário de término do evento',
			'lista_de_patrocinadores': 'Lista de Patrocinadores',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'lista_de_organizadores': forms.Textarea(attrs={'class':'form-control'}),
			'lista_de_promotores': forms.Textarea(attrs={'class':'form-control'}),
			'data_inicio': forms.TextInput(attrs={'class':'form-control'}),
			'data_fim': forms.TextInput(attrs={'class':'form-control'}),
			'horario_inicio': forms.TextInput(attrs={'class':'form-control'}),
			'horario_fim': forms.TextInput(attrs={'class':'form-control'}),
			'lista_de_patrocinadores': forms.Textarea(attrs={'class':'form-control'}),
		}

			