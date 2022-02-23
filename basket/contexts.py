from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
        }

    return context
