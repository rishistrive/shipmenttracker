# Generated by Django 4.0.4 on 2022-05-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='widgets',
            field=models.ManyToManyField(to='shipment.widgets'),
        ),
    ]