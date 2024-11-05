# Generated by Django 5.0.7 on 2024-07-30 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.company'),
            preserve_default=False,
        ),
    ]
