# Generated by Django 3.2.3 on 2021-05-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0019_auto_20210530_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug_field',
            field=models.SlugField(default='slug'),
        ),
    ]
