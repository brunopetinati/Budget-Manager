# Generated by Django 3.2 on 2021-07-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_transactionmodel_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='status',
            field=models.CharField(choices=[('FINALIZADO', 'FINALIZADO'), ('EM_PROCESSO', 'EM_PROCESSO'), ('PENDENTE', 'PENDENTE')], max_length=15),
        ),
    ]