# Generated by Django 3.2.3 on 2021-05-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0023_alter_blogs_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='category',
        ),
    ]
