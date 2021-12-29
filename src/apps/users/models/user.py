from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from apps.common.models import (
    UUIDModel,
    TimeStampModel,
    NotDeletableModel,
    PersonalDataModel
)


class User(UUIDModel,
           TimeStampModel,
           NotDeletableModel,
           PersonalDataModel,
           AbstractUser,
           ):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # objects = UserManager()

    phone_number = PhoneNumberField
