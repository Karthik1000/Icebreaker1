from django.conf.urls import url
from . import views

app_name = 'project'

urlpatterns = [
    url('post/', views.post_list, name='post_list'),
    url('login/', views.user_login, name='user_login'),
    url('logout/', views.user_logout, name='user_logout'),
    url('register/', views.user_register, name='user_register'),
    url('new_user_reg/', views.new_user_reg, name='new_user_reg'),
    url('profile/', views.edit_profile, name='edit_profile'),
    url('home/', views.home, name='home'),


]
