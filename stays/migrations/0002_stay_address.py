# Generated by Django 4.0.3 on 2022-04-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='address',
            field=models.CharField(default=0, max_length=400),
        ),
    ]
