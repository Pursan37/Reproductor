from django.contrib import admin
from .models import Cancion

# Register your models here.
@admin.register(Cancion)
class TrackAdmin(admin.ModelAdmin):
	list_display=('id','titulo','album','artista','track_file','player')
	list_filter = ('artista','album')
	search_fields= ('titulo','artista__nombre','album__nombre')