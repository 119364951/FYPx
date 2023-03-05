from django.db import models
# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 4:00
from django.utils import timezone
from django.contrib.auth.models import User
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 29:00
from django.urls import reverse


# Change this for later Username: adming@gmail.com Email: admin@gmail.com Password: adminATgmail

# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 2:19
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # If User gets deleted their posts get removed too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 2:19
class GreenPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # If User gets deleted their posts get removed too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

 #Code derived from "Build A Blog Comment Section - Django Blog #33" Timestamp 1:40
 #Code Derived from https://djangocentral.com/creating-comments-system-with-django/
class Comments(models.Model):
    posts = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format (self.body, self.name)

