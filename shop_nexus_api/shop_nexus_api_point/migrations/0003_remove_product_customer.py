# Generated by Django 4.2.1 on 2023-06-10 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0002_seller_product_count_product_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
    ]
