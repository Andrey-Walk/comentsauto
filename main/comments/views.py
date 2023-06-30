from django.shortcuts import render
from rest_framework import viewsets
from .models import Countrys, Directors, Cars, Comments
from .serializers import DirectorsSerializer, CountrysSerializer, CarsSerializer, CommentsSerializer


def index(request):
    news = Cars.objects.all()
    return render(request, 'main/index.html', {'main': news})

class DirectorsModelViewSet(viewsets.ModelViewSet):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer

class CountrysModelViewSet(viewsets.ModelViewSet):
    queryset = Countrys.objects
    serializer_class = CountrysSerializer

class CarsModelViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects
    serializer_class = CarsSerializer

class CommentsModelViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects
    serializer_class = CommentsSerializer
