from django.shortcuts import get_object_or_404
# rest_framework

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# autenticação

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth import authenticate

# models e serializers

from .models import TransactionModel
from .serializers import TransactionSerializer
from accounts.models import User

import ipdb



class TransactionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # criar log dessas informações
        queryset = TransactionModel.objects.filter(account_owner=request.user)
        serializer = TransactionSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        account_owner = request.user
        transaction_status = "EM PROCESSO"
        # status = ['FINALIZADO', 'EM PROCESSO', 'PENDENTE']

        create_transaction = TransactionModel.objects.create(
            account_owner=account_owner,
            transaction_type=request.data['transaction_type'], 
            description=request.data['description'], 
            amount=request.data['amount'], 
            status=transaction_status 
        )

        value = create_transaction.amount 
        
        get_account = get_object_or_404(User, email=account_owner)

        if create_transaction.transaction_type == 'credit':
            result = get_account.wallet + float(create_transaction.amount)
            get_account.wallet = result
            create_transaction.status = "FINALIZADO"
            get_account.save()
        if create_transaction.transaction_type == 'debt':
            if get_account.wallet >= float(create_transaction.amount):
                result = get_account.wallet - float(create_transaction.amount)
                get_account.wallet = result
                create_transaction.status = "FINALIZADO"
                get_account.save()
            else:
                return Response("Não autorizado, verifique seu saldo.", status=status.HTTP_401_UNAUTHORIZED)



        serializer = TransactionSerializer(create_transaction)

        return Response(serializer.data, status=status.HTTP_201_CREATED)