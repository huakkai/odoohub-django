from django.db import models
from simple_history.models import HistoricalRecords


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self._change_reason = 'this is save (UPDATE)'
        super().save(*args, **kwargs)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()
