# Generated by Django 3.2.3 on 2021-05-30 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0028_remove_blogs_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
