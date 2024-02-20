from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageListAPIView.as_view(), name='image_list')
]