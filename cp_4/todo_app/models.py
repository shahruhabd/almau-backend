from django.db import models


class TodoList(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
