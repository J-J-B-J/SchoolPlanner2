"""SchoolPlanners URL Configuration"""

from django.urls import path

from . import views

app_name = 'SchoolPlanners'
urlpatterns = [
    path('', views.index, name='index'),

    # Subjects
    path('subjects/', views.all_subjects, name='all_subjects'),
    path('subjects/<int:subject_id>/', views.subject, name='subject'),
    path('subjects/<int:subject_id>/delete', views.delete_subject,
         name='delete_subject'),
    path('subjects/new/', views.new_subject, name='new_subject'),

    # Homework
    path('homework/', views.all_homework, name='all_homework'),
    path('homework/<int:homework_id>/', views.homework, name='homework'),
    path('homework/<int:homework_id>/delete', views.delete_homework,
         name='delete_homework'),
    path('homework/new/', views.new_homework, name='new_homework'),

    # Assessments
    path('assessments/', views.all_assessments, name='all_assessments'),
    path('assessments/<int:assessment_id>/', views.assessment,
         name='assessment'),
    path('assessments/<int:assessment_id>/delete', views.delete_assessment,
         name='delete_assessment'),
    path('assessments/new/', views.new_assessment, name='new_assessment'),

    # Events
    path('events/', views.all_events, name='all_events'),
    path('events/<int:event_id>/', views.event, name='event'),
    path('events/<int:event_id>/delete', views.delete_event,
         name='delete_event'),
    path('events/new/', views.new_event, name='new_event'),
]
