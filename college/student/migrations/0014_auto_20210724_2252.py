# Generated by Django 3.0.4 on 2021-07-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_student_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mark',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Mark'),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Subject'),
        ),
    ]
