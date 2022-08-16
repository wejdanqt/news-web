# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid
from datetime import date
# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from . import validators


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    national_id = models.CharField(max_length=10, validators=[
                                   validators.NationalIdValidator()])
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10, validators=[
        validators.PhoneNumberValidator()])
    date_of_birth = models.DateField(null=True, blank=True)

    def clean(self):
        if self.date_of_birth and self.date_of_birth > date.today():
            raise ValidationError({'date_of_birth':"The date can't be in the feature"})
        return super().clean()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
