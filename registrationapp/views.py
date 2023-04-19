from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect
# Create your views here.




def signin(request):
    
    # submitted = False
    # if request.method == 'POST':
    #     ...

    return render(request, 'signin.html')


def signup(request):
    submitted = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/signup?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'signup.html', {'submitted' : submitted})