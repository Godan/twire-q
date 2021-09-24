from base.models import BaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class Question(BaseModel):

    class Meta:
        verbose_name = _("自由記述式アンケート")
        verbose_name_plural = _("自由記述式アンケート")

    question_text = models.TextField(_("質問"), max_length=500)
    hashtag = models.CharField(_("ハッシュタグ"), max_length=100, null=False, blank=False)
    aggregate_start_time = models.DateTimeField(_("集計開始時間"), null=True, blank=True, default=None) 
    aggregate_end_time = models.DateTimeField(_("集計終了"), null=True, blank=True, default=None)

    def start_aggreagate(self) -> None:
        self.aggregate_start_time = datetime.now()
        self.save()