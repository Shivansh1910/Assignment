# Generated by Django 3.1.4 on 2021-03-27 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=251)),
                ('manager', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('discription', models.CharField(blank=True, max_length=500, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('certificate_name', models.CharField(blank=True, default='test', max_length=50, null=True)),
                ('x', models.IntegerField(default=7)),
                ('y', models.IntegerField(default=15)),
                ('is_discription', models.BooleanField(default=False)),
                ('discription', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCertificate',
            fields=[
                ('email', models.EmailField(blank=True, max_length=251, primary_key=True, serialize=False)),
                ('event1', models.BooleanField(default=False)),
                ('event2', models.BooleanField(default=False)),
                ('event3', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=251, null=True)),
                ('email', models.EmailField(blank=True, max_length=251)),
                ('auth', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=251, null=True)),
                ('email', models.EmailField(blank=True, max_length=251)),
                ('auth', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
