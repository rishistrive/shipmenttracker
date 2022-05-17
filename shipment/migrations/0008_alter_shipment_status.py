# Generated by Django 3.2.7 on 2022-05-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0007_alter_shipment_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('Sending', 'sending'), ('Pending', 'Pending'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('In way', 'In way'), ('Arrived Destination', 'Arrived Destination'), ('Received', 'Received')], default='Pending', max_length=20),
        ),
    ]