from django.db import models


class Teacher(models.Model):
    t_name = models.CharField(max_length=100)
    t_email = models.EmailField(max_length=100,)
    t_pass = models.CharField(max_length=100)
