# Generated by Django 3.2.3 on 2021-05-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0027_auto_20210530_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='category',
        ),
    ]
