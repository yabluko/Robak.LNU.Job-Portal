from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
# Create your views here.

def home(request):
    return render(request, 'core-index.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user) # виключити де user = request.user
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ("You must be log in to view this page"))
        return redirect('home')
 