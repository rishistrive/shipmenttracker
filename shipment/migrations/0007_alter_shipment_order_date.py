# Generated by Django 3.2.7 on 2022-05-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0006_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
