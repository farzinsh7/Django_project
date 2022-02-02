# Generated by Django 3.2.3 on 2021-05-29 11:09

from django.db import migrations, models
import project_blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(null=True, upload_to=project_blogs.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='blogs',
            name='seo_meta',
            field=models.TextField(default='seo meta'),
        ),
    ]