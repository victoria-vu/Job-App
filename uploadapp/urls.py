from . import views
from django.urls import path

urlpatterns = [
    path("image/", views.upload_image, name="upload_image"),
    path("file/", views.upload_file, name="upload_file"),
    path("application_success/", views.application_success, name="application_success")
]