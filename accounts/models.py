import random

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def generate_code():
    return random.randint(100000, 999999)


class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField(default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return self.created_at < timezone.now() - timezone.timedelta(minutes=5)