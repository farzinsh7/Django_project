# Generated by Django 3.2.3 on 2021-05-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blogs', '0031_blogs_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('published_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
