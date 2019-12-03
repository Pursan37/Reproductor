from django.contrib import admin
from .models import Artista

# Register your models here.
@admin.register(Artista)
class AdminArtista(admin.ModelAdmin):
	list_display=('id','nombre',)
	search_fields= ('nombre','id',)
