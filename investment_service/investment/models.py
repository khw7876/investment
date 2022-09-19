from django.db import models
from user.models import User as UserModel

# Create your models here.
class Bank(models.Model):
    name = models.CharField("증권사 명", max_length=40)

    def __str__(self):
        return self.name

class Investment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_name = models.CharField("계좌명", max_length=40)
    account_num = models.IntegerField("계좌번호")
    starting_fund = models.IntegerField("투자원금", default=0)
    total_asset = models.IntegerField("계좌 총 자산", default=0)

    def __str__(self):
            return self.user, self.account_name

class InvestmentHistory(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_name = models.CharField("계좌명", max_length=40)
    account_num = models.IntegerField("계좌번호")
    starting_fund = models.IntegerField("투자원금", default=0)
    total_asset = models.IntegerField("계좌 총 자산", default=0)
    isin = models.CharField("ISIN", max_length=40)
    cur_price = models.IntegerField("현재가")
    order = models.IntegerField("보유수량")


    def __str__(self):
            return self.account_name, self.cur_price, self.order
