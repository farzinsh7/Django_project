# Generated by Django 3.2.3 on 2021-05-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
