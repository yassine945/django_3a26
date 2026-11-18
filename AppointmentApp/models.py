from django.db import models

Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(blank=True,upload_to='prescriptions/')
class Status(models.TextChoices):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    #status = models.CharField(max_length=10, choices=[(PENDING = 'Pending'),(CONFIRMED = 'Confirmed'),(CANCELLED = 'Cancelled')], default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey('accountApp.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('accountApp.Patient', on_delete=models.CASCADE, related_name='appointments')