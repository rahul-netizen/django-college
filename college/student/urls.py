from django.urls import path

from .views import (

    student_detail_view,
    student_home_view,
    student_login_view,
    student_logout_view,
    student_marks_view,
    student_attendence_view,


)

urlpatterns = [
    path('', student_home_view, name='student-home'),
    path('login/', student_login_view, name='student-login'),
    path('<int:my_id>/detail/', student_detail_view, name='student-detail'),
    path('logout/', student_logout_view, name='student-logout'),
    path('marks/', student_marks_view, name='student-marks'),
    path('attendence/', student_attendence_view, name='student-attendence'),

]
