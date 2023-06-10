from django.urls import path

from orders.views import OrdersPageView

urlpatterns = [
    path('',  OrdersPageView.as_view(), name='orders')
]