from django.db import models
from app.models import JobPost


# Create your models here.
class Uploads(models.Model):
    """An image upload."""

    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    

class JobApplication(models.Model):
    """A job application upload."""

    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    applied_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="files")
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Application for {self.job.title} by {self.name}"