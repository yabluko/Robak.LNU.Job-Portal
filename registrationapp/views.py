from django.shortcuts import render
from django.shortcuts import render , redirect
from core.models import Account
# Create your views here.

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']

        # user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
 
        # user_model = User.objects.get(username=username)
        new_profile = Account.objects.create(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
        return redirect('login/')
    
    return render(request, 'registrationapp/registration.html')

def login(request):
    return render(request, 'registrationapp/login.html')