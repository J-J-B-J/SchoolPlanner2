"""The views for the SchoolPlanners app."""
from django.shortcuts import render, redirect
from django.forms.utils import RenderableMixin

import datetime

from .models import Subject, Event, Homework, Assessment
from .forms import NewSubjectForm, NewHomeworkForm, NewAssessmentForm, \
    NewEventForm, EditSubjectForm, EditHomeworkForm, EditAssessmentForm, \
    EditEventForm


def index(request):
    """The home page for SchoolPlanner."""
    events_count = Event.objects.filter(end__range=(
        datetime.date.today(),
        datetime.date.today() + datetime.timedelta(days=14)
    )).count()

    assessments = Assessment.objects.all()
    homework_ = Homework.objects.all()

    uncompleted_assessments = 0
    for assessment_ in assessments:
        if not assessment_.completed():
            uncompleted_assessments += 1

    uncompleted_homework = homework_.filter(completed=False).count()

    upcoming_assessments = \
        assessments.filter(date__gte=datetime.date.today()).order_by('date')
    upcoming_homework = homework_.filter(due_date__gte=datetime.date.today()) \
        .order_by('due_date')

    context = {
        'upcoming_homework':             upcoming_homework,
        'upcoming_assessments':          upcoming_assessments,
        'homework_uncompleted_count':    uncompleted_homework,
        'assessments_uncompleted_count': uncompleted_assessments,
        'events_count':                  events_count,
    }
    return render(request, 'aa_index.html', context)


def all_subjects(request):
    """The page for subjects."""
    context = {
        'subjects': Subject.objects.order_by('name'),
    }
    return render(request, 'subjects/all.html', context)


def subject(request, subject_id):
    """The page for editing a subject."""
    subject_ = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        # Submit data
        form = EditSubjectForm(request.POST, instance=subject_)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_subjects')
    else:
        # Show form
        form = EditSubjectForm(instance=subject_)
    context = {
        'subject': subject_,
        'form':    form,
    }
    return render(request, 'subjects/one.html', context)


def delete_subject(request, subject_id):
    """The page for deleting a subject."""
    subject_ = Subject.objects.get(id=subject_id)
    subject_.delete()
    return redirect('SchoolPlanners:all_subjects')


def new_subject(request):
    """The page for creating a new subject."""
    if request.method == 'POST':
        # Submit data
        form = NewSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_subjects')
    else:
        # Show form
        form = NewSubjectForm()
    context = {
        'form': form,
    }
    return render(request, 'subjects/new.html', context)


def all_homework(request):
    """The page for homework"""
    if Homework.objects.filter(due_date__lt=datetime.date.today()):
        homework_ = \
            list(Homework.objects.filter(due_date__gte=datetime.date.today()) \
                 .order_by('due_date')) + ['BREAK'] + \
            list(Homework.objects.filter(due_date__lt=datetime.date.today()) \
                 .order_by('due_date').reverse())
    else:
        homework_ = \
            Homework.objects.filter(due_date__gte=datetime.date.today()) \
                .order_by('due_date')
    context = {
        'all_homework': homework_
    }
    return render(request, 'homework/all.html', context)


def homework(request, homework_id):
    """The page for editing a homework."""
    homework_ = Homework.objects.get(id=homework_id)
    if request.method == 'POST':
        # Submit data
        form = EditHomeworkForm(request.POST, instance=homework_)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_homework')
    else:
        # Show form
        form = EditHomeworkForm(instance=homework_)
    context = {
        'homework': homework_,
        'form':     form,
    }
    return render(request, 'homework/one.html', context)


def delete_homework(request, homework_id):
    """The page for deleting homework."""
    homework_ = Homework.objects.get(id=homework_id)
    homework_.delete()
    return redirect('SchoolPlanners:all_homework')


def new_homework(request):
    """The page for creating a new homework."""
    if request.method == 'POST':
        # Submit data
        form = NewHomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_homework')
    else:
        # Show form
        form = NewHomeworkForm()
    context = {
        'form': form,
    }
    return render(request, 'homework/new.html', context)


def all_assessments(request):
    """The page for assessments"""
    if Assessment.objects.filter(date__lt=datetime.date.today()):
        assessments = \
            list(Assessment.objects.filter(date__gte=datetime.date.today()) \
                 .order_by('date')) + ["BREAK"] + \
            list(Assessment.objects.filter(date__lt=datetime.date.today()) \
                 .order_by('date').reverse())
    else:
        assessments = \
            Assessment.objects.filter(date__gte=datetime.date.today()) \
                .order_by('date')
    context = {
        'assessments': assessments
    }
    return render(request, 'assessments/all.html', context)


def assessment(request, assessment_id):
    """The page for editing an assessment."""
    assessment_ = Assessment.objects.get(id=assessment_id)
    if request.method == 'POST':
        # Submit data
        form = EditAssessmentForm(request.POST, instance=assessment_)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_assessments')
    else:
        # Show form
        form = EditAssessmentForm(instance=assessment_)
    context = {
        'assessment': assessment_,
        'form':       form,
    }
    return render(request, 'assessments/one.html', context)


def delete_assessment(request, assessment_id):
    """The page for deleting an assessment."""
    assessment_ = Assessment.objects.get(id=assessment_id)
    assessment_.delete()
    return redirect('SchoolPlanners:all_assessments')


def new_assessment(request):
    """The page for creating a new assessment."""
    if request.method == 'POST':
        # Submit data
        form = NewAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_assessments')
    else:
        # Show form
        form = NewAssessmentForm()

    context = {
        'form': form,
    }
    return render(request, 'assessments/new.html', context)


def all_events(request):
    """The page for events"""
    if Event.objects.filter(end__lt=datetime.date.today()):
        events = list(Event.objects.filter(end__gte=datetime.date.today()) \
                      .order_by('start')) + ["BREAK"] + \
                 list(Event.objects.filter(end__lt=datetime.date.today()) \
                      .order_by('start').reverse())
    else:
        events = Event.objects.filter(end__gte=datetime.date.today()) \
            .order_by('start')
    context = {
        'events': events
    }
    return render(request, 'events/all.html', context)


def delete_event(request, event_id):
    """The page for deleting an event."""
    event_ = Event.objects.get(id=event_id)
    event_.delete()
    return redirect('SchoolPlanners:all_events')


def event(request, event_id):
    """The page for editing an event."""
    event_ = Event.objects.get(id=event_id)
    if request.method == 'POST':
        # Submit data
        form = EditEventForm(request.POST, instance=event_)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_events')
    else:
        # Show form
        form = EditEventForm(instance=event_)
    context = {
        'event': event_,
        'form':  form,
    }
    return render(request, 'events/one.html', context)


def new_event(request):
    """The page for creating a new event."""
    if request.method == 'POST':
        # Submit data
        form = NewEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SchoolPlanners:all_events')
    else:
        # Show form
        form = NewEventForm()
    context = {
        'form': form,
    }
    return render(request, 'events/new.html', context)
