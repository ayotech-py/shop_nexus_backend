# Generated by Django 4.2.1 on 2023-06-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_nexus_api_point', '0010_product_img_1_product_img_2_product_img_3_and_more'),
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
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no-product-img.png', upload_to='product_images/'),
        ),
    ]
