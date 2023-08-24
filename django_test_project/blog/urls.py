from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="posts"),
    path("post/create", views.create_post, name="post-create"), # type: ignore
    path("about/", views.about, name="about"),
]
