from rest_framework import serializers
from investment.models import InvestmentHistory

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestmentHistory
        fields = ["id", "user", "bank", "account_name", "account_num", "total_asset"]