from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Add(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
   