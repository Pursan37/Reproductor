from django.contrib import admin
from .models import Cancion

# Register your models here.
@admin.register(Cancion)
class TrackAdmin(admin.ModelAdmin):
	list_display=('id','titulo','album','track_file','player')
	list_filter = ('album',)
	search_fields= ('titulo','album__nombre',)