from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.first_name + "" + self.last_name


class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.email


class Results(models.Model):
    student = models.ForeignKey(Students, null=True, on_delete=models.SET_NULL)

    TERM = (
        ('fist_term', 'FIRST TERM'),
        ('second_term', 'SECOND TERM'),
        ('third_term', 'THIRD TERM'),
        )

    SESSION = (
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
    )
    term = models.CharField(max_length=100, null=True)
    session = models.CharField(max_length=100, null=True)


    math_exam = models.FloatField(null=True)
    math_test = models.FloatField(null=True)
    math_total = models.FloatField(null=True)
    math_grade = models.CharField(max_length=10,null=False)

    eng_exam = models.FloatField(null=True)
    eng_test = models.FloatField(null=True)
    eng_total = models.FloatField(null=True)
    eng_grade = models.CharField(max_length=10,null=False)



    physics_exam = models.FloatField(null=True)
    physics_test = models.FloatField(null=True)
    physics_total = models.FloatField(null=True)
    physics_grade = models.CharField(max_length=10,null=False)


    bio_exam = models.FloatField(null=True)
    bio_test = models.FloatField(null=True)
    bio_total = models.FloatField(null=True)
    bio_grade = models.CharField(max_length=10,null=False)


    chem_exam = models.FloatField(null=True)
    chem_test = models.FloatField(null=True)
    chem_total = models.FloatField(null=True)
    chem_grade = models.CharField(max_length=10,null=False)


    agric_exam = models.FloatField(null=True)
    agric_test = models.FloatField(null=True)
    agric_total = models.FloatField(null=True)
    agric_grade = models.CharField(max_length=10,null=False)


    civic_exam = models.FloatField(null=True)
    civic_test = models.FloatField(null=True)
    civic_total = models.FloatField(null=True)
    civic_grade = models.CharField(max_length=10,null=False)

    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return  self.date_created
