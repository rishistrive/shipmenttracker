from django.shortcuts import render
from .models import Shipment
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {}
    supplier = request.user.is_supplier
    # breakpoint()
    if not supplier:
        shipments = Shipment.objects.filter(customer = request.user).prefetch_related()
        context['shipments'] = shipments
    else:
        print('supplier')
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        context['shipments'] = shipments
    return render(request, 'shipment/home.html', context)


def about(request):
    return render(request, 'shipment/about.html')