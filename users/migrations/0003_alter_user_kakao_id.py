# Generated by Django 4.0.3 on 2022-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_first_name_user_nick_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(max_length=20),
        ),
    ]