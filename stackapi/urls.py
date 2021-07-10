from django.contrib import admin
from django.urls import path
from stackapi import views

urlpatterns = [
    path('index/', views.index),
    path('QuestionAPI/', views.QuestionAPI),
    path('latest/', views.latest),
]


