# Generated by Django 3.2.6 on 2021-08-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210826_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]