# Generated by Django 5.1.6 on 2025-03-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_created_at_alter_ad_image_alter_ad_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(max_length=255, upload_to='ads/'),
        ),
    ]
