from django.urls import URLPattern, path
from typing import List
from . import views

app_name: str = 'core'

urlpatterns: List[URLPattern] = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
]