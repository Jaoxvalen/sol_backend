from django.shortcuts import render
from rest_framework import viewsets, generics, filters

from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):

    search_fields = ['name']
    filter_backends = (filters.SearchFilter, )

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
