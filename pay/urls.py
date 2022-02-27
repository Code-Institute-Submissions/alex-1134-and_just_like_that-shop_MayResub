from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.pay, name='pay'),
    path('pay_done/<order_number>', views.pay_done, name='pay_done'),
    path('cache_pay_data/', views.cache_pay_data, name='cache_pay_data'),
    path('wh/', webhook, name='webhook'),
]