# Generated by Django 3.2.7 on 2022-05-17 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
