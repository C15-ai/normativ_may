from django.db import models

from common.models import BaseModel

from common.models import DeleteModel


class Fighter(BaseModel , DeleteModel):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    weight_class = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()
    country = models.CharField(max_length=255)
    country_flag = models.ImageField(upload_to='images/',
            null=True,
            blank=True
    )

    image = models.ImageField(upload_to='fighters/',
            null=True,
            blank=True

    )

    video = models.FileField(upload_to='videos/',
            null=True,
            blank=True)

    def __str__(self):
        return self.name

