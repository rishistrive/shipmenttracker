from django.shortcuts import render
from django.db.models import Avg

from shipment.models import Shipment



def stats(request):
    labels = []
    data = []
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all().select_related('product_name')
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
        avg=Shipment.objects.aggregate(Avg('order_amount'))
    else:
        shipments = request.user.supplier.all().select_related('product_name')
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)
        avg=Shipment.objects.aggregate(Avg('order_amount'))
    return render(
        request,
        "stats/stats.html",
        {"labels": labels, "data": data, "average_amount": avg.get('order_amount__avg')},
    )
