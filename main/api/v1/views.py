from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from main.models import *

class ImageListAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many =True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ImageSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ImageDetailAPIView(APIView):
    def get(self, request, id):
        image = Image.objects.get(id = id)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    def put(self, request, id):
        image = Image.objects.get(id = id)
        serializer = ImageSerializer(data=request.POST, instance=image)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageAPIView(APIView):
    def get(self, request):
        texts = Message.objects.all()
        serializer = MessageSerializer(texts, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FileAPIView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = MessageSerializer(files, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)