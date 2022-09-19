from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from investment.models import (
    Bank as BankModel,
    Investment as InvestmentModel,
    InvestmentHistory as InvestmentHistoryModel
    )
import pandas as pd


# Create your views here.
class InvetmentView(APIView):
    
    def get(self, request):
        data = pd.read_csv('investment_service/account_asset_info_set.csv')
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

        account_name_data = data["계좌명"]
        account_num_data = data["계좌번호"]
        isin_data = data["ISIN"]
        cur_price_data = data["현재가"]
        order_data = data["보유수량"]
        
        for index, account_num in enumerate(account_num_data):
            user = UserModel.objects.get(username=username_data[index])
            bank = BankModel.objects.get(name=bank_data[index])

            InvestmentModel.objects.get_or_create(
                user = user,
                bank = bank,
                account_name = account_name_data[index],
                account_num = account_num
                )
            InvestmentHistoryModel.objects.get_or_create(
                user = user,
                bank = bank,
                account_name = account_name_data[index],
                account_num = account_num,
                isin = isin_data[index],
                cur_price = cur_price_data[index],
                order = order_data[index],
                )

        return Response({"detail" : "데이터를 성공적으로 저장하였습니다."}, status=status.HTTP_200_OK)
        






