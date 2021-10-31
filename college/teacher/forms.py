from django import forms

from .models import Teacher
from student.models import Student, Attendence, Subject, Mark


class TeacherLoginForm(forms.ModelForm):

    t_email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Your Email', 'style': 'width: 300px;'},))
    t_pass = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Your Password'}))
#email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = [
            't_email',
            't_pass'
        ]


class StudentSearchForm(forms.ModelForm):

    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'placeholder': 'Name', },))
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', },))
    roll = forms.CharField(label='Roll Number', widget=forms.TextInput(
        attrs={'placeholder': 'Roll number', },))
    dob = forms.CharField(label='Date of Birth', widget=forms.DateInput(
        attrs={'placeholder': '1998-01-01', },))

    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'dob',
            'roll',
            'course',
        ]


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'email',
            'name',
            'dob',
            'roll',
            'course',
        ]


class StudentAttendenceForm(forms.ModelForm):

    class Meta:
        model = Attendence
        fields = ['month', 'attend_count']


class StudentSubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['sub_1', 'sub_2', 'sub_3', 'sub_4']


class StudentMarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = ['marks_1', 'marks_2', 'marks_3', 'marks_4']


class StudentModelForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Name'}))

    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'dob',
            'roll',
            'course',
            'attendence',
            'mark',
            'subject',
        ]
