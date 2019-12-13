from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import AlbumSerializer
from Reproductor.structure import Estructura
from django.db.models import Q
from .models import Album



class AlbumViewSet(viewsets.ModelViewSet):
	model = Album
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	paginate_by = 20
	def retrieve(self,request,*args,**kwargs):
		try:
 			instance = self.get_object()
 			serializer = self.get_serializer(instance)
 			respuesta = Estructura.success('', serializer.data)
 			return Response(respuesta)
		except Exception as e:
			respuesta = Estructura.error('No se encontraron registros')
			return Response(respuesta, status=status.HTTP_404_NOT_FOUND)	
	
	def list(self, request, *args, **kwargs):
		try:
			queryset = super(AlbumViewSet, self).get_queryset()
			dato = self.request.query_params.get('dato', None)
			page = self.request.query_params.get('page', None)		
			ID = self.request.query_params.get('id', None)

			qset = (~Q(id = 0))
			if dato:
				qset = qset & (Q(nombre__icontains=dato) | (Q(artista__nombre__icontains=dato)))	
			if ID:
				qset = qset & Q(id=ID)

			queryset = self.model.objects.filter(qset)

			if page:						
				paginacion = self.paginate_queryset(queryset)			
				if paginacion is not None:
					serializer = self.get_serializer(paginacion, many=True)
					respuesta = Estructura.success('', serializer.data)	
					return self.get_paginated_response(respuesta)

			serializer = self.get_serializer(queryset,many=True)
			respuesta=Estructura.success('', serializer.data)

			return Response(respuesta)
		except Exception as e:
			#print (e)
			respuesta=Estructura.error500()
			return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)	

	def create(self, request, *args, **kwargs):
		if request.method == 'POST':
			try:
				serializer = self.serializer_class(data=request.data,context={'request': request})

				if serializer.is_valid():
					serializer.save(artista_id=request.data['artista_id'])
					respuesta=Estructura.success('El album ha sido creado exitosamente.',serializer.data)
					
					return Response(respuesta,status=status.HTTP_201_CREATED)
				else:
					respuesta=Estructura.error(serializer.errors)					
					return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
			except Exception as e:
				print(e)
				respuesta=Estructura.error500()
				return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,*args,**kwargs):
		if request.method == 'PUT':			
			try:
				partial = kwargs.pop('partial', False)
				instance = self.get_object()
				serializer = self.serializer_class(instance, 
					data=request.data, 
					context={'request': request},
					partial=partial)
				
				if serializer.is_valid():
					serializer.save()				
					respuesta=Estructura.success('El album ha sido actualizado exitosamente.',
						serializer.data)
					return Response(respuesta,status=status.HTTP_201_CREATED)
				else:
					respuesta=Estructura.error(serializer.errors)
					return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
			except Exception as e:
				respuesta=Estructura.error500()				
				return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,*args,**kwargs):
		if request.method == 'DELETE':			
			try:
				instance = self.get_object()
				self.perform_destroy(instance)
				serializer = self.get_serializer(instance)
				respuesta=Estructura.success('El album ha sido eliminado exitosamente.',serializer.data)
				return Response(respuesta, status=status.HTTP_202_ACCEPTED)
			except Exception as e:
				respuesta=Estructura.error500()				
				return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

def inicioView(request):
	return render(request,'album/album.html',{'modelo':'album'})
def registroView(request):
	return render(request, 'album/registro.html',{'modelo':'album'})	
# Create your views here.
