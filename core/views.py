from django.shortcuts import render
# from .forms import UserForm
# from django.http import HttpResponseRedirect
# Create your views here.

def core(request):
    # submitted = False
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('core-index/?submitted=True')
    # else:
    #     form = UserForm
    #     if 'submitted' in request.GET:
    #         submitted = True
             
    return render(request, 'core-index.html')


