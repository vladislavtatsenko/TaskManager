from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    status_choices = [
        ('В роботі', 'В роботі'),
        ('Завершено', 'Завершено'),
        ('Відкладено', 'Відкладено'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='В роботі')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
