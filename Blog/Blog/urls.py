"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from BlogApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tb',views.technologyblog,name='Blog'),
    path('',views.show,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('readmore/<int:id>',views.readmore,name='readmore'),
    path('search',views.search,name='search'),
    path('logout',views.logout,name='logout')
    
]
