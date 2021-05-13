from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', view=login, name='login'),
    path('submit', view=login_submit, name='login_submit'),
    path('home/', view=home, name='home'),
    path('sair/', view=sair, name='sair'),
    path('robos/<int:id>/', robos, name='robos')
]