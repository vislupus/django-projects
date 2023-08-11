from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('hello_world.urls')),
    path("projects/", include("projects.urls")),
]
