from django.urls import URLPattern, path
from typing import List
from . import views

app_name: str = 'account'

urlpatterns: List[URLPattern] = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]