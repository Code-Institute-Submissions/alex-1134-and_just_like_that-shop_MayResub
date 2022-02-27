from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    read_only = ('grand_total', 'order_total', 'delivery_cost',)  # 'order_number', 'date',

    fields = ('grand_total', 'order_total', 'delivery_cost',  # 'order_number', 'date',
              'full_name', 'phone_number', 'email', 'postcode',
              'country', 'street_address1', 'street_address2',
              'county',)

    display = ('date', 'order_number', 'full_name',
               'order_total', 'delivery_cost', 'grand_total',)
             
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
