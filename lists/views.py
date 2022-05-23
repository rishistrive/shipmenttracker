from django.shortcuts import render


def lists(request):
    context = {}
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all()
    else:
        shipments = request.user.supplier.all()
    context["shipments"] = shipments
    return render(request, "lists/lists.html", context)
