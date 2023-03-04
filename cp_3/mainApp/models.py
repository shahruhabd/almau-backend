from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


