# Generated by Django 3.0.4 on 2021-07-24 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20210724_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='attend_count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='mark',
            name='marks_2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='mark',
            name='marks_3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='mark',
            name='marks_4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
