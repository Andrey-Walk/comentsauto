from rest_framework import serializers
from .models import Countrys, Directors, Cars, Comments


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = ('country', 'director')

class CountrysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countrys
        fields = ('country',)

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('car', 'director', 'datastart', 'dataend')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('avtor', 'avtocar', 'datacreate', 'comment')
