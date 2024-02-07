from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

from app.models import JobPost


# Create your views here.
class TempClass:
    x = 5

def hello(request):
    
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context={
        "name": "Django", 
        "age": 30, 
        "first_list": list, 
        "temp_object": temp, 
        "is_authenticated": is_authenticated
        }
    return render(request,"app/hello.html",context)


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