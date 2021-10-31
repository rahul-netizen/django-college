from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import TeacherLoginForm, StudentSearchForm, StudentUpdateForm, StudentAttendenceForm, StudentSubjectForm, StudentMarkForm, StudentModelForm
from .models import Teacher

from student.models import Student, Attendence, Subject, Mark


def teacher_home_view(request):
    if request.session.get('email'):
        return render(request, 'teacher/teacher_navbar.html')
    else:
        return redirect('/teacher/login/')


def teacher_logout_view(request):
    del request.session['email']
    return redirect('/login/')


def teacher_login_view(request):
    my_form = TeacherLoginForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_email = None
    my_pass = None

    if my_form.is_valid():
        my_email = my_form.cleaned_data['t_email']
        my_pass = my_form.cleaned_data['t_pass']

    my_obj = Teacher.objects.filter(t_email=my_email, t_pass=my_pass)

    if len(my_obj) >= 1:
        request.session['email'] = my_email
        return redirect('/teacher/')

    else:
        my_form = TeacherLoginForm()
        if my_form.is_valid():
            my_context['error_msg'] = 'INVALID CREADENTIALS !'
        return render(request, 'teacher/teacher_login.html', my_context)


def student_list_view(request):
    queryset = Student.objects.all()
    my_context = {
        'obj': queryset,
    }

    return render(request, 'teacher/student_list.html', my_context)


def student_detail_view(request, my_id):
    my_obj = get_object_or_404(Student, id=my_id)
    my_context = {
        'obj': my_obj,
    }

    return render(request, 'teacher/student_detail.html', my_context)


def student_search_view(request):
    my_form = StudentSearchForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_name = None
    my_dob = None
    my_email = None
    my_roll = None
    my_course = None

    if my_form.is_valid():
        my_dob = my_form.cleaned_data["dob"]
        my_email = my_form.cleaned_data["email"]
        my_roll = my_form.cleaned_data["roll"]
        my_course = my_form.cleaned_data["course"]
        my_name = my_form.cleaned_data["name"]

    my_obj = Student.objects.filter(
        dob=my_dob, email=my_email, roll=my_roll, course=my_course, name=my_name)

    if len(my_obj) >= 1:
        my_id = my_obj[0].id
        return redirect(f'/teacher/student/{my_id}/detail')

    else:
        my_form = StudentSearchForm()
        if my_form.is_valid():
            my_context['error_msg'] = 'Not found!'
        return render(request, 'teacher/student_search.html', my_context)


def student_update_options_view(request):
    my_form = StudentSearchForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_name = None
    my_dob = None
    my_email = None
    my_roll = None
    my_course = None

    if my_form.is_valid():
        my_dob = my_form.cleaned_data["dob"]
        my_email = my_form.cleaned_data["email"]
        my_roll = my_form.cleaned_data["roll"]
        my_course = my_form.cleaned_data["course"]
        my_name = my_form.cleaned_data["name"]

    my_obj = Student.objects.filter(
        dob=my_dob, email=my_email, roll=my_roll, course=my_course)

    #request.session['my_dob'] = my_obj[0].dob
    request.session['my_email'] = my_email
    request.session['my_roll'] = my_roll
    #request.session['my_course'] = my_course
    request.session['my_name'] = my_name

    if len(my_obj) >= 1:
        return render(request, 'teacher/student_update_options.html', my_context)

    else:
        if my_form.is_valid():
            my_form = StudentSearchForm()
            my_context = {
                'error_msg': 'Student Not Found!',
            }
        return render(request, 'teacher/student_update.html', my_context)


def student_detail_update_view(request):
    my_form = StudentUpdateForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    new_my_name = None
    new_my_email = None
    new_my_roll = None
    new_my_course = None
    new_my_dob = None
    my_obj = None

    my_email = request.session.get('my_email')
    my_roll = request.session.get('my_roll')
    my_name = request.session.get('my_name')

    if my_form.is_valid():
        new_my_course = my_form.cleaned_data["course"]
        new_my_dob = my_form.cleaned_data["dob"]
        new_my_email = my_form.cleaned_data["email"]
        new_my_roll = my_form.cleaned_data["roll"]
        new_my_name = my_form.cleaned_data["name"]

    my_obj = Student.objects.filter(
        email=my_email, roll=my_roll, name=my_name)

    if my_obj:
        if my_form.is_valid():
            my_obj = Student.objects.filter(email=my_email, roll=my_roll, name=my_name).update(
                email=new_my_email, roll=new_my_roll, name=new_my_name, course=new_my_course, dob=new_my_dob)
            my_context['success_msg'] = 'Details Updated! '
        return render(request, 'teacher/student_detail_update.html', my_context)

    else:

        return render(request, 'teacher/student_update.html', my_context)


