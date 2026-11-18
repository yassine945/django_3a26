from django.db import models
from django.contrib.auth.models import AbstractUser

Create your models here.
class User(AbstractUser):
    pass


class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)


class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()


class Speciality(models.Model):
    name = models.CharField(max_length=255)+
    from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

Create your models here.
class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #specialities = models.ManyToManyField("AcountApp.Speciality")
    specialities = models.ManyToManyField('Speciality', related_name='doctors')
number_validator = RegexValidator(regex=r'^\d{8}$', message='Phone number must be 8 digits')

def validate_birth_date(v):
    if v >= timezone.localdate():
        raise ValidationError('Birth date cannot be in the future.')

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctors = models.ManyToManyField(Doctor, related_name='specialities')