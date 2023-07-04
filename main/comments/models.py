from django.db import models


class Countrys(models.Model):
    country = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Directors(models.Model):
    director = models.CharField('Имя', max_length=50)
    country = models.ForeignKey(Countrys, on_delete=models.CASCADE)

    def __str__(self):
        return self.director

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Cars(models.Model):
    car = models.CharField('Имя', max_length=50)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    datastart = models.DateField('Год начала выпуска', max_length=10)
    dataend = models.DateField('Год окончания выпуска', max_length=10)

    def __str__(self):
        return self.car

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Comments(models.Model):
    avtor = models.CharField('Email автора', max_length=50)
    avtocar = models.ForeignKey(Cars, on_delete=models.CASCADE)
    datacreate = models.DateTimeField('Дата создания', auto_now_add=True)
    comment = models.TextField('Комментарий', max_length=400)

    def __str__(self):
        return self.avtor

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
