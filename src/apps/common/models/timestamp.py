from django.db import models


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name='Created date',
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated date',
        blank=True,
        auto_now=True,
    )
