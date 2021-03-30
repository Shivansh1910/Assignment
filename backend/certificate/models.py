from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.


class Manager(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    urname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=251, null=True, blank=True)
    email = models.EmailField(max_length=251, null=False, blank=True)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Candidate(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    urname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=251, null=True, blank=True)
    email = models.EmailField(max_length=251, null=False, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class UserCertificate(models.Model):
    email = models.EmailField(
        max_length=251, null=False, blank=True, primary_key=True)
    event1 = models.BooleanField(default=False)
    event2 = models.BooleanField(default=False)
    event3 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"


def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.certificate_name, ext)
    # str(instance.certificate_name)
    return '/'.join(['sample', filename])


class Sample(models.Model):
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    # file = models.FileField(blank=True, null=True)
    certificate_name = models.CharField(
        max_length=50, default='test', null=True, blank=True)
    x = models.IntegerField(default=7)
    y = models.IntegerField(default=15)
    is_discription = models.BooleanField(default=False)
    begin = models.CharField(
        max_length=100, null=True, blank=True, default="")
    discription = models.CharField(
        max_length=100, null=True, blank=True, default="")
    discription1 = models.CharField(
        max_length=100, null=True, blank=True, default="")
    discription2 = models.CharField(
        max_length=100, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.certificate_name}"


class Concern(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=251, null=False, blank=True)
    manager = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    discription = models.CharField(max_length=500, null=True, blank=True)
    # complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


# class Certificate(models.Model):
#     certi1 = models.CharField(max_length=50, null=True, blank=True)
#     temp1 = models.ImageField(null=True, blank=True)
#     x1 = models.FloatField(default=7, decimal_places=2)
#     y1 = models.FloatField(default=15, decimal_places=2)
#     certi2 = models.CharField(max_length=50, null=True, blank=True)
#     temp2 = models.ImageField(null=True, blank=True)
#     discription = models.CharField(max_length=100, null=True, blank=True)
#     certi3 = models.CharField(max_length=50, null=True, blank=True)
#     temp3 = models.ImageField(null=True, blank=True)
#     x3 = models.FloatField(default=7, decimal_places=2)
#     y3 = models.FloatField(default=15, decimal_places=2)
