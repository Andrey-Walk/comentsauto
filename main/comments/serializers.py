from rest_framework import serializers
from .models import Countrys, Directors, Cars, Comments


class CountrysSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()

    class Meta:
        model = Countrys
        fields = ('country', 'directors')

    def get_directors(self, obj):
        directors = Directors.objects.filter(country=obj)
        return DirectorsSerializer(directors, many=True).data

class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = ('country', 'director')

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('car', 'director', 'datastart', 'dataend')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('avtor', 'avtocar', 'datacreate', 'comment')
