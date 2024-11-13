from django.db import models
from account.models import User, PHONE_REGEX


class Shop(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    address = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=21, unique=True)

    def __str__(self):
        return f'{self.name}'





