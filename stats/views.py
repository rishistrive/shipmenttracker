from django.shortcuts import render
from shipment.models import Shipment


def stats(request):
    labels = []
    data = []
    prices = 0
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
            prices += shipment.order_amount
        average_amount = prices / shipment_count
        return render(
            request,
            "stats/stats.html",
            {"labels": labels, "data": data, "average_amount": average_amount},
        )
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)
            prices += shipment.order_amount
            average_amount = prices / shipment_count

        return render(
            request,
            "stats/stats.html",
            {"labels": labels, "data": data, "average_amount": average_amount},
        )
