from django.urls import path, include
from . import views
from comments.views import DirectorsModelViewSet, CountrysModelViewSet, CarsModelViewSet, CommentsModelViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'countrys', CountrysModelViewSet)
router.register(r'directors', DirectorsModelViewSet)
router.register(r'cars', CarsModelViewSet)
router.register(r'comments', CommentsModelViewSet)

urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls))
]
