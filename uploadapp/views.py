from django.shortcuts import render, redirect
from django.urls import reverse
from uploadapp.forms import JobApplicationForm, UploadForm
from app.models import JobPost

# Create your views here.
def upload_image(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            return render(request, "uploadapp/add_image.html", {"form": form, "saved_object": saved_object})
    else:
        form = UploadForm()

    return render(request, "uploadapp/add_image.html", {"form": form})


def upload_file(request, job_id):

    job = JobPost.objects.get(id=job_id)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.job = job
            form.save()
            return redirect(reverse("thank_you"))
    else:
        form = JobApplicationForm()

    return render(request, "uploadapp/add_file.html", {"form": form})


def thank_you(request):
    """A view function to render a thank you page after successful submission."""
    
    context = {}
    return render(request, "uploadapp/thank_you.html", context)