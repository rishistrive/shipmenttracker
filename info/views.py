from django.shortcuts import render
from shipment.models import Shipment


def info(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        context["shipments"] = shipments
        print(shipments)
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        context["shipments"] = shipments
    return render(request, "info/info.html", context)
