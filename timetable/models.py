from django.db import models


class TimeSlot(models.Model):

    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    time_slot = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.day} - {self.subject}"