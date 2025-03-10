# Generated by Django 5.1.6 on 2025-03-07 13:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(upload_to='ads/'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
