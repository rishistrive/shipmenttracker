# Generated by Django 4.0.4 on 2022-05-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0008_alter_shipment_customer_alter_shipment_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='widgets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shipment.widgets'),
        ),
    ]