from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item, Category
from .forms import ItemForm


def all_items(request):

    items = Item.objects.all()
    query = None
    sort = None
    direction = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)   

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Tell us what you're looking for!")
                return redirect(reverse('items'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)


def add_item(request):
    """ Add an item to the Closet """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been added!')
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add')
    else:
        form = ItemForm()
        
    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)