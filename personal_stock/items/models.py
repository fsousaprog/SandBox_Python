from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    avg_price = models.FloatField()


def __str__(self):
    return f"{self.name} Qtd: {self.quantity}"
