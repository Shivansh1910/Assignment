# Generated by Django 3.1.4 on 2021-03-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='manager',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]