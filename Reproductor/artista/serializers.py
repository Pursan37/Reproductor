from rest_framework import serializers
from .models import Artista

class ArtistaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artista
		fields = ('id', 'nombre', )

class ArtistaLiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artista
		fields = ('nombre', )