from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_followers = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
    user_following = models.ManyToManyField("self", blank=True, related_name="following", symmetrical=False)
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


