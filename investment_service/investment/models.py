from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField("증권사 명", max_length=40)

    def __str__(self):
        return self.name

class Investment(models.Model):
    account_name = models.CharField("계좌명", max_length=40)
    account_num = models.IntegerField("계좌번호")
    starting_fund = models.IntegerField("투자원금", default=0)
    total_asset = models.IntegerField("계좌 총 자산", default=0)