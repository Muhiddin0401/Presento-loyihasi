from django.db import models

# Create your models here.

class Sms(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    subject = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)
    answered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name