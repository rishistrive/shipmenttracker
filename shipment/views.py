from genericpath import exists
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from shipment.forms import WidgetsForm

from .models import UserConfig, Widgets


def redirect_to_widget(request, *args, **kwargs):
    widget_id = kwargs.get("widget_id", None)
    if widget_id:
        try:
            widget = Widgets.objects.get(id=widget_id)
            if widget.name == "Chart":
                return redirect(reverse("charts"))
            if widget.name == "Info":
                return redirect(reverse("info"))
            if widget.name == "List":
                return redirect(reverse("lists"))
            if widget.name == "Statistics":
                return redirect(reverse("stats"))
        except:
            return HttpResponse("That widget type doesn't exist.")


@login_required
def config_widget(request):
    if request.method == "POST":
        form = WidgetsForm(data=request.POST)
        user_config = request.user.userwidget.first()
        form = WidgetsForm(request.POST, instance=user_config)
        if form.is_valid():
            form.save()
        return redirect(reverse("home"))
    else:
        all_widgets = request.user.userwidget.values_list('widget__id', flat=True)
        form = WidgetsForm(initial={"user": request.user, "widget": all_widgets})
    return render(request, "shipment/config.html", {"form": form})


@login_required
def dashboard(request):
    context = {}
    user_config = request.user.userwidget.filter(
        widget__name__isnull=False).annotate(
            name=F('widget__name'),
            pk=F('widget__id')
        ).values('name', 'pk')
    context["userwidgets"] = user_config if user_config.exists() else Widgets.objects.filter(name="Chart").values('name', 'pk')
    return render(request, "shipment/home.html", context)


@login_required
def about(request):
    return render(request, "shipment/about.html")
