from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    reg_date = models.DateTimeField(default=datetime.now)
    info = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.info.username
