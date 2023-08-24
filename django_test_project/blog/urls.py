from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="posts"),
    path("post/create", views.create_post, name="post-create"), # type: ignore
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'), # type: ignore
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'), # type: ignore
    path("about/", views.about, name="about"),
]
