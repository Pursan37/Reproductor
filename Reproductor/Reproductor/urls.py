"""Reproductor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# APIS
admin.autodiscover()
router = routers.DefaultRouter()

#invocacion del recurso Artista
from artista.views import ArtistaViewSet
router.register(r'artista', ArtistaViewSet)
from album.views import AlbumViewSet
router.register(r'album', AlbumViewSet)
from cancion.views import CancionViewSet
router.register(r'cancion', CancionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('artista/', include('artista.urls')),
    path('album/', include('album.urls')),
    path('cancion/', include('cancion.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

