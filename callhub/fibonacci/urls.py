from django.urls import path
from . import views

app_name = 'fibonacci'
urlpatterns = [
    path('', views.resp, name='resp')
]