# Generated by Django 3.1.7 on 2021-07-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0003_alter_warehouse_grid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='shelves',
        ),
    ]
