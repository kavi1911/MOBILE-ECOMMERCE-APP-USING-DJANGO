# Generated by Django 5.1.2 on 2024-10-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_rename_operating_system_product_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
