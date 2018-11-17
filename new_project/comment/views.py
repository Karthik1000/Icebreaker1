from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
import re

# Create your views here.
#@login_required(login_url='/register/login')
def comment(request):
    if request.method == 'POST':
        form = forms.createcomment(request.POST)
        if form.is_valid():
            a = request.POST.get('content').split(' ')
            b = ['fuck','crap','shit']
            d = 0
            for c in a:
                if c in b:
                    d = d+1
            if d==0:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return HttpResponse('comment is {}'.format(a))
            else:
                return HttpResponse('Do not use bad words')
    else:
        form = forms.createcomment()
    return render(request,'comment/create.html',{'form':form})
