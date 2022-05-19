from django.shortcuts import render
from shipment.models import Shipment


def pie_chart(request):
    labels = []
    data = [5,6,24,67,98,45]

    shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
    for shipment in shipments:
        labels.append(shipment.product_name.name)
        # data.append(shipment.status)
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
