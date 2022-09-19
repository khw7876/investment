from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField("증권사 명", max_length=40)

    def __str__(self):
        return self.name
