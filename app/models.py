from django.db import models
from django.utils.text import slugify

# Create your models here.
class JobPost(models.Model):
    """A job post."""

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)

    def save(self, *args, **kwargs):
        """Overrides the save method to automatically generate a slug based on the title."""

        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        """A string representation of a job post object."""

        return self.title