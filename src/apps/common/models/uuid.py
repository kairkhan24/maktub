import uuid

from django.db import models


def generate_uuid():
    return uuid.uuid4().hex


class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = models.CharField(
        primary_key=True,
        default=generate_uuid,
        editable=False,
        db_index=True,
        max_length=40,
    )
