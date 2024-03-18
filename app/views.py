from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from uploadapp.views import upload_file as upload_submit_job_application

from app.models import JobPost


# Create your views here.
def job_list(request):

    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):

    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
    

submit_job_application = upload_submit_job_application