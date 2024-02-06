from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader


job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]

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

    context = {"job_title_list": job_title}
    return render(request, "app/index.html", context)


def job_detail(request, id):

    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        context = {"job_title": job_title[id], "job_description": job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")