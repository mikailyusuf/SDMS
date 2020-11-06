# Generated by Django 3.0 on 2020-11-06 18:50

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
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math_exan', models.FloatField(null=True)),
                ('math_test', models.FloatField(null=True)),
                ('math_total', models.FloatField(null=True)),
                ('math_grade', models.CharField(max_length=10)),
                ('eng_exan', models.FloatField(null=True)),
                ('eng_test', models.FloatField(null=True)),
                ('eng_total', models.FloatField(null=True)),
                ('eng_grade', models.CharField(max_length=10)),
                ('physics_exan', models.FloatField(null=True)),
                ('physics_test', models.FloatField(null=True)),
                ('physics_total', models.FloatField(null=True)),
                ('physics_grade', models.CharField(max_length=10)),
                ('bio_exan', models.FloatField(null=True)),
                ('bio_test', models.FloatField(null=True)),
                ('bio_total', models.FloatField(null=True)),
                ('bio_grade', models.CharField(max_length=10)),
                ('chem_exan', models.FloatField(null=True)),
                ('chem_test', models.FloatField(null=True)),
                ('chem_total', models.FloatField(null=True)),
                ('chem_grade', models.CharField(max_length=10)),
                ('agric_exan', models.FloatField(null=True)),
                ('agric_test', models.FloatField(null=True)),
                ('agric_total', models.FloatField(null=True)),
                ('agric_grade', models.CharField(max_length=10)),
                ('civic_exan', models.FloatField(null=True)),
                ('civic_test', models.FloatField(null=True)),
                ('civic_total', models.FloatField(null=True)),
                ('civic_grade', models.CharField(max_length=10)),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Students')),
            ],
        ),
    ]
