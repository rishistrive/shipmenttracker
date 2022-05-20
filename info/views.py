from django.shortcuts import render
from shipment.models import Shipment

def info(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
<<<<<<< HEAD
        shipments = request.user.customer.all()
        context["shipments"] = shipments
        print(shipments)
    else:
        shipments = request.user.supplier.all()
=======
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        context["shipments"] = shipments
        print(shipments)
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
        context["shipments"] = shipments
    return render(request, "info/info.html", context)
