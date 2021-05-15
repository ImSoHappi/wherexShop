from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clientList, name='clients'),
    path('products/', views.productList, name='products'),
    path('sales/', views.saleList, name='sales'),
    path('clients/<str:client>/sales', views.clientSaleList, name="client_sales"),
    path('sales/<str:sale>/detail', views.saleDetail, name="sale_detail"),
]