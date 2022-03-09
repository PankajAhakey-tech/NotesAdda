from audioop import reverse
from unicodedata import category
from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator

class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def  get_absolute_url(self): 
        
        return reverse('home')

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=256)
    branch = models.CharField(max_length=256,default="general")
    notes=models.FileField(upload_to="media",validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])
    description = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.subject}'

    def  get_absolute_url(self): 
        
        return reverse('home')
    