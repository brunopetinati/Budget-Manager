# Generated by Django 3.2 on 2021-07-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
