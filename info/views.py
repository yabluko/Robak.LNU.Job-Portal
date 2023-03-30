from django.shortcuts import render
from core.models import Account

# Create your views here.
def info(request):
    account_list = Account.objects.all()
    return render(request, 'info-index.html', {"accounts":account_list})