# Generated by Django 3.1.4 on 2021-03-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_remove_concern_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='is_discription',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
