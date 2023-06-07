from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from registrationapp.models import Profile, Post , Vacancy, Company, CompanyProfile
from .forms import PostForm, SignUpForm, ProfilePicForm, ProfileUserForm, VacancyForm, Vacancy_Apply
from django.contrib.auth.models import User
from django.core.mail import send_mail
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
        posts = Post.objects.filter(user_id=pk)
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

        return render(request,'profile-user.html', {'profile':profile, 'number_of_followers': number_of_followers, 'posts':  posts} )
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

    vacancy = Vacancy.objects.filter(skills=profile.skills)
    
    return render(request, 'vacancies.html', {'vacancy': vacancy , 'profile': profile})

def vacancies__creating(request):
    if request.user.is_authenticated:
        vacancy_form = Vacancy_Apply()
        username = request.user.username
        if request.method == 'POST':
            vacancy_form = Vacancy_Apply(request.POST, request.FILES)
            email = request.POST['email']
            number = request.POST['number']
            # resume = request.FILES['resume']
            # send_mail(
            #     username, 
            #     email,
            #     ['linkedinclone1@gmail.com'], 
            # )
            

            messages.success(request, ("Your apply was sended succeeded"), extra_tags='message-success')
            return redirect('vacancies')
    else:
        messages.success(request, ("Your apply wasn't posted"), extra_tags='message-error')
        return redirect('vacancies')      
    return render(request, 'vacancies-creation.html', {'vacancy_form': vacancy_form })


def vacancies_recommended(request, vacancy_pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        vacancies_all = Vacancy.objects.filter(skills=profile.skills)
        vacancy_count = Vacancy.objects.filter(skills=profile.skills).count()
        vacancy = Vacancy.objects.get(id=vacancy_pk)
        company_profile = CompanyProfile.objects.get(company_id=vacancy.company.id)
        # recomendation_algorithm(vacancies_all,vacancy)
    else:  
        return redirect('home')
    
    return render(request, 'vacancies-recomend.html', {'vacancy':vacancy , 'vacancies_all':vacancies_all, 'company_profile':company_profile, 'profile':profile ,'vacancy_count':vacancy_count})

def searched_vacancies(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        vacancies = Vacancy.objects.filter(position__contains=searched)
        request.session['searched'] = searched
        vacancy_count = vacancies.count()
        return render(request, 'searched-vacancies.html', {'searched':searched, 'vacancies':vacancies, 'vacancy_count':vacancy_count})
    else:
        return render(request, 'searched-vacancies.html', {})


def searched_vacancies_bio(request, vacancy_pk):
    vacancy = Vacancy.objects.get(id=vacancy_pk)
    searched = request.session.get('searched')
    vacancies = Vacancy.objects.filter(position__contains=searched)
    return render(request, 'searched-vacancies-bio.html',{'vacancy':vacancy, 'vacancies':vacancies})


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


def favourites(request , id ):
    if request.user.is_authenticated:
        vacancy = get_object_or_404(Vacancy, id=id)
        if vacancy.favourites.filter(id =request.user.id).exists():
            vacancy.favourites.remove(request.user)
        else:
            vacancy.favourites.add(request.user)
        return redirect('vacancies') 
    return render(request, 'vacancies.html', {})


def favourites_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user__id=request.user.id)
        new = Vacancy.objects.filter(favourites=request.user)
        count_new = new.count()
        return render(request, 'favourites.html', {'new':new, 'profile':profile ,'count_new':count_new} )


def recomendation_algorithm(vacancy_all,vacancy):
    for vac in range(vacancy_all):
        vacancy_all_cleaned = vac.skills.replace(',','')
        vacancy_cleaned = vacancy.skills.replace(',','')

        print(vacancy_all_cleaned)
        print(vacancy_cleaned)

        v = vacancy_all_cleaned.strip()
        y = vacancy_cleaned.strip()
        if v ==  y:
            return print('Equals')
        else:
            return print('Not equals')    