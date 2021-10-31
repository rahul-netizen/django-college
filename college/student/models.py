from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

COURSE_CHOICES = (
    ("bca", "BCA"),
    ("bba", "BBA"),
    ("mba", "MBA"),
    ("mca", "MCA"),
)

MONTH_CHOICES = (
    ("jan", "JANUARY"),
    ("feb", "FEBUARY"),
    ("mar", "MARCH"),
    ("apr", "APRIL"),
    ("may", "MAY"),
    ("jun", "JUNE"),
    ("jul", "JULY"),
    ("aug", "AUGUST"),
    ("sept", "SEPTEMBER"),
    ("oct", "OCTOBER"),
    ("nov", "NOVEMBER"),
    ("dec", "DECEMBER"),
)


class Course(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(
        max_length=10, choices=COURSE_CHOICES, default='BCA', null=True, blank=True)
    semester = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.course_name, self.semester)


class Attendence(models.Model):

    #student = models.ForeignKey(Student, on_delete=models.CASCADE,default=1)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    attend_count = models.IntegerField(
        default=0, validators=[MaxValueValidator(30)])


class Subject(models.Model):
    sub_1 = models.CharField(max_length=50)
    sub_2 = models.CharField(max_length=50)
    sub_3 = models.CharField(max_length=50)
    sub_4 = models.CharField(max_length=50)


class Mark(models.Model):
    marks_1 = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])
    marks_2 = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])
    marks_3 = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])
    marks_4 = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])


class Student(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dob = models.DateField(default='1998-01-01')
    roll = models.IntegerField(validators=[MinValueValidator(1)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    attendence = models.ForeignKey(
        Attendence, on_delete=models.CASCADE, default=1)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, default=1)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "%s %s %s " % (self.name, self.course.course_name, self.course.semester)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
