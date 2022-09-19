from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from investment.models import Bank as BankModel
import pandas as pd


# Create your views here.
class InvetmentView(APIView):
    
    def get(self, request):
        data = pd.read_csv('investment_service/investment/account_asset_info_set.csv')
        username_data = data["고객이름"]
        username_list = []
        for username in username_data:
            if not username in username_list:
                username_list.append(username)
        for username in username_list:
            UserModel.objects.get_or_create(username = username)

        bank_data = data["증권사"]
        bank_list = []
        for bank_name in bank_data:
            if not bank_name in bank_list:
                bank_list.append(bank_name)
        for bankname in bank_list:
            BankModel.objects.get_or_create(name=bankname)



        return Response()





