from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile, Post
from .forms import PostForm
# Create your views here.

def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
                 
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been succesfully log in"))
            return redirect('home')
        else:
            messages.success(request,("There was an error logging in .Please try again..."))
            return redirect('main')
        
    else:    
        return render(request, 'initial-page.html')


def signin(request):
    return render(request, 'login-index.html')


def signup(request):
    return render(request, 'signup.html')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile-list.html', {"profiles": profiles})
    

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        if request.method == 'POST':
            #Get current user
            current_user_profile = request.user.profile
            #Get form data
            action = request.POST['follow']
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()            

        return render(request,'profile-user.html', {'profile':profile} )
    else:
        messages.success(request, ('You must be logged in '))
        return redirect('main')

 
def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Your post has been posted!")
                return redirect('home')

        posts = Post.objects.all().order_by("-created_at")
        return render(request, 'home-page.html', {'posts': posts, 'form': form})
    else:
        messages.success(request, "Your must be log in!")
        posts = Post.objects.all().order_by("-created_at")
    return render(request, 'home-page.html',{'posts': posts})
    

# def profile(request):
#     return render(request, 'profile-page.html')    