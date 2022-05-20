from django.shortcuts import render
from shipment.models import Shipment


def lists(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
<<<<<<< HEAD
        shipments = request.user.customer.all()
        context["shipments"] = shipments
    else:
        shipments = request.user.supplier.all()
=======
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        context["shipments"] = shipments
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
        context["shipments"] = shipments

    return render(request, "lists/lists.html", context)
