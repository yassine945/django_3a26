from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Status(models.TextChoices):
    PENDING = 'Pending', 'En attente'
    CONFIRMED = 'Confirmed', 'Confirmé'
    CANCELLED = 'Cancelled', 'Annulé'


class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(upload_to='prescriptions/', blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(
        'accountApp.Doctor',
        on_delete=models.CASCADE,
        related_name='appointments',
    )
    patient = models.ForeignKey(
        'accountApp.Patient',
        on_delete=models.CASCADE,
        related_name='appointments',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.appointment_date is not None and self.appointment_date <= timezone.now():
            raise ValidationError('La date du rendez-vous doit être dans le futur.')

    class Meta:
        ordering = ['appointment_date']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unique_patient_doctor_date',
                violation_error_message='Ce docteur possède déjà un rendez-vous à cette date.',
            ),
        ]

    def __str__(self):
        return f"Rendez-vous du {self.reason}"