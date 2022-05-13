from django.db import models

from apps.common.models import TimeStampModel, UUIDModel


class Post(
    UUIDModel,
    TimeStampModel
):
    class Meta:
        ordering = ('-id',)

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    is_published = models.BooleanField(default=True)
    viewed = models.IntegerField(default=0)
    author = models.ForeignKey(
        'blog.Author',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    source = models.ForeignKey(
        'blog.Source',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    category = models.ForeignKey(
        'blog.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        'blog.Tag',
        related_name='posts'
    )

    def __str__(self):
        return self.title
