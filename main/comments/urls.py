from django.urls import path, include
from . import views
from comments.views import DirectorsModelViewSet, CountrysModelViewSet, CarsModelViewSet, CommentsModelViewSet, CountrysAPIView, DirectorsAPIView, CarsAPIView, CommentsAPIView, AllAPIView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'countrys', CountrysModelViewSet)
router.register(r'directors', DirectorsModelViewSet)
router.register(r'cars', CarsModelViewSet)
router.register(r'comments', CommentsModelViewSet)

urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    path('api/export/countrys', CountrysAPIView.as_view(), name='countrys_xlsx'),
    path('api/export/countrys', CountrysAPIView.as_view(), name='countrys_csv'),
    path('api/export/directors', DirectorsAPIView.as_view(), name='directors_xlsx'),
    path('api/export/directors', DirectorsAPIView.as_view(), name='directors_csv'),
    path('api/export/cars', CarsAPIView.as_view(), name='cars_xlsx'),
    path('api/export/cars', CarsAPIView.as_view(), name='cars_csv'),
    path('api/export/comments', CommentsAPIView.as_view(), name='comments_xlsx'),
    path('api/export/comments', CommentsAPIView.as_view(), name='comments_csv'),
    path('api/export/all', AllAPIView.as_view(), name='all_xlsx'),
    path('api/export/all', AllAPIView.as_view(), name='all_csv')
]

