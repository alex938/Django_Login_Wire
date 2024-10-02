from django.urls import URLPattern, path
from typing import List
from . import views
from django.contrib.auth.views import LogoutView

app_name: str = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]