# Generated by Django 4.1.3 on 2022-11-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0003_investment_amount_investment_wallet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='wallet',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
