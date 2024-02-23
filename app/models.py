from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    """An author."""

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)


class Location(models.Model):
    """A location of a job post."""

    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)


class JobPost(models.Model):
    """A job post."""

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        """Overrides the save method to automatically generate a slug based on the title."""

        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        """A string representation of a job post object."""

        return f"{self.title} with Salary {self.salary}"