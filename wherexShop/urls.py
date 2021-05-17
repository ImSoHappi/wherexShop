from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sql', views.sql, name='sql'),
    path('clients/', views.clientList, name='clients'),
    path('products/', views.productList, name='products'),
    path('sales/', views.saleList, name='sales'),
    path('clients/<str:client>/sales', views.clientSaleList, name="client_sales"),
    path('sales/<str:sale>/detail', views.saleDetail, name="sale_detail"),
    path('products/<str:product>/edit', views.productEdit, name="product_edit"),
    path('products/add_product', views.addProduct, name="add_product"),
    path('clients/add_client', views.addClient, name="add_client"),
    path('clients/<str:client>/edit', views.clientEdit, name="client_edit"),
]