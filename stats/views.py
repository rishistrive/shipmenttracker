from django.shortcuts import render


def stats(request):
    labels = []
    data = []
    average_amount = 0
    prices = 0
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all()
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
            prices += shipment.order_amount
            if prices > 0 and shipment_count:
                average_amount = prices / shipment_count
    else:
        shipments = request.user.supplier.all()
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)
            prices += shipment.order_amount
            if prices > 0 and shipment_count:
                average_amount = prices / shipment_count
    return render(
        request,
        "stats/stats.html",
        {"labels": labels, "data": data, "average_amount": average_amount},
    )
