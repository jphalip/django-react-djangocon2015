import uuid

from django.db import models
from django.utils import timezone


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    url = models.CharField(max_length=1000)
    is_color = models.BooleanField(default=False)


class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    photo = models.ForeignKey(Photo)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_created']