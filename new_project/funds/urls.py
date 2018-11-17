from django.urls import path
from . import views

app_name = 'funds'
urlpatterns = [

    path('fundsform', views.funds_view, name='funds_view'),

    path('fundstable', views.funds_table, name='funds_table'),

]