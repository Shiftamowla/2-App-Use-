from django.db import models
from django.utils import timezone
from myapp.models import *

class NewsModel(models.Model):
    CATEGORY=[
        ('politics','Politics'),
        ('sports','Sports'),
        ('intertainment','Intertainment'),

    ]
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE,null=True)
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    Title=models.CharField(max_length=100,null=True)
    Content=models.CharField(max_length=100,null=True)
    Author=models.CharField(max_length=100,null=True)
    Date=models.DateField(default=timezone.now,null=True)
    Categories=models.CharField(choices=CATEGORY, max_length=100,null=True)
    
    def __str__(self):
        return f"{self.Title}"
