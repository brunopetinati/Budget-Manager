# Generated by Django 3.2 on 2021-07-29 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account_owner', models.OneToOneField(null=True, on_delete=django.db.models.fields.CharField, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
