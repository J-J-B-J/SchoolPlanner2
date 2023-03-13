"""Models for the SchoolPlanners app."""
from django.db import models


class Subject(models.Model):
    """Model for a subject."""
    name = models.CharField(max_length=100, default="")
    teacher = models.CharField(max_length=100, default="")
    class_name = models.CharField(max_length=10, default="")
    current_summary = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """Model for an event."""
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="", blank=True, null=True)
    start = models.DateTimeField(default="")
    end = models.DateTimeField(default="")
    location = models.CharField(max_length=100, default="School")

    def __str__(self):
        return self.title


class Homework(models.Model):
    """Model for homework."""
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="", blank=True, null=True)
    due_date = models.DateTimeField(default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Assessment(models.Model):
    """Model for an assessment."""
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="", blank=True, null=True)
    date = models.DateTimeField(default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def completed(self):
        """Get weather or not all subtasks are completed."""
        for subtask in SubTask.objects.filter(assignment=self):
            if not subtask.completed:
                return False
        return True

    def completed_tasks_count(self):
        """Get the number of completed subtasks"""
        return SubTask.objects.filter(assignment=self, completed=True).count()

    def total_tasks_count(self):
        """Get the number of incomplete subtasks"""
        return SubTask.objects.filter(assignment=self).count()


class SubTask(models.Model):
    """Model for a subtask."""
    name = models.CharField(max_length=200, default="")
    assignment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
