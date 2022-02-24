from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    """ View to see basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the amount of products to the customer's basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # customer continues shopping without losing their shopping basket content
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity 

    request.session['basket'] = basket
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


    
def item_removal(request, item_id):
    """Remove item from basket"""
    try: 
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
