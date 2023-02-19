from django.db import models
# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 4:00
from django.utils import timezone
from django.contrib.auth.models import User
#Code derived from "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 29:00
from django.urls import reverse

# Change this for later Username: adming@gmail.com Email: admin@gmail.com Password: adminATgmail

# Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations Timestamp 2:19
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # If User gets deleted their posts get removed too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

#Derived Python Django Tutorial: Full-Feautred Web App Part 5 timestamp 19:39
#Code updated from "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 28:25
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
