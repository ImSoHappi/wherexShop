from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, unique=True)
    state = models.BooleanField(default = True)

    def __str__(self):
        return self.name

    def get_all_client ():
        return Client.objects.all()

    def get_all_active_client ():
        return Client.objects.filter(state=True)

    def get_client (client):
        return Client.objects.get(pk=client)


class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    def get_all_stock_product ():
        return Product.objects.filter(stock__gt=0)

    def get_all_product ():
        return Product.objects.all()


class Sale(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    iva = models.IntegerField()
    discount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_all_sale ():
        return Sale.objects.all()
    
    def get_client_sales (client):
        return Sale.objects.filter(client=client)

    def get_sale (sale):
        return Sale.objects.get(id=sale)


class SaleDetail(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)

    amount = models.IntegerField()
    products = models.ManyToManyField(Product)
    subtotal = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_sale_detail (sale):
        return SaleDetail.objects.get(sale_id=sale)
