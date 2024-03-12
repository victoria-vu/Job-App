from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    """A view function to handle subscription form submission."""

    subscribe_form = SubscribeForm()
    email_error_empty=""

    if request.POST:
        subscribe_form = SubscribeForm(request.POST) # Bind data to the subscribe form
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse("thank_you"))

    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, "subscribe/subscribe.html", context)


def thank_you(request):
    """A view function to render a thank you page after successful subscription."""
    
    context = {}
    return render(request, "subscribe/thank_you.html", context)