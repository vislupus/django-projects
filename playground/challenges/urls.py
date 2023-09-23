from django.urls import path

from . import views

urlpatterns = [
    path("animal/<pet>", views.pet),
    path("animal-red/<pet>", views.pet_red, name="animal-red"),
    path("animals/", views.animal),
    path("animals/<animal>", views.animals),
    path("challenges/", views.index),
    path("challenges/<int:month>", views.monthly_challenge_by_number), # https://docs.djangoproject.com/en/4.2/topics/http/urls/
    path("challenges/<str:month>", views.monthly_challenge, name="month-challenge"),
]
