from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('pay_done/<order_number>', views.pay_done, name='pay_done')
]