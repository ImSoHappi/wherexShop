import uuid
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Client, Sale, SaleDetail
import ast

def home(request):

    if request.method == "POST":
        try:
            saleResume = ast.literal_eval(request.POST['sale'])
            client = get_object_or_404(Client, id=request.POST['client'])
            subtotal = request.POST['subtotal'] 
            discount = request.POST['discount'] 
            iva = request.POST['iva'] 
            total = request.POST['total']

            sale = Sale.objects.create(client=client, iva=iva, discount=discount, total=total)
            sale.save()

            resume = SaleDetail.objects.create(sale_id=sale, amount=2, subtotal=subtotal)
            resume.save()

            for item in saleResume:
                resume.products.add(item['id'])    

        except:
            print("fail")

    context = {}
    context['products'] = Product.get_all_stock_product()
    context['active_clients'] = Client.get_all_active_client()
    
    return render(request, 'home.html', context=context)


def clientList(request):

    context = {}
    context['clients'] = Client.get_all_client()

    return render(request, 'client_list.html', context=context)

def productList(request):

    context = {}
    context['products'] = Product.get_all_product()

    return render(request, 'product_list.html', context=context)

def saleList(request):

    context = {}
    context['sales'] = Sale.get_all_sale()

    return render(request, 'sale_list.html', context=context)

def clientSaleList (request, client):
    context = {}
    context['sales'] = Sale.get_client_sales(client)
    context['client'] = Client.get_client(client)
    return render(request, 'sale_list.html', context=context)

def saleDetail (request, sale):
    
    if request.method == "POST":
        deleteSale = get_object_or_404(Sale, id=sale)
        deleteSale.delete()
        return redirect('sales')

    context = {}
    context['detail'] = SaleDetail.get_sale_detail(sale)
    context['sale'] = Sale.get_sale(sale)
    return render(request, 'sale_detail.html', context=context)

def productEdit (request, product):

    if request.method == "POST":
        if 'delete_product' in request.POST:
            deleteProduct = get_object_or_404(Product, id=product)
            deleteProduct.delete()
            return redirect('products')

        if 'update_product' in request.POST:
            updateProduct = get_object_or_404(Product, id=product)
            updateProduct.name = request.POST['name']
            updateProduct.price = request.POST['price']
            updateProduct.stock = request.POST['stock']
            updateProduct.save()
            return redirect('product_edit', product=product)

    context = {}
    context['product'] = Product.get_product(product)
    return render(request, 'edit_product.html', context=context)


def clientEdit (request, client):

    if request.method == "POST":
        if 'delete_client' in request.POST:
            deleteCliente = get_object_or_404(Client, id=client)
            deleteCliente.delete()
            return redirect('clients')

        if 'update_client' in request.POST:
            updateClient = get_object_or_404(Client, id=client)
            updateClient.name = request.POST['name']

            if 'state' in request.POST:
                state = True
                print("True")
            else:
                state = False
                print("False")

            updateClient.state = state
            updateClient.save()
            return redirect('client_edit', client=client)

    context = {}
    context['client'] = Client.get_client(client)
    return render(request, 'edit_client.html', context=context)


def addProduct (request):

    if request.method == "POST":

        product = Product.objects.create(name=request.POST['name'], price=request.POST['price'], stock=request.POST['stock'])
        product.save()
        return redirect('products')

    return render(request, 'add_product.html')


def addClient (request):

    if request.method == "POST":
        
        if 'state' in request.POST:
            state = True
        else:
            state = False

        client = Client.objects.create(name=request.POST['name'], state=state)
        client.save()

        return redirect('clients')

    return render(request, 'add_client.html')