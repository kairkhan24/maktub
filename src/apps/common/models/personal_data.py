from django.db import models


class PersonalDataModel(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        verbose_name='First name',
        max_length=40,
        default=""
    )
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=40,
        default="",
    )
    patronymic = models.CharField(
        verbose_name='Patronymic',
        max_length=40,
        default="",
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return " ".join(
            filter(None, [self.first_name, self.patronymic, self.last_name])
        )
