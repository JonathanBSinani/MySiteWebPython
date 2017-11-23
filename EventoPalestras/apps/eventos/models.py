from django.db import models

# Create your models here.

class Evento(models.Model):
	titulo = models.CharField(max_length=50)
	lista_de_organizadores = models.TextField()
	lista_de_promotores = models.TextField()
	data_inicio = models.DateField()
	data_fim = models.DateField()
	horario_inicio = models.TimeField()
	horario_fim = models.TimeField()
	lista_de_patrocinadores = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.titulo, self.titulo)
