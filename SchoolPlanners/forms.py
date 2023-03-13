"""Model Forms"""
from django import forms

from .models import Subject, Homework, Assessment, Event, SubTask


class NewSubjectForm(forms.ModelForm):
    """Form for a subject."""
    class Meta:
        """Metaclass for the form."""
        model = Subject
        fields = ['name', 'teacher', 'class_name']


class NewHomeworkForm(forms.ModelForm):
    """Form for homework."""
    class Meta:
        """Metaclass for the form."""
        model = Homework
        fields = ['title', 'description', 'due_date', 'subject']
        localized_fields = ['due_date']


class NewAssessmentForm(forms.ModelForm):
    """Form for an assessment."""
    class Meta:
        """Metaclass for the form."""
        model = Assessment
        fields = ['title', 'description', 'date', 'subject']
        localized_fields = ['date']


class NewEventForm(forms.ModelForm):
    """Form for an event."""
    class Meta:
        """Metaclass for the form."""
        model = Event
        fields = ['title', 'description', 'start', 'end', 'location']
        localized_fields = ['start', 'end']


class EditSubjectForm(forms.ModelForm):
    """Form for editing a subject."""
    class Meta:
        """Metaclass for the form."""
        model = Subject
        fields = ['name', 'teacher', 'class_name', 'current_summary']


class EditHomeworkForm(forms.ModelForm):
    """Form for editing homework."""
    class Meta:
        """Metaclass for the form."""
        model = Homework
        fields = ['title', 'description', 'due_date', 'subject', 'completed']
        localized_fields = ['due_date']


class EditAssessmentForm(forms.ModelForm):
    """Form for editing an assessment."""
    class Meta:
        """Metaclass for the form."""
        model = Assessment
        fields = ['title', 'description', 'date', 'subject']
        localized_fields = ['date']


class EditEventForm(forms.ModelForm):
    """Form for editing an event."""
    class Meta:
        """Metaclass for the form."""
        model = Event
        fields = ['title', 'description', 'start', 'end', 'location']
        localized_fields = ['start', 'end']
