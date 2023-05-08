from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Subscription(models.Model):
    card_number = models.CharField(max_length=16, null=False, default='')
    cardholder_name = models.CharField(max_length=255, null=False, default='')
    card_exp_month = models.CharField(max_length=2, null=False, default='')
    card_exp_year = models.CharField(max_length=2, null=False, default='')
    card_cvv = models.CharField(max_length=3, null=False, default='')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
