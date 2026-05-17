from django.db import models

from common.models import BaseModel

from common.models import DeleteModel


class Fighter(BaseModel , DeleteModel):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    weight_class = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()


    def __str__(self):
        return self.name

