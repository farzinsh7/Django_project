# Generated by Django 3.2.3 on 2021-05-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_sliders', '0004_alter_slider_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='image',
            new_name='image_slider',
        ),
    ]