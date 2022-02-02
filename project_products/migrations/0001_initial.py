# Generated by Django 3.2.3 on 2021-05-21 11:46

from django.db import migrations, models
import project_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to=project_products.models.upload_image_path)),
                ('price', models.IntegerField(default=0)),
                ('publish_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]