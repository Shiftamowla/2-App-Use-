from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Custom_user(AbstractUser):
    USER=[
        ('viewers','Viewers'),
        ('creator','Creator')
    ]

    user_type=models.CharField(choices=USER,max_length=100,null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    
class viewersProfileModel(models.Model):
    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='viewersProfile',null=True)
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    
    
    def __str__(self):
        return f"{self.user.username}"   
    
class CreatorProfileModel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE,related_name='bloggersProfile',null=True)
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    
    def __str__(self):
        return f"{self.user.username}"
    
class BlogModel(models.Model):
    CATEGORY=[
        ('politics','Politics'),
        ('sports','Sports'),
        ('intertainment','Intertainment'),

    ]
    user=models.ForeignKey(Custom_user,on_delete=models.CASCADE,null=True)
    Image=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    Title=models.CharField(max_length=100,null=True)
    Content=models.CharField(max_length=100,null=True)
    Author=models.CharField(max_length=100,null=True)
    Date=models.DateField(default=timezone.now,null=True)
    Categories=models.CharField(choices=CATEGORY, max_length=100,null=True)
    
    def __str__(self):
        return f"{self.Title}"   
    

