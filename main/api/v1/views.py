from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from main.models import *

class ImageListAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many =True)
        return Response(serializer.data)