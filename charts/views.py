from django.shortcuts import render
from shipment.models import Shipment


def pie_chart(request):
    labels = []
    data = []
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
        print(data)

        return render(
            request,
            "charts/charts.html",
            {
                "labels": labels,
                "data": data,
            },
        )
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)
        print(data)

        return render(
            request,
            "charts/charts.html",
            {
                "labels": labels,
                "data": data,
            },
        )


def charts(request):
    return render(request, "charts/charts.html")
