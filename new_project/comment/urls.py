from django.urls import path
from . import views

app_name = 'comment'

urlpatterns=[
    path('create/',views.comment,name='create'),
]
