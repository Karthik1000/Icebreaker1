"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
#from project import views
#from startFundraiser import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
#from django.contrib.auth.views import (password_reset, password_reset_done,
                                #    password_reset_confirm,password_reset_complete)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('project/', include('project.urls')),
    url('startFundraiser/', include('startFundraiser.urls')),
    url('funds/', include('funds.urls')),
    url('comment/', include('comment.urls')),
    #url('post/', views.post_list, name='post_list'),
    #url('login/', views.user_login, name='user_login'),
    #url('logout/', views.user_logout, name='user_logout'),
    #url('register/', views.user_register, name='user_register'),
    #url('profile/', views.edit_profile, name='edit_profile'),

    # password reset urls
    #url('password_reset/', auth_views.password_reset, name='password_reset'),
    #url('password_reset/done/',auth_views.password_reset_done, name='password_reset_done'),
    #url('password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    #url('reset/done/',auth_views.password_reset_complete, name='password_reset_complete'),

    path('',include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    #account_activation_sent
    #path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    #path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    #url('start_campaign/', views.start_campaign, name='start_campaign'),
    #url('all_campaigns/', views.campaigns, name='campaigns'),
    #url('campaigns/creative/', views.creative, name='creative'),
    #url('campaigns/social/', views.social, name='social'),
    #url('campaigns/tech/', views.tech, name='tech'),
    #url('campaign/(?P<campaign_id>[0-9]+)/', views.detail, name='campaign_detail'),
    #url('index/', views.index, name='index'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
