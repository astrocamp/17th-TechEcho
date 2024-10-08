from django.urls import path

from . import views

app_name = "reservations"

url_teacher = [
    path("teacher/", views.teacher_index, name="teacher_index"),
    path("teacher/new/", views.teacher_new, name="teacher_new"),
    path("teacher/<int:id>/edit/", views.teacher_edit, name="teacher_edit"),
    path("teacher/<int:id>/delete/", views.teacher_delete, name="teacher_delete"),
    path("teacher/available/", views.teacher_available, name="teacher_available"),
    path(
        "teacher/calendar_events/<int:teacher_id>/",
        views.calendar_events,
        name="calendar_events",
    ),
    path("teacher/update_event/", views.update_event, name="update_event"),
]

url_student = [
    path("student/", views.student_index, name="student_index"),
    path("student/<int:id>/new/", views.student_new, name="student_new"),
    path("student/<int:id>/edit/", views.student_edit, name="student_edit"),
    path("student/<int:id>/delete/", views.student_delete, name="student_delete"),
]

urlpatterns = url_teacher + url_student
