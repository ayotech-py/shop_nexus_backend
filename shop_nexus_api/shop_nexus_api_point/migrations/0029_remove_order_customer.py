# Generated by Django 4.2.2 on 2023-06-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0028_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
