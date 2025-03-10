# Generated by Django 5.1.6 on 2025-03-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads/', verbose_name='广告图片')),
                ('location', models.CharField(choices=[('home', '首页'), ('sidebar', '侧边栏'), ('footer', '底部')], default='home', max_length=100, verbose_name='广告位置')),
            ],
        ),
    ]
