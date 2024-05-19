from django.urls import path

from product import views



urlpatterns = [
    path('products/', views.get_all_products,name='products'),
    path('products/<str:pk>/', views.get_by_id_products,name='get_by_id_product'),

]