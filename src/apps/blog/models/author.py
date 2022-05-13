from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='authors/')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
