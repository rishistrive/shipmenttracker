from django.shortcuts import render
from shipment.models import Shipment



def stats(request):
    labels = []
    data = []
<<<<<<< HEAD
    average_amount = 0
    prices = 0
    supplier = request.user.is_supplier
    if not supplier:
        shipments = request.user.customer.all()
=======
    prices = 0
    supplier = request.user.is_supplier
    if not supplier:
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.quantity)
            prices += shipment.order_amount
<<<<<<< HEAD
            if prices > 0 and shipment_count:
                average_amount = prices / shipment_count
    else:
        shipments = request.user.supplier.all()
=======
        average_amount = prices / shipment_count
        return render(
            request,
            "stats/stats.html",
            {"labels": labels, "data": data, "average_amount": average_amount},
        )
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
        shipment_count = shipments.count()
        for shipment in shipments:
            labels.append(shipment.product_name.name)
            data.append(shipment.order_amount)
            prices += shipment.order_amount
<<<<<<< HEAD
            if prices > 0 and shipment_count:
                average_amount = prices / shipment_count
    return render(
        request,
        "stats/stats.html",
        {"labels": labels, "data": data, "average_amount": average_amount},
    )
=======
            average_amount = prices / shipment_count

        return render(
            request,
            "stats/stats.html",
            {"labels": labels, "data": data, "average_amount": average_amount},
        )
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
