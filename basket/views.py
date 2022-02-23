from django.shortcuts import render, redirect


def basket(request):
    """ View to see basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add the amount of products to the customer's basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # customer is able to continue shopping without losing their shopping basket content
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
