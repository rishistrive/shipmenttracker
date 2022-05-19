from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserConfig, Widgets
from django.http import HttpResponse


@login_required
def redirecttowidget(request, *args, **kwargs):
    widget_id = kwargs.get("widget_id")
    if widget_id:
        widget = Widgets.objects.get(id=widget_id)
        if widget.name == "Chart":
            return redirect(reverse("charts"))
        if widget.name == "Info":
            return redirect(reverse("info"))
        if widget.name == "List":
            return redirect(reverse("lists"))
        if widget.name == "Statistics":
            return redirect(reverse("stats"))
    else:
        return HttpResponse("That widget type doesn't exist.")


@login_required
def config_widget(request):
    context = {}
    widgets = Widgets.objects.all()
    context["widgets"] = widgets
    selected_widgets = request.GET.getlist("checkbox-lists")
    var = UserConfig.objects.create(user=request.user)
    var.widget.set(selected_widgets)
    var.save()
    return render(request, "shipment/config.html", context)


@login_required
def check_widget(request):
    context = {}
    try:
        userwidgets = UserConfig.objects.get(user=request.user).widget.all()
        context["userwidgets"] = userwidgets
    except:
        defaultwidget = Widgets.objects.get(name="Chart")
        context["defaultwidget"] = defaultwidget
    return render(request, "shipment/home.html", context)


@login_required
def about(request):
    return render(request, "shipment/about.html")
