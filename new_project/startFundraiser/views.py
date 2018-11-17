from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Campaign
from .forms import CampaignForm


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    projects = Campaign.objects.all()
    query = request.GET.get('q')
    if query:
        projects = projects.filter(
            Q(campaign_Title__icontains=query) |
            Q(campaign_Tagline__icontains=query) |
            Q(campaign_Category__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()
        return render(request, 'startFundraiser/campaigns.html', {'projects': projects})
    else:
        return render(request, 'startFundraiser/campaigns.html', {'projects': projects})


def home(request):
    return render(request, 'startFundraiser/base.html')


def campaigns(request):
    projects = Campaign.objects.all()
    return render(request, 'startFundraiser/campaigns.html', {'projects': projects})


def creative(request):
    projects = Campaign.objects.filter(campaign_Category__icontains='art')
    return render(request, 'startFundraiser/campaigns.html', {'projects': projects})


def social(request):
    projects = Campaign.objects.filter(campaign_Category__icontains='culture')
    return render(request, 'startFundraiser/campaigns.html', {'projects': projects})


def tech(request):
    projects = Campaign.objects.filter(campaign_Category__icontains='education')
    return render(request, 'startFundraiser/campaigns.html', {'projects': projects})



def start_campaign(request):
    form = CampaignForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        campaign = form.save(commit=False)
        campaign.user = request.user
        campaign.image = request.FILES['image']
        # tags = form.cleaned_data['campaign.tags']
        # tag = tags.split()
        # print(tag)
        file_type = campaign.image.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'campaign': campaign,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'startFundraiser/campaign-form.html', context)
        campaign.save()
        return render(request, 'startFundraiser/base.html', {'campaign': campaign})
    context = {
        "form": form
    }
    return render(request, 'startFundraiser/campaign-form.html', context)


def detail(request, campaign_id):
    #   campaign1 = Campaign.objects.filter(pk=campaign_id)
    campaign1 = get_object_or_404(Campaign, pk=campaign_id)
    tags = campaign1.tags
    tag = tags.split()
    context = {
        'campaign1': campaign1,
        'tag': tag,
    }
    return render(request, 'startFundraiser/detail.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'startFundraiser/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                campaigns = Campaign.objects.filter(user=request.user)
                return render(request, 'startFundraiser/base.html', {'campaigns': campaigns})
            else:
                return render(request, 'startFundraiser/login.html',
                              {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'startFundraiser/login.html', {'error_message': 'Invalid login'})
    return render(request, 'startFundraiser/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                campaigns = Campaign.objects.filter(user=request.user)
                return render(request, 'startFundraiser/base.html', {'campaigns': campaigns})
    context = {
        "form": form,
    }
    return render(request, 'startFundraiser/register.html', context)
