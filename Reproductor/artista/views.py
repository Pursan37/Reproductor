from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ArtistaSerializer

from Reproductor.structure import Estructura
from django.db.models import Q

from .models import Artista 

# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet):
	model = Artista
	queryset = Artista.objects.all()
	serializer_class = ArtistaSerializer
	paginate_by = 20

	def retrieve(self,request,*args, **kwargs):
		try:
			instance = self.get_object()
			serializer = self.get_serializer(instance)
			respuesta = Estructura.success('', serializer.data)
			return Response(respuesta)
		except Exception as e:
			# print e
			respuesta = Estructura.error('No se encontraron registros')
			return Response(respuesta, status=status.HTTP_404_NOT_FOUND)

	def list(self, request, *args, **kwargs):
		try:
			queryset = super(ArtistaViewSet, self).get_queryset()
			dato = self.request.query_params.get('dato', None)
			page = self.request.query_params.get('page', None)

			if dato:
				qset = Q(nombre__icontains=dato)
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
					serializer.save()
					respuesta=Estructura.success('El artista ha sido creado exitosamente.',serializer.data)
					
					return Response(respuesta,status=status.HTTP_201_CREATED)
				else:
					respuesta=Estructura.error(serializer.errors)
					
					return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
			except Exception as e:
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
					respuesta=Estructura.success('El artista ha sido actualizado exitosamente.',
						serializer.data)
					return Response(respuesta,status=status.HTTP_201_CREATED)
				else:
					respuesta=Estructura.error(serializer.errors)
					return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)
			except Exception as e:
				respuesta=Estructura.error500()				
				return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,*args,**kwargs):
		#codigo para crer el punto de interrupcion
		#import pdb; pdb.set_trace()
		if request.method == 'DELETE':			
			try:
				instance = self.get_object()
				self.perform_destroy(instance)
				serializer = self.get_serializer(instance)
				respuesta=Estructura.success('El artista ha sido eliminado exitosamente.',serializer.data)
				return Response(respuesta, status=status.HTTP_202_ACCEPTED)
			except Exception as e:
				respuesta=Estructura.error500()				
				return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

def inicioView(request):
	return render(request,'artista/artista.html',{'modelo':'artista'})
def registroView(request):
	return render(request, 'artista/registro.html',{'modelo':'artista'})