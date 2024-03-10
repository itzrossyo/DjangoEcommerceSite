from django.urls import path, re_path
from . import views
app_name = "checkout"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('getAddress_ajax', views.getAddress_ajax , name='getAddress_ajax'),
    path('process_order/', views.processOrder, name="process_order"),
  
]