# Generated by Django 3.2.3 on 2021-05-30 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0025_blogs_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
    ]
