from django.urls import path, re_path
from . import views
app_name = "cart"

urlpatterns = [
 path('cart/', views.cart, name="cart"),
 path('update_item/', views.updateItem, name="update_item"),
]