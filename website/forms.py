from django import forms
from django.contrib.auth.models import User
from .models import Posts, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ["title", "content", "image"]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)