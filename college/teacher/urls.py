from django.urls import path
from .views import (
    teacher_login_view,
    teacher_logout_view,
    teacher_home_view,
    student_list_view,
    student_detail_view,
    student_search_view,
    student_update_options_view,
    student_detail_update_view,
    student_attendence_update_view,
    student_subject_update_view,
    student_mark_update_view,
    student_create_view,
)

app_name = 'student'

urlpatterns = [
    path('', teacher_home_view, name='teacher-home'),
    path('login/', teacher_login_view, name='teacher-login'),
    path('logout/', teacher_logout_view, name='teacher-logout'),
    path('studentlist/', student_list_view, name='student-list'),
    path('student/<int:my_id>/detail/', student_detail_view, name='student-detail'),
    path('studentsearch/', student_search_view, name='student-search'),    
    path('studentupdateoptions/', student_update_options_view, name='student-update-options'),    
    path('studentdetailupdate/', student_detail_update_view, name='student-detail-update'),    
    path('studentattendenceupdate/', student_attendence_update_view, name='student-attendence-update'),    
    path('studentsubjectupdate/', student_subject_update_view, name='student-subject-update'),    
    path('studentmarkupdate/', student_mark_update_view, name='student-mark-update'),    
    path('studentcreate/', student_create_view, name='student-create'),    

]


