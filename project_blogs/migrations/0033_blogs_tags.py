# Generated by Django 3.2.3 on 2021-05-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0032_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='project_blogs.Tag'),
        ),
    ]