def student_attendence_update_view(request):
    my_form = StudentAttendenceForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_email = request.session.get('my_email')
    my_roll = request.session.get('my_roll')
    my_name = request.session.get('my_name')

    new_my_month = None
    new_my_attend_count = None
    my_attend_obj = None

    if my_form.is_valid():
        new_my_month = my_form.cleaned_data["month"]
        new_my_attend_count = my_form.cleaned_data["attend_count"]

        my_attend_obj = Attendence.objects.create(
            month=new_my_month, attend_count=new_my_attend_count)
        my_attend_obj.save()

    if my_attend_obj:
        if my_form.is_valid():
            my_obj = Student.objects.filter(
                email=my_email, roll=my_roll, name=my_name).update(attendence=my_attend_obj)
            my_context['success_msg'] = 'Details Updated! '
        return render(request, 'teacher/student_attendence_update.html', my_context)

    else:

        return render(request, 'teacher/student_update.html', my_context)


def student_subject_update_view(request):
    my_form = StudentSubjectForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_email = request.session.get('my_email')
    my_roll = request.session.get('my_roll')
    my_name = request.session.get('my_name')

    new_sub_1 = None
    new_sub_2 = None
    new_sub_3 = None
    new_sub_4 = None
    my_sub_obj = None

    if my_form.is_valid():
        new_sub_1 = my_form.cleaned_data["sub_1"]
        new_sub_2 = my_form.cleaned_data["sub_2"]
        new_sub_3 = my_form.cleaned_data["sub_3"]
        new_sub_4 = my_form.cleaned_data["sub_4"]

        my_sub_obj = Subject.objects.create(
            sub_1=new_sub_1, sub_2=new_sub_2, sub_3=new_sub_3, sub_4=new_sub_4)
        my_sub_obj.save()

    if my_sub_obj:
        if my_form.is_valid():
            my_obj = Student.objects.filter(
                email=my_email, roll=my_roll, name=my_name).update(subject=my_sub_obj)
            my_context['success_msg'] = 'Details Updated! '
        return render(request, 'teacher/student_subject_update.html', my_context)

    else:

        return render(request, 'teacher/student_update.html', my_context)


def student_mark_update_view(request):
    my_form = StudentMarkForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_email = request.session.get('my_email')
    my_roll = request.session.get('my_roll')
    my_name = request.session.get('my_name')

    new_marks_1 = None
    new_marks_2 = None
    new_marks_3 = None
    new_marks_4 = None
    my_marks_obj = None

    if my_form.is_valid():
        new_marks_1 = my_form.cleaned_data["marks_1"]
        new_marks_2 = my_form.cleaned_data["marks_2"]
        new_marks_3 = my_form.cleaned_data["marks_3"]
        new_marks_4 = my_form.cleaned_data["marks_4"]

        my_marks_obj = Mark.objects.create(
            marks_1=new_marks_1, marks_2=new_marks_2, marks_3=new_marks_3, marks_4=new_marks_4)
        my_marks_obj.save()

    if my_marks_obj:
        if my_form.is_valid():
            my_obj = Student.objects.filter(
                email=my_email, roll=my_roll, name=my_name).update(mark=my_marks_obj)

            my_context['success_msg'] = 'Details Updated! '

        return render(request, 'teacher/student_marks_update.html', my_context)

    else:

        return render(request, 'teacher/student_update.html', my_context)


def student_create_view(request):
    my_form = StudentModelForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()
        my_form = StudentModelForm()

    my_context = {
        'form': my_form,
    }

    return render(request, 'teacher/student_create.html', my_context)
