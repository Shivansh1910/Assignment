# Generated by Django 3.1.4 on 2021-03-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_auto_20210330_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='begin',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
