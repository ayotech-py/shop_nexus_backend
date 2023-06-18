# Generated by Django 4.2.1 on 2023-06-17 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_nexus_api_point', '0017_rename_orderitem_order_orderitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]