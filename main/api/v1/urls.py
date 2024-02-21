from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('image/', views.ImageListAPIView.as_view(), name='image_list'),
    path('<uuid:id>/', views.ImageDetailAPIView.as_view(), name='detail'),
    path('message/', views.MessageAPIView.as_view(), name='message'),
    path('file/', views.FileAPIView.as_view(), name='file'),
]