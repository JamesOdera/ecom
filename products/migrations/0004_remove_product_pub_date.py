# Generated by Django 3.0.4 on 2020-04-02 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
    ]
