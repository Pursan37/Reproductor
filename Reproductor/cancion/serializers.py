from rest_framework import serializers
from .models import Cancion


class CancionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cancion
		fields = ('id', 'titulo', 'track_file', 'album', 'artista',)

class CancionLiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cancion
		fields = ('id', 'titulo', 'track_file', )

	