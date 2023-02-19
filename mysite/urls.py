"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('website/', include('website.urls'))
"""
from django.contrib import admin

# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 8:00
from django.urls import path, include
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 6 - User Registration" Timestamp: 13:59
from users import views as user_views
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 7 - Login and Logout System" Timestamp: 1:25
from django.contrib.auth import views as auth_views
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture" Timestamp 22:40
from django.conf import settings
from django.conf.urls.static import static

# Derived from the video "Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes" Timestamp 8:00
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 6 - User Registration" Timestamp: 14:35
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 7 - Login and Logout System" Timestamp: 2:13, 4:44, 24:00
# Connects the project urls to the app urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('website.urls')),
]


# Code derived from "Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture" Timestamp 22:40
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

