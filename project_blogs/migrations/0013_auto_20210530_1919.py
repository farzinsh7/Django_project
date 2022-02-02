# Generated by Django 3.2.3 on 2021-05-30 14:49

import ckeditor.fields
from django.db import migrations, models
import project_blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0012_auto_20210530_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to=project_blogs.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='blog',
            name='keywords',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='seo_meta',
            field=models.TextField(default='seo meta'),
        ),
        migrations.AddField(
            model_name='blog',
            name='show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug_field',
            field=models.SlugField(default='slug'),
        ),
    ]
