import pandas as pd

from user.models import User as UserModel
from investment.models import (
    Bank as BankModel,
    Investment as InvestmentModel,
    InvestmentHistory as InvestmentHistoryModel,
    AssetGroup as AssetGroupModel,
    Stock as StockModel
    )


# Create your views here.

def make_data():
    # 여기부터는 asset_group_info_set을 정제하는 데이터
    asset_group_data = pd.read_csv('investment_service/asset_group_info_set.csv')
    name_data = asset_group_data["종목명"]
    isin_data = asset_group_data["ISIN"]
    asset_group_name_data = asset_group_data["자산그룹"]
    
    for asset_group_name in asset_group_name_data:
        AssetGroupModel.objects.get_or_create(name = asset_group_name)
    
    for index, name in enumerate(name_data):
        StockModel.objects.get_or_create(name = name, isin = isin_data[index])

    # 여기는 accoutn_accet_info_set.csv 파일을 정제하는 데이터
    account_asset_data = pd.read_csv('investment_service/account_asset_info_set.csv')

    username_data = account_asset_data["고객이름"]
    username_list = []
    for username in username_data:
        if not username in username_list:
            username_list.append(username)
    for username in username_list:
        UserModel.objects.get_or_create(username = username)

    bank_data = account_asset_data["증권사"]
    bank_list = []
    for bank_name in bank_data:
        if not bank_name in bank_list:
            bank_list.append(bank_name)
    for bankname in bank_list:
        BankModel.objects.get_or_create(name=bankname)

    account_name_data = account_asset_data["계좌명"]
    account_num_data = account_asset_data["계좌번호"]
    isin_data = account_asset_data["ISIN"]
    cur_price_data = account_asset_data["현재가"]
    order_data = account_asset_data["보유수량"]
    
    for index, account_num in enumerate(account_num_data):
        user = UserModel.objects.get(username=username_data[index])
        bank = BankModel.objects.get(name=bank_data[index])
        isin = StockModel.objects.get(isin=isin_data[index])
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
            isin = isin,
            cur_price = cur_price_data[index],
            order = order_data[index],
            )
        
    # 여기부터는 account_asset_basic을 정제하는 데이터 
    account_basic_data = pd.read_csv('investment_service/account_basic_info_set.csv')
    account_num_data = account_basic_data["계좌번호"]
    starting_fund_data = account_basic_data["투자원금"]

    for index, account_num in enumerate(account_num_data):
        investment_obj = InvestmentModel.objects.get(account_num = account_num_data[index])
        investment_obj.starting_fund = starting_fund_data[index]
        investment_obj.save()
        

        




