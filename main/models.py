from django.db import models
import uuid

class Image(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class Message(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class File(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    file = models.FileField(upload_to='files')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)