# Generated by Django 3.0 on 2020-11-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201107_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='math_exan',
            new_name='math_exam',
        ),
        migrations.AlterField(
            model_name='results',
            name='session',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='term',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
