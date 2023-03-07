from django.contrib import admin

#Code derived from Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations
#Timestamp 35:46
# Code derived from "Build A Blog Comment Section - Django Blog #33" Timestamp 6:44
from .models import Posts, Comments, GreenPosts

admin.site.register(Posts)
admin.site.register(GreenPosts)
admin.site.register(Comments)

#Derived https://djangocentral.com/creating-comments-system-with-django/
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)