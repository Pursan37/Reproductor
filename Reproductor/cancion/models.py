from django.db import models
from artista.models import Artista
from album.models import Album
from django.utils.safestring import mark_safe

class Cancion(models.Model):
	titulo = models.CharField(max_length=255)
	track_file = models.FileField(upload_to='Cancion')
	album = models.ForeignKey(Album, on_delete=models.PROTECT)
	
	def player(self):
		mystr = '<audio controls><source src="%s" type="audio/mpeg"></audio>'% self.track_file.url
		mystr = mark_safe(mystr)
		return mystr
	player.allow_tags = True
	player.admin_order_field = 'track_file'	
	def __str__(self):
		return self.titulo + ' de ' + self.album.nombre

	class Meta: 
		db_table = 'cancion'	
# Create your models here.


#<audio src="song.mp3">Audio tag not supported</audio>