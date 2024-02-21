from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.ImageListAPIView.as_view(), name='image_list'),
    path('<uuid:id>/', views.ImageDetailAPIView.as_view(), name='detail')
]