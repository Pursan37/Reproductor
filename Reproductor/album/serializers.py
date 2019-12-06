from rest_framework import serializers
from .models import Album

from artista.serializers import ArtistaSerializer
from artista.models import Artista

class AlbumSerializer(serializers.ModelSerializer):
	artista = ArtistaSerializer(read_only = True , allow_null = False)
	artista_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Artista.objects.all() , allow_null = False)
	class Meta:
		model = Album
		fields = ('id', 'nombre', 'artista','artista_id')
 
class AlbumLiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = ('nombre', 'artista',)