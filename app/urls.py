from django.urls import path
from app import views


urlpatterns = [
    path("", views.job_list, name="jobs_home"),
    path("job/<int:id>", views.job_detail, name="jobs_detail"),
    path("job/apply/<int:job_id>/", views.submit_job_application, name="submit_job_application"),
]