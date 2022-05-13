from django.db import models


class Source(models.Model):
    title = models.CharField(max_length=64)
    url = models.URLField(max_length=64, unique=True)

    def __str__(self):
        return self.title
