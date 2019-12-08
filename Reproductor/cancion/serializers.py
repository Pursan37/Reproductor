from rest_framework import serializers
from .models import Cancion
from album.serializers import AlbumSerializer
from album.models import Album

class CancionSerializer(serializers.ModelSerializer):
	album = AlbumSerializer(read_only = True , allow_null = False)
	album_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Album.objects.all() , allow_null = False)

	class Meta:
		model = Cancion
		fields = ('id', 'titulo', 'track_file', 'player', 'album', 'album_id')

class CancionLiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cancion
		fields = ('id', 'titulo', 'player', )

	