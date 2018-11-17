from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class comment(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
