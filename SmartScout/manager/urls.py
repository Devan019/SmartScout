"""
URL configuration for smartscout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from os import name
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'manager'

urlpatterns = [
    path('',views.home,name="home"),
    path('forms/',views.getRecruitmentForm, name="readForms"),
    path("forms/create/",views.generateRecruitmentForm , name="genarateForm"),
    path('forms/deactivate/<int:id>/', views.doDeactivate, name="deactivate"),
    path('forms/activate/<int:id>/', views.doActivate, name="activate"),
    path('forms/update/<int:id>/', views.updateRecruitmentForm, name="updateForm"),
    path('forms/delete/<int:id>/', views.deleteRecruitmentForm, name="deleteForm"),
    path('forms/applications/<int:id>', views.showApplications, name="applications"),
    path("application/<int:id>/",views.showProfile,name="viewApplication"),
    path('application/process/<int:application_id>/', views.process_application, name='process_application'),
    path('applications/<int:id>/',views.showsStatusApplications, name="getApplication"),
    path('applications/',views.showsDeafultStatusApplications, name="getDefaultApplication")
]
