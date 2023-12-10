from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like', blank=True)

    def total_likes(self):
        return self.like.count()


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_text=models.TextField()

class UserProfile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio= models.CharField(max_length=255)
    fb_url=models.CharField(max_length=255,null=True,blank=True)
    insta_url=models.CharField(max_length=255,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='static/images/author/')
