from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, unique=True)
    state = models.BooleanField(default = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    iva = models.IntegerField()
    discount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)


class SaleDetail(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)

    amount = models.IntegerField()
    products = models.ManyToManyField(Product)
    subtotal = models.IntegerField()

    def __str__(self):
        return str(self.id)
