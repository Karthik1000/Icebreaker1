from django.shortcuts import render
from django.http import HttpResponse
from .models import post,Profile
from .forms import UserLoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.urls import reverse
from django.contrib.auth.views import password_reset, password_reset_done
from django.utils.encoding import force_bytes,force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from new_project.tokens import account_activation_token
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.forms import modelformset_factory
from django.contrib import messages
from datetime import datetime
import random
from django.contrib.auth.models import User
#from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'project/home.html')

def account_activation_sent(request):
    print('-------------in account_activation_sent-------------')
    return render(request, 'registration/account_activation_sent.html')

def post_list(request):
    posts = post.published.all()
    query = request.GET.get('q')
    if query:
        posts = post.objects.filter(
        Q(title__icontains=query)|
        Q(author__username=query)|
        Q(body__icontains=query))

    context = {
        'posts' : posts
    }
    return render(request, 'project/post_list.html',context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('project:post_list')

                else:
                    return HttpResponse('User is not active')

            else:
                return HttpResponse('User is not available')

    else:
        form = UserLoginForm()


    contexts = {'form':form}

    return render(request, 'project/login.html', contexts)

def user_logout(request):
    logout(request)
    return redirect('project:post_list')

#fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
def email_verify(form):
    rand_numb = random.randint(100000, 999999)
    b = str(rand_numb)
    email = [form.data['email']]
    response = send_mail("Hello rock77", b, "yagnakarthik100@gmail.com", email)
    return b

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            b = email_verify(form)
            print(b)
            username = form.data['username']
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']
            password1 = form.data['password1']
            context1 = {
                'username':username,
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password1':password1,
                'b':b,
            }

            #new_user.save()
            #Profile.objects.create(user = new_user)
            return render(request,'project/verify.html', context1)
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }
    return render(request,'registration/register.html', context)

def new_user_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        new_user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
        new_user.set_password(request.POST['password1'])
        new_user.save()
        Profile.objects.create(user = new_user)
    return HttpResponse('hello world congrats')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('project:post_list')

    else:
        user_form = UserEditForm(instance=request.user)
        #print(request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        #if num < 1:
        #    Profile.objects.create(user = request.user)

        #    num +=1
        #else:
        #    Profile.objects.filter(user = request.user)
        #    profile_form = ProfileEditForm(instance=request.user.profile)
        #print(profile_form)


    contexts = {
        'user_form': user_form,
        'profile_form': profile_form,

    }

    return render(request, 'project/edit_profile.html', contexts)
