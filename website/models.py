
from django.db import models
# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 4:00
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
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
    image = models.ImageField(default='/media/posts/default.jpg', upload_to='posts')
    #Code derived "How to add Like/Unlike button to your Django Blog"
    likes = models.ManyToManyField(User, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 2:19
class GreenPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # If User gets deleted their posts get removed too
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/media/posts/default.jpg', upload_to='posts')
    #Code derived "How to add Like/Unlike button to your Django Blog"
    likes = models.ManyToManyField(User, related_name='greenpost_like')

    def number_of_likes(self):
        return self.likes.count()

#TBC
class Comment(models.Model):
    post = models.ForeignKey('website.Posts', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


