from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile, Post
from .forms import PostForm
# Create your views here.

def main(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(request, email=email, password=password)
                
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, ("You have been succesfully log in"))
    #         return redirect('main')
    #     else:
    #         messages.success(request,("There was an error logging in .Please try again..."))
    #         return redirect('home')
    # else:    
    return render(request, 'initial-page.html')


def signin(request):
    return render(request, 'login-index.html')


def signup(request):
    return render(request, 'signup.html')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile-page.html', {"profiles": profiles})
    
 
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
        posts = Post.objects.all().order_by("-created_at")
        return render(request, 'home-page.html', {'posts': posts})
    

# def profile(request):
#     return render(request, 'profile-page.html')    