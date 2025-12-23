"""
URL configuration for crowdsolver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from problems import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('signup/',views.sign_up, name = 'sign_up'),
    path('login/',views.log_in, name = 'log_in'),
    path('member/',views.member, name = 'member'),
    path('home/',views.home, name = 'home'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('raiseproblem/',views.raise_problem, name = 'raiseproblem'),
    path('suggestions/',views.suggestions, name = 'suggestions'),
    path('givesuggestions/',views.givesuggestions, name = 'givesuggestions'),
    path('voting/',views.vote, name = 'voting'),
    path('profile/',views.profile, name = 'profile'),
    path('finalsolution/',views.finalsolution, name = 'finalsolution'),
    path('wrong/',views.wrong, name = 'wrong'),
    path('logout/',views.logout, name = 'logout'),
    path('solutions/',views.solutions, name = 'solutions'),
]
