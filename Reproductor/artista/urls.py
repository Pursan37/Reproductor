from django.urls import path

from . import views
urlpatterns = [
	path('inicio/', views.inicioView, name='artista.inicio'),
	path('edicion/<int:id>', views.edicionView, name='artista.edicion'),
	path('registro/', views.registroView, name='artista.registro'),
]