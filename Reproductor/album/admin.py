from django.contrib import admin

from .models import Album

# Register your models here.
@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
	list_display=('id','nombre','artista',)
	search_fields= ('nombre','id',)
	list_filter= ('artista',)

