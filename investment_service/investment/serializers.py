from rest_framework import serializers
from investment.models import InvestmentHistory

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestmentHistory
        fields = ["id", "user", "bank", "account_name", "account_num", "total_asset"]


class DetailInvestmentSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField()
    income_percent = serializers.SerializerMethodField()

    def get_total_income(self, obj):
        return obj.total_asset - obj.starting_fund

    def get_income_percent(self, obj):
        return obj.total_income / (obj.starting_fund * 100)

    class Meta:
        model = InvestmentHistory
        fields = ["id", "user", "bank", "account_name", "account_num", "total_asset",
        "starting_fund", "total_income", "income_percent"]