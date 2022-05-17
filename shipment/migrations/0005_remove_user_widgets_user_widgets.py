# Generated by Django 4.0.4 on 2022-05-17 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0004_alter_widgets_widgets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='widgets',
        ),
        migrations.AddField(
            model_name='user',
            name='widgets',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.PROTECT, to='shipment.widgets'),
        ),
    ]
