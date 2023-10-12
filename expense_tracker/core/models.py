from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32, blank=True) 
    type = models.CharField(max_length=8,  blank=False)
    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='transactions')
    descripton = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.category} {self.currency.code}  {self.amount}  {self.date} "