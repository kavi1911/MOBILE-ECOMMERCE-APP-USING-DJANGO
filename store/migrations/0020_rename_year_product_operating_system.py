# Generated by Django 5.1.2 on 2024-10-17 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_model_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='year',
            new_name='Operating_System',
        ),
    ]
