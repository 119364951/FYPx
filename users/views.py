from django.shortcuts import render, redirect
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 6 - User Registration"
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Code further derived from "Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile" Tiemstamp 3:52
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Code derived from "Python Django Tutorial: Full-Featured Web App Part 6 - User Registration"
# Timestamp 4:05
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Now you ar able to Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Code Derived "Python Django Tutorial: Full-Featured Web App Part 7 - Login and Logout System" Timestamp 22:12,27:04
@login_required
def profile(request):
    if request.method == 'POST':
     u_form = UserUpdateForm(request.POST, instance=request.user)
     p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
     if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         messages.success(request, f'Has been updated')
         return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    return render(request, 'users/profile.html', context)

