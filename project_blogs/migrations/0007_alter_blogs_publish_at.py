# Generated by Django 3.2.3 on 2021-05-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0006_alter_blogs_publish_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='publish_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
