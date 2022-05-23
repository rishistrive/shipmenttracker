from django.shortcuts import render


def info(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all()
    else:
        shipments = request.user.supplier.all()
    context["shipments"] = shipments
    return render(request, "info/info.html", context)
