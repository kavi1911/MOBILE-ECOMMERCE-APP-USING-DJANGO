# Generated by Django 5.1.2 on 2024-10-14 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='transmission_type',
        ),
    ]