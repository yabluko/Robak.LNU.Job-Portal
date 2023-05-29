from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from registrationapp.models import Profile, Post , Vacancy
from .forms import PostForm, SignUpForm, ProfilePicForm, ProfileUserForm, VacancyForm, OrderPostForm
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
        user_profile = profile.followed_by.all()
        number_of_followers = user_profile.count()
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

        return render(request,'profile-user.html', {'profile':profile, 'number_of_followers': number_of_followers} )
    else:
        messages.success(request, ('You must be logged in '))
        return redirect('main')    
 
def home(request):
    if request.user.is_authenticated:
        order_by = request.GET.get('order_by', 'default')
        if order_by == 'likes':
            posts = Post.objects.all().order_by('likes')
        elif order_by == '-created_at':
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.all().order_by('-created_at')

        form = PostForm(request.POST or None)
        profile = Profile.objects.get(user__id=request.user.id)
        user = request.user
        user_profile_follows = profile.followed_by.all()
        number_of_followers = user_profile_follows.count()
        current_url = reverse('home')


        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Your post has been posted!", extra_tags='message-success')
                return redirect('home')
            
        user_posts = user.posts_user.all()
        return render(request, 'home-page.html', {'form': form, 'profile': profile, 'number_of_followers':number_of_followers , 'user_posts':user_posts , 'posts':posts,'current_url':current_url})
    else:
        messages.success(request, "Your must be log in!")
        return render(request, 'home-page.html')

    
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


def vacancies(request):
    # vacancy = Vacancy.objects.get(user__id=request.user.id)
    profile = Profile.objects.get(user__id=request.user.id)
    vacancy = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancy': vacancy , 'profile': profile})

def vacancies__creating(request):
    if request.user.is_authenticated:
        vacancy_form = VacancyForm()
        if request.method == 'POST':
            vacancy_form = VacancyForm(request.POST)
            if vacancy_form.is_valid():
                job = vacancy_form.save() 
                job.user = request.user
                job.save()
                messages.success(request, ("Your vacancy posted"), extra_tags='message-success')
                return redirect('vacancies')
            else:
                messages.success(request, ("Your vacancy wasn't posted"), extra_tags='message-error')
                return redirect('vacancies-creation')    
            
    else :
        vacancy_form = VacancyForm()        
    return render(request, 'vacancies-creation.html', {'vacancy_form': vacancy_form})




def post_likes(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('home')        

    else:
        messages.success(request, "Your must be log in!")
        return redirect('main')


def vacancies_recommended(request):
    return render(request, 'vacancies-recomend.html')