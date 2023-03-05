from django import forms
from django.contrib.auth.models import User
from .models import Posts, Comments, GreenPosts

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')