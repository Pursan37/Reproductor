from django.urls import path

from . import views

urlpatterns = [
	path('inicio/', views.inicioView, name='album.inicio'),
 	path('registro/', views.registroView, name='album.registro'),
]