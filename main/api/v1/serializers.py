from rest_framework import serializers
from main.models import Image, Message, File

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'message', 'created', 'updated']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'