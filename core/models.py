# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.utils.text import slugify


class Folder(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    folder_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Folder, self).save(*args, **kwargs)


class File(models.Model):
    file_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    file = models.FileField(upload_to='files/')
    decrypted = models.BooleanField(default=False)
    decryption_key = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(File, self).save(*args, **kwargs)
