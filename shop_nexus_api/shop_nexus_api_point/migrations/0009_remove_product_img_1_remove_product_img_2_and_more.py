# Generated by Django 4.2.1 on 2023-06-12 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0008_alter_product_image_alter_product_img_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_4',
        ),
    ]