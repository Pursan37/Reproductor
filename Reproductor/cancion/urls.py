from django.urls import path

from . import views

urlpatterns = [
	path('inicio/', views.inicioView, name='cancion.inicio'),
	path('registro/', views.registroView, name='cancion.registro'),
]