# Generated by Django 3.0.4 on 2021-07-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_remove_attendence_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='month',
            field=models.CharField(choices=[('jan', 'JANUARY'), ('feb', 'FEBUARY'), ('mar', 'MARCH'), ('apr', 'APRIL'), ('may', 'MAY'), ('jun', 'JUNE'), ('jul', 'JULY'), ('aug', 'AUGUST'), ('sept', 'SEPTEMBER'), ('oct', 'OCTOBER'), ('nov', 'NOVEMBER'), ('dec', 'DECEMBER')], max_length=20),
        ),
    ]
