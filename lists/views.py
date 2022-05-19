from django.shortcuts import render
from shipment.models import Shipment


def lists(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        context["shipments"] = shipments
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        context["shipments"] = shipments

    return render(request, "lists/lists.html", context)
