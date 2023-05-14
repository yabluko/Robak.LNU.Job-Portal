from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from registrationapp.models import Profile, Post 
from .forms import PostForm, SignUpForm, ProfilePicForm, ProfileUserForm
from django.contrib.auth.models import User
# Create your views here.

def main(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
                 
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been succesfully log in"), extra_tags='message-success')
            return redirect('home')
        else:
            messages.success(request,("There was an error logging in .Please try again..."),extra_tags='message-error')
            return redirect('main')
    else:    
        return render(request, 'initial-page.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been succesfully log out"), extra_tags='message-error')
    return redirect('main')

def signin(request):
    return render(request, 'login-index.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
             
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')


    return render(request, 'signup.html', {'form':form})


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
        username = request.user.username
        form = PostForm(request.POST or None)
        profile = Profile.objects.get(user__id=request.user.id)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Your post has been posted!", extra_tags='message-success')
                return redirect('home')

        posts = Post.objects.all().order_by("-created_at")
        number_of_posts = posts.count()
        # posts = Profile.objects.all()
        # number_of_posts = posts.count()
        return render(request, 'home-page.html', {'posts': posts, 'form': form, 'username': username, 'profile': profile,'number_of_posts':number_of_posts })
    else:
        messages.success(request, "Your must be log in!")
        posts = Post.objects.all().order_by("-created_at")

    return render(request, 'home-page.html',{'posts': posts, 'user':username, 'profile':profile})

    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        
        user_form = ProfileUserForm(request.POST or None , request.FILES or None, instance=profile_user)
        profile_form_picture = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form_picture.is_valid():
            user_form.save()
            profile_form_picture.save()
     
            login(request, current_user)
            messages.success(request, "Your profile has been be updated", extra_tags='message-success')
            return redirect('home')

        return render(request, 'update-user.html',{'user_form': user_form, 'profile_form': profile_form_picture})
    else:
        messages.success(request, "Your must be log in!")
        return redirect('main')
