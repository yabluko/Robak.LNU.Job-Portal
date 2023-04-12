from django.shortcuts import render
from django.shortcuts import render , redirect
from core.models import Account
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def signin(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password'] 
    #     user = authenticate(request, username=username , email=email, password=password)
        # user = User.objects.create_user(username=username, email=email, password=password)
 
        # user_model = User.objects.get(username=username)
        # new_profile = Account.objects.create(email=email, username=username, password=password)

        # if user is not None:
        #     # A backend authenticated the credentials
        #     login(request, user)
        #     return redirect('')
        # else:
        #     messages.success(request,)
    # No backend authenticated the credentials
        # return redirect('login/')
    return render(request, 'signin.html')


def signup(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = Account.objects.create(first_name=firstname, last_name=lastname, username=username, email=email, password=password)

        myuser.save()

        messages.success(request, "Your Account has been succesfully created")
        return redirect('/registration/signin')

    return render(request, 'signup.html')