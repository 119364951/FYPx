# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 5:30
from mysite.urls import path
from.import views

# Updated derived from the video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 4:00, 11:30, 21:10, 40:30
# Code updated and derived from "Post Blog Comments - Django Blog #34" Timestamp 6:25
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostCommentView

# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 5:30 and 14:10
# Updated derived from the video "Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts" Timestamp 4:00, 18:35
# Creates a URL path for the app
urlpatterns = [
    path('about/', views.about, name='website-about'),
    path('', PostListView.as_view(), name='website-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/', PostCommentView.as_view(), name='post-comment'),

    # Own code derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 5:30 and 14:10
    path('archives/', views.archives, name='website-archives'),
    path('alternatives/', views.alternatives, name='website-alternatives'),
    path('greenwashing/', views.greenwashing, name='website-greenwashing'),
]
