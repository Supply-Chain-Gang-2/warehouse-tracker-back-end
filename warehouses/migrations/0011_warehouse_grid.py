# Generated by Django 3.1.7 on 2021-07-19 21:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0010_remove_warehouse_grid'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='grid',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None), size=None), default='baby goats', size=None),
            preserve_default=False,
        ),
    ]
