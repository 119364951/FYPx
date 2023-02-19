# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 11 - Pagination" Timestamp 25:10
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
from .models import Posts

# Create your views here
# Posts: This variable has the innards of our posts
# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 3 - Templates" Timestamp 10:20

#Dummy data
#posts = [
#   {
#        'author': 'Jane Doe',
#        'title': 'Test Post',
#        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis commodo dapibus congue. Aliquam accumsan finibus tellus eget lacinia. Donec blandit tortor ac erat condimentum, sit amet aliquet dui hendrerit. Phasellus ante nisl, tempor in posuere at, vulputate nec quam. Nulla consequat nisl in massa semper, ac pretium dui tincidunt. Nulla porttitor enim pretium urna rhoncus blandit. Phasellus malesuada tempus venenatis. Mauris semper cursus ornare. Nullam rhoncus eros non pellentesque auctor. Nulla blandit consectetur odio. Aenean in ante venenatis, malesuada quam a, consectetur arcu. Aliquam fermentum lectus orci, vel imperdiet diam pharetra ut.',
#        'date_posted': 'August 28, 2018'
#    },
#    {
#        'author': 'L. Eg Schafer',
#        'title': 'Test Post 2',
#        'content': 'Sed consequat, massa ut dictum laoreet, massa diam pellentesque mi, quis condimentum turpis neque egestas neque. Morbi rutrum erat turpis, aliquam ornare est condimentum non. Morbi felis magna, luctus vel lacus sit amet, sodales hendrerit mi. Nullam porta eu urna ut congue. Vestibulum vel ex venenatis, blandit nulla eu, aliquam erat. Curabitur placerat, sem quis suscipit hendrerit, nisi tellus venenatis nibh, nec vestibulum arcu massa non sem. Pellentesque non arcu nec elit sollicitudin dignissim dapibus vitae arcu. Vestibulum vel cursus ante, quis ullamcorper leo.',
#        'date_posted': 'August 30, 2020'
#    },
#    {
#        'author': 'River Cuomo',
#        'title': 'Test Post 3',
#        'content': 'In sed lobortis justo. Aenean vel lectus ipsum. Curabitur vitae lacus hendrerit, accumsan enim sit amet, placerat leo. Nulla gravida metus et lacinia convallis. Aliquam sapien sapien, hendrerit at lorem vel, dapibus euismod velit. Aenean vel ex eget est porttitor ultrices consequat vitae libero. Donec laoreet nec urna quis rutrum. Quisque nibh sapien, interdum et orci nec, suscipit suscipit velit. Vivamus at luctus ex. Vivamus sed dignissim eros. Sed quis diam aliquam est hendrerit bibendum.',
#        'date_posted': 'September 15, 2020'
#    },
#    {
#        'author': 'Matt Sharp',
#        'title': 'Test Post 4',
#        'content': 'Curabitur tristique sem nec tellus faucibus gravida. Maecenas tempus vitae eros ut finibus. Quisque consectetur dui ut nulla convallis, ut sodales massa accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus sit amet eros bibendum, aliquam turpis sit amet, luctus dui. Cras iaculis, sem a lobortis aliquam, quam ante pulvinar mauris, ac maximus augue tortor sed tortor. Quisque cursus vehicula iaculis. Aenean rutrum bibendum massa, nec suscipit felis mollis vel.',
#        'date_posted': 'September 21, 2020'
#    }
#]

# Code derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 4:00 and 12:40
# The visible tidbits on our website
# Connects to the URLs
def home(request):
    # Context: allows us to deploy info from here to the templates
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'website/home.html', context)

# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 13:25
def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

# Code derived from video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 3:20, 6:23, 7:30
class PostListView(ListView):
    model = Posts
    template_name = 'website/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # Not changed because newer articles would be better to see
    ordering = ['date_posted']
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

# Own Code derived from "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes"
def archives(request):
    return render(request, 'website/archives.html', {'title': 'Archives'})

def alternatives(request):
    return render(request, 'website/alternatives.html', {'title': 'Alternatives'})

def greenwashing(request):
    return render(request, 'website/greenwashing.html', {'title': 'Greenwashing'})

