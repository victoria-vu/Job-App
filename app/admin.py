from django.contrib import admin
from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "salary")
    list_filter = ("date", "salary", "expiry")
    search_fields = ("title", "description")
    search_help_text = "Write in your query and hit enter"
    fieldsets = (
        ("Basic Information", {
            "fields": ("title", "description")
        }),
        ("More Information", {
            "classes": ("collapse", "wide"),
            "fields": (("expiry", "salary"), "slug")
        }),
    )


# Register your models here.
admin.site.register(JobPost, JobAdmin)