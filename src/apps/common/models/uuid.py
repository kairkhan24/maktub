import uuid

from django.db import models


class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = models.CharField(
        primary_key=True,
        default=lambda: uuid.uuid4().hex,
        editable=False,
        db_index=True,
        max_length=40,
    )
