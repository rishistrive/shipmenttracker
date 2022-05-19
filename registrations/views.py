from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            supplier = form.cleaned_data.get("is_supplier")
            if not supplier:
                form.instance.is_customer = True
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"{username} Your account has been created, Now you can login!"
            )
            return redirect("login")

    else:
        form = UserRegistrationForm()
    return render(request, "registrations/register.html", {"form": form})
