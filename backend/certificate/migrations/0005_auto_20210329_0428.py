# Generated by Django 3.1.4 on 2021-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0004_auto_20210329_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='is_discription',
            field=models.BooleanField(default=False),
        ),
    ]
