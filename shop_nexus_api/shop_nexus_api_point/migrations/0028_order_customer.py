# Generated by Django 4.2.2 on 2023-06-26 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0027_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_nexus_api_point.customer'),
            preserve_default=False,
        ),
    ]