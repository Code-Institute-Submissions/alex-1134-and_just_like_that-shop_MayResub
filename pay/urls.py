from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.pay, name='pay'),
    path('pay_done/<order_number>', views.pay_done, name='pay_done'),
    path('wh/', webhook, name='webhook'),
]