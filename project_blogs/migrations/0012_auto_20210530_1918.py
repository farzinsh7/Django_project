# Generated by Django 3.2.3 on 2021-05-30 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0011_remove_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='publish_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='seo_meta',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='show',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug_field',
        ),
    ]