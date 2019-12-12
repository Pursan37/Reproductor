from django.urls import path

from . import views

urlpatterns = [
	path('inicio/', views.inicioView, name='artista.inicio'),
	path('registro/', views.registroView, name='artista.registro'),
]