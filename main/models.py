from django.db import models
import uuid
from django.contrib.auth.models import User

class Image(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    image = models.ImageField(upload_to='images')
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class Message(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class File(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    description = models.TextField(null = True, blank = True)
    file = models.FileField(upload_to='files')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class DeviceLocation(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    extra = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)