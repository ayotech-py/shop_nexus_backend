# Generated by Django 4.2.2 on 2023-06-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0026_remove_payment_orderitem_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
