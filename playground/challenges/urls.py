from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),  # /challenges/
    path("astronomical/star", views.stars),
    path("animals/<str:animal>", views.pets),
    path("challenges/<int:month>", views.monthly_challenge_by_number), # https://docs.djangoproject.com/en/4.2/topics/http/urls/
    path("challenges/<str:month>", views.monthly_challenge, name="month-challenge"),
]
