from django.shortcuts import render


def pie_chart(request):
    labels = []
    data = []
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
    else:
        shipments = request.user.supplier.all()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)

    return render(
        request,
        "charts/charts.html",
        {
            "labels": labels,
            "data": data,
        },
    )

