from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    content=models.TextField()
    img=models.ImageField(upload_to='pics')
    timestamp=models.DateTimeField(blank=True)
    slug=models.CharField(max_length=50)