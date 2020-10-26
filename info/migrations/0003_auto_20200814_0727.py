# Generated by Django 3.1 on 2020-08-14 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_restaurants_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=200, unique=True),
        ),
    ]
