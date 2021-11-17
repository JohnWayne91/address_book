# Generated by Django 3.2.9 on 2021-11-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211117_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='street',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]