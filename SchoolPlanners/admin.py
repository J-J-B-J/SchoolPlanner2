from django.contrib import admin

from .models import Subject, Event, Homework, Assessment, SubTask

admin.site.register(Subject)
admin.site.register(Event)
admin.site.register(Homework)
admin.site.register(Assessment)
admin.site.register(SubTask)
