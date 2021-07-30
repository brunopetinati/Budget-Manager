from rest_framework import serializers
from .models import TransactionModel

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ['id', 'account_owner', 'transaction_type','description', 'amount', 'status', 'date_of_transaction']

        extra_kwargs = {'account_owner':{'read_only':True}, 'status':{'read_only':True}, 'date_of_transaction':{'read_only':True}}

    def create(self, validated_data):
        return TransactionModel.objects.create(**validated_data)
