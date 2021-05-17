from django.db import models
from django.conf import settings


# Create your models here.
# # user.todo_set은 user.todos로 변경됨
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    