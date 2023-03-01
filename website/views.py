# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 25:10
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 32:10, 36:50
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 25:30
from django.contrib.auth.models import User

# Code derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 3:26
from django.http import HttpResponse

# Code derived from the video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 3:05, 10:43, 19:50, 39:20
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

## Code derived from the video "Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations"
# Timestamp 28:37
#Code derived from "Post Blog Comments - Django Blog #34" Timestmap 5:48
from .models import Posts, Comments, GreenPosts

# Create your views here
# Posts: This variable has the innards of our posts
# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 3 - Templates" Timestamp 10:20

# Code derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 4:00 and 12:40
# The visible tidbits on our website
# Connects to the URLs
def home(request):
    # Context: allows us to deploy info from here to the templates
    posts = Posts.objects.filter().order_by('-date_posted')[:2]
    greenposts = GreenPosts.objects.filter().order_by('-date_posted')[:2]

    context = {
        'greenposts' : greenposts,
        'posts': posts
    }

    return render(request, 'website/home.html', context,)

# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 13:25
def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

# Alternatives Posts
# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 3:20, 6:23, 7:30
class PostListView(ListView):
    model = Posts
    template_name = 'website/alternatives.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # Not changed because newer articles would be better to see
    ordering = ['-date_posted']
# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 8:40
    paginate_by = 5

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 23:20
class UserPostListView(ListView):
    model = Posts
    template_name = 'website/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 8:40, 25:55
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 11:00,,22:08
class PostDetailView(DetailView):
    model = Posts

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 20:21, 25:25
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 33:15
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 39:40, 46:25
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#Code derived from "Post Blog Comments - Django Blog #34" Timestmap 5:48
class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Greenwashing Posts

# Own Code derived from "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes"
def archives(request):
    return render(request, 'website/archives.html', {'title': 'Archives'})

def alternatives(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'website/alternatives.html', context)

def greenwashing(request):
    # Context: allows us to deploy info from here to the templates
    context = {
        'greenposts': GreenPosts.objects.all()
    }
    return render(request, 'website/greenwashing.html', {'title': 'greenwashing'})

class GreenPostListView(ListView):
    model = GreenPosts
    template_name = 'website/greenwashing.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'greenposts'
    # Not changed because newer articles would be better to see
    ordering = ['-date_posted']
# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 8:40
    paginate_by = 5

#Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 23:20
class GreenUserPostListView(ListView):
    model = Posts
    template_name = 'website/greenuser_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'greenposts'
# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 8:40, 25:55
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return GreenPosts.objects.filter(author=user).order_by('-date_posted')

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 11:00,,22:08
class GreenPostDetailView(DetailView):
    model = GreenPosts

# Based off "https://djangoguide.readthedocs.io/en/latest/django/search.html"
class SearchPosts(ListView):
    template_name = 'website/alternatives.html'
    def get_queryset(self):
        val = self.kwargs.get("urlsearch")
        if val:
            queryset = Posts.objects.filter(title__icontains=val)
        else:
            queryset = Posts.objects.none()
        return queryset


