from django.db import models

from apps.eventos.models import Evento
# Create your models here.

class Palestra(models.Model):
	titulo = models.CharField(max_length=50)
	nome_palestrante = models.CharField(max_length=50)
	descricao_palestra = models.TextField()
	data_da_palestra = models.DateField()
	horario_inicio = models.TimeField()
	horario_termino = models.TimeField()
	link_apresentacao = models.URLField()
	evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)

	"""docstring for ClassName"""
	'''def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg'''
		