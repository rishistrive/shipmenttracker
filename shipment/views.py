from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
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
        user_exist = request.user.userwidget.exists()
        if user_exist:
            existed_user = UserConfig.objects.get(user=request.user)
            form = WidgetsForm(request.POST, instance=existed_user)
            if form.is_valid():
                form.save()
            return redirect(reverse("home"))
    else:
        all_widgets = request.user.userwidget.values_list('widget__id', flat=True)
        form = WidgetsForm(initial={"user": request.user, "widget": all_widgets})
    return render(request, "shipment/config.html", {"form": form})
=======
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
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7


@login_required
def check_widget(request):
    context = {}
<<<<<<< HEAD
    widgets = []
    user_config = request.user.userwidget.all()
    if user_config.exists():
        widgets = user_config.last().widget.all()
    context["userwidgets"] = widgets or Widgets.objects.filter(name="Chart")
=======
    try:
        userwidgets = UserConfig.objects.get(user=request.user).widget.all()
        context["userwidgets"] = userwidgets
    except:
        defaultwidget = Widgets.objects.get(name="Chart")
        context["defaultwidget"] = defaultwidget
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
    return render(request, "shipment/home.html", context)


@login_required
def about(request):
    return render(request, "shipment/about.html")
