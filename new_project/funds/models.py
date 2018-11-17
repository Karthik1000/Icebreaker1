from django.db import models


class Funding(models.Model):
    campaign_Title = models.ForeignKey('Campaign', on_delete=models.PROTECT)
    amount = models.FloatField()
    name = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True, null=True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)


class Campaign(models.Model):

    campaign_Title = models.CharField(max_length=200)
