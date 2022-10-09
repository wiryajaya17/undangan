from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

def garcon(request):
    return render(request, 'index.html')

def index(request):
    # return render(request, 'index.html')
    return HttpResponseRedirect(reverse('index'))

def featuresType(request):
    # return render(request, 'features-type.html')
    return HttpResponseRedirect(reverse('features-type'))

def pageappUserList(request):
    # return render(request, 'pageapp-userlist.html')
    return HttpResponseRedirect(reverse('pageapp-userlist'))
