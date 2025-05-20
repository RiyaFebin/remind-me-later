from django.db import models

class Reminder(models.Model):
    REMIND_CHOICES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    remind_by = models.CharField(max_length=10, choices=REMIND_CHOICES)

    def __str__(self):
        return f"{self.message} @ {self.date} {self.time} via {self.remind_by}"
