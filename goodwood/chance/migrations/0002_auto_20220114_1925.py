# Generated by Django 3.2.6 on 2022-01-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chance',
            options={'ordering': ['-created_at', 'number_phone'], 'verbose_name': 'Победитель', 'verbose_name_plural': 'Победители'},
        ),
        migrations.RemoveField(
            model_name='chance',
            name='title',
        ),
        migrations.AddField(
            model_name='chance',
            name='number_phone',
            field=models.CharField(default='', max_length=20, verbose_name='Номер победителя'),
        ),
    ]
