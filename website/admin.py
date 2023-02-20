from django.contrib import admin

#Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations
#Timestamp 35:46
# Code derived from "Build A Blog Comment Section - Django Blog #33" Timestamp 6:44
from .models import Posts, Comments

admin.site.register(Posts)
admin.site.register(Comments)
