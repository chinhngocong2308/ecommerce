# Generated by Django 2.2.14 on 2021-03-28 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
    ]
