from django.db import models
from accounts.models import User

class TransactionType(models.TextChoices):
    CREDIT = 'credit', 'credit'
    DEBT = 'debt', 'debt'

class TransactionStatus(models.TextChoices):
    FINALIZADO = 'FINALIZADO', 'FINALIZADO'
    EM_PROCESSO = 'EM_PROCESSO', 'EM_PROCESSO'
    PENDENTE = 'PENDENTE', 'PENDENTE'

class TransactionModel(models.Model):
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255, choices=TransactionType.choices)
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(max_length=15, choices=TransactionStatus.choices)
    date_of_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)


