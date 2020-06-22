from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    post_date = models.DateTimeField(default=datetime.now)
    post_user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.title

    def ShortenText (self):
        return self.description[:50]

class Comment (models.Model):
    comment = models.TextField()
    comment_date = models.DateTimeField(default=datetime.now)
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment[:50]