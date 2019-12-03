from django.db import models
from artista.models import Artista
from album.models import Album

class Cancion(models.Model):
	titulo = models.CharField(max_length=255)
	track_file = models.FileField(upload_to='Cancion')
	album = models.ForeignKey(Album, on_delete=models.PROTECT)
	artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
	def player(self):
		return """
		<audio controls>
			<source src="%s" type="audio/mpeg">
			Your browser does not support the audio tag.
		</audio>
		""" % self.track_file.url
	player.allow_tags = True
	player.admin_order_field = 'track_file'	
	def __str__(self):
		return self.titulo + ' de ' + self.artista.nombre

	class Meta: 
		db_table = 'cancion'	
# Create your models here.


