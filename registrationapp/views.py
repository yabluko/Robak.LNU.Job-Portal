from django.shortcuts import render
from django.shortcuts import render , redirect
from core.models import Account
# from django.contrib import messages
# from django.contrib.auth import authenticate,login
# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'] 
        # user = authenticate(request, username=username , email=email, password=password)
        # user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
 
        # user_model = User.objects.get(username=username)
        new_profile = Account.objects.create(first_name=firstname, last_name=lastname, email=email, username=username, password=password)

        # if user is not None:
        #     # A backend authenticated the credentials
        #     login(request, user)
        #     return redirect('')
        # else:
        #     messages.success(request,)
    # No backend authenticated the credentials
        return redirect('login/')
    return render(request, 'registration-index.html')

# def login(request):
#     return render(request, 'registrationapp/login.html')