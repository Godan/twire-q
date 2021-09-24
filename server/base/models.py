import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.TextField(_("タスク名"), max_length=500) 
    updated_at = models.DateTimeField(_("更新日時"), auto_now=True, editable=False)
