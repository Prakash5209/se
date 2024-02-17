from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class ProfileDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'real_user')
    image = models.ImageField(upload_to='profile',blank=True,null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

