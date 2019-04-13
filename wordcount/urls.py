
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('',view.homepage,name='homepage'),
    #path('contact',view.contact)
    path('countword/', view.count, name='count1'),

    path('about/', view.aboutme,name='about'),
]
