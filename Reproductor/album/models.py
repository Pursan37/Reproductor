from django.db import models
from artista.models import Artista
# Create your models here.
class Album(models.Model):
	nombre = models.CharField(max_length=200)
	artista =  models.ForeignKey(Artista, on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre + ' de ' + self.artista.nombre

	class Meta: 
		db_table = 'album'