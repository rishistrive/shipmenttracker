# Generated by Django 4.0.4 on 2022-05-17 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0009_alter_user_widgets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='widgets',
        ),
        migrations.DeleteModel(
            name='Widgets',
        ),
    ]
