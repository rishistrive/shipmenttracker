from django.shortcuts import render


def info(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = request.user.customer.all()
        context["shipments"] = shipments
        print(shipments)
    else:
        shipments = request.user.supplier.all()
        context["shipments"] = shipments
    return render(request, "info/info.html", context)
