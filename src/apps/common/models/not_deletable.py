from django.db import models


class NotDeletableModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(
        verbose_name='Is deleted?',
        default=False,
        blank=True,
        db_index=True,
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=('is_deleted',))

    def real_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)
