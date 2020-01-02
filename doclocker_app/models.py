from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

"""class Images(models.Model):

    post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)"""

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


    """description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)"""

    def __str__(self):
        return self.username





