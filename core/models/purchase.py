from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} purchased {self.item.name}"

