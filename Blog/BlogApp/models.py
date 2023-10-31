from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Blog(models.Model):
    
    Blog_name=models.CharField(max_length=250)
    Img=CloudinaryField('images')
    Blog=models.TextField()

    def __str__(self):
        return self.Blog_name

    