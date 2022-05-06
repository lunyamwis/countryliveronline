from django.db import models

from base.models import BaseModel

# Create your models here.


class Client(BaseModel):
    name = models.CharField(max_length=1024, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    phone_numbers = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
