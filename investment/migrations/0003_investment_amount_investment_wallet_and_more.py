# Generated by Django 4.1.3 on 2022-11-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_alter_investment_balance_alter_investment_interest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='investment',
            name='wallet',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='wallet_address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]