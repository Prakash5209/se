from django.db import models
from django.conf import settings


from account.models import User

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length =255)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog,on_delete =models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.blog}--{self.comment}"