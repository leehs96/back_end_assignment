from django.db import models
from django.contrib.auth.models import  User
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
	        settings.AUTH_USER_MODEL,
	        on_delete=models.CASCADE,
	)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]