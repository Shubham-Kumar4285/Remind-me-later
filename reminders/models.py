from django.db import models
from django.utils import timezone
import datetime

class Reminder(models.Model):
    REMINDER_METHOD_CHOICES = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]

    reminder_date = models.DateField(default=timezone.now)
    reminder_time = models.TimeField(default=datetime.time(10, 0, 0))
    message = models.TextField(max_length=1000) 
    reminder_method = models.CharField(
        max_length=20,
        choices=REMINDER_METHOD_CHOICES,
        default='EMAIL',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.reminder_date} at {self.reminder_time.strftime('%H:%M')} via {self.reminder_method}: {self.message[:50]}"


    class Meta:
        ordering = ['reminder_date', 'reminder_time']