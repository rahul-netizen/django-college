from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# from django.contrib.auth.decorators import login_required
from .forms import StudentLoginForm
from .models import Student, Course
# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def student_home_view(request):
    if request.session.get('roll'):
        return render(request, 'student/student_navbar.html')
    else:
        return redirect('/student/login/')


def student_logout_view(request):
    del request.session['roll']
    del request.session['semester']
    # return redirect('/student/')
    return redirect('/login/')


def student_detail_view(request, my_id):
    my_obj = get_object_or_404(Student, id=my_id)
    my_context = {
        'obj': my_obj,
    }

    return render(request, 'student/student_detail.html', my_context)


def student_login_view(request):
    my_form = StudentLoginForm(request.POST or None)
    my_context = {
        'form': my_form
    }

    my_name = None
    my_email = None
    my_roll = None
    my_semester = None
    my_course = None

    if my_form.is_valid():
        my_email = my_form.cleaned_data["email"]
        my_roll = my_form.cleaned_data["roll"]
        my_course = my_form.cleaned_data["course"]

    my_obj = Student.objects.filter(
        email=my_email, roll=my_roll, course=my_course)

    if len(my_obj) >= 1:
        request.session['roll'] = my_obj[0].roll
        request.session['semester'] = my_obj[0].course.semester
        return redirect('/student/')

    else:
        my_form = StudentLoginForm()
        if my_form.is_valid():
            my_context['error_msg'] = 'INVALID CREADENTIALS !'
        return render(request, 'student/student_login.html', my_context)


def student_marks_view(request):

    my_roll = request.session.get('roll')
    my_semester = request.session.get('semester')
    my_course = get_object_or_404(Course, semester=my_semester)
    my_student = get_object_or_404(Student, roll=my_roll, course=my_course)

    #my_obj = StudentInfo.objects.get(student=my_student)

    mark_1 = my_student.mark.marks_1
    mark_2 = my_student.mark.marks_2
    mark_3 = my_student.mark.marks_3
    mark_4 = my_student.mark.marks_4

    overall_marks = 400
    total_marks = (mark_1 + mark_2 + mark_3 + mark_4)

    my_context = {
        'obj': my_student,
        'sem': my_semester,
        'grandtotal': overall_marks,
        'totalmarks': total_marks,
    }

    return render(request, 'student/student_marks.html', my_context)


def student_attendence_view(request):

    my_roll = request.session.get('roll')
    my_semester = request.session.get('semester')
    my_course = get_object_or_404(Course, semester=my_semester)
    my_student = get_object_or_404(Student, roll=my_roll, course=my_course)

    my_context = {
        'obj': my_student,
        'sem': my_semester
    }

    return render(request, 'student/student_attendence.html', my_context)
