from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.email


class Teachers(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.email


class Result(models.Model):
    student = models.ForeignKey(Students, null=False, on_delete=models.SET_NULL)

    math_exan = models.FloatField(null=True)
    math_test = models.FloatField(null=True)
    math_total = models.FloatField(null=True)

    eng_exan = models.FloatField(null=True)
    eng_test = models.FloatField(null=True)
    eng_total = models.FloatField(null=True)


    physics_exan = models.FloatField(null=True)
    physics_test = models.FloatField(null=True)
    physics_total = models.FloatField(null=True)

    bio_exan = models.FloatField(null=True)
    bio_test = models.FloatField(null=True)
    bio_total = models.FloatField(null=True)

    chem_exan = models.FloatField(null=True)
    chem_test = models.FloatField(null=True)
    chem_total = models.FloatField(null=True)

    agric_exan = models.FloatField(null=True)
    agric_test = models.FloatField(null=True)
    agric_total = models.FloatField(null=True)

    civic_exan = models.FloatField(null=True)
    civic_test = models.FloatField(null=True)
    civic_total = models.FloatField(null=True)


    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
