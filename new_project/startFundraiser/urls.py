from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name = 'startFundraiser'

urlpatterns = [
    # /startFundraiser/
    path('', views.home, name='home'),
    #url('register/', views.register, name='register'),
    #url('login_user/', views.login_user, name='login_user'),
    #url('logout_user/', views.logout_user, name='logout_user'),
    url('start_campaign/', views.start_campaign, name='start_campaign'),
    url('all_campaigns/', views.campaigns, name='campaigns'),
    url('campaigns/creative/', views.creative, name='creative'),
    url('campaigns/social/', views.social, name='social'),
    url('campaigns/tech/', views.tech, name='tech'),
    url('campaign/(?P<campaign_id>[0-9]+)/', views.detail, name='campaign_detail'),
    url('index/', views.index, name='index'),
]
