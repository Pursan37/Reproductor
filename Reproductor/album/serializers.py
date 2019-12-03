from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = ('id', 'nombre', 'artista',)
 
class AlbumLiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = ('nombre', 'artista',)