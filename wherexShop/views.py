import uuid
from django.shortcuts import render, get_object_or_404
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
