from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

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
