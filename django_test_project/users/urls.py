from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.sign_in, name="login"), # type: ignore
    path('logout/', views.sign_out, name='logout'), # type: ignore
    path('register/', views.sign_up, name='register'), # type: ignore
]
