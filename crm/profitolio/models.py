from django.db import models

# Create your models here.

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    company_name = models.CharField(max_length=100, null = True)

    stock_symbol = models.CharField(max_length=100, null = True)

    buy_price = models.DecimalField(max_digits = 20, decimal_places = 3, null = True)

    quantity = models.PositiveIntegerField(null = True)

    sell_price = models.DecimalField(max_digits = 20, decimal_places = 3, null = True)

    returns = models.DecimalField(max_digits = 20, decimal_places = 3, null = True, blank = True)

    buy_date = models.CharField(max_length=100, null = True)

    sell_date = models.CharField(max_length=100, null = True)


    def __str__(self):

        return self.company_name + "   " + self.stock_symbol
