from rest_framework import serializers
from .models import Countrys, Directors, Cars, Comments


class DirectorsSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.country')
    car = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Directors
        fields = ('director', 'country', 'car', 'comments_count')

    def get_car(self, obj):
        car = Cars.objects.filter(director = obj)
        return CarsSerializer(car, many = True).data

    def get_comments_count(self, obj):
        comments_count = Comments.objects.filter(avtocar__director = obj).count()
        return comments_count

class CountrysSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Countrys
        fields = ('country', 'director')

    def get_director(self, obj):
        director = Directors.objects.filter(country=obj)
        return DirectorsSerializer(director, many = True).data

class CommentsSerializer(serializers.ModelSerializer):
    avtocar = serializers.CharField(source = 'avtocar.car')

    class Meta:
        model = Comments
        fields = ('avtor', 'avtocar', 'datacreate', 'comment')

    def validate(self, data):
        if len(data['comment']) < 1:
            raise serializers.ValidationError("Длина комментария должна быть не менее 1 символа.")
        return data

class CarsSerializer(serializers.ModelSerializer):
    director = serializers.CharField(source='director.director')
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = ('car', 'director', 'datastart', 'dataend', 'comments', 'comments_count')

    def get_comments_count(self, obj):
        comments_count = Comments.objects.filter(avtocar = obj).count()
        return comments_count

    def get_comments(self, obj):
        comments = Comments.objects.filter(avtocar = obj)
        return CommentsSerializer(comments, many = True).data
