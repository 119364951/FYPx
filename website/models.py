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
class Comments(models.Model):
    posts = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Derived Python Django Tutorial: Full-Feautred Web App Part 5 timestamp 19:39
    # Code updated from "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 28:25
    def __str__(self):
        return '%s - %s' %  (self.posts.title, self.name)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
