from django.contrib import admin

from .models import Product, Shipment, User, Widgets


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'is_supplier', 'is_customer']

    class Meta:
        model = User

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Shipment)
admin.site.register(Widgets)
