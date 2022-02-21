from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item



def all_items(request):

    items = Item.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Tell us what you're looking for!")
                return redirect(reverse('items'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)
