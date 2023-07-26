from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_comments")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_posts")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    comments = models.ManyToManyField(Comment, blank=True, related_name="commented_posts")

class follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    timestamp = models.DateTimeField(auto_now_add=True)

class following(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    timestamp = models.DateTimeField(auto_now_add=True)
