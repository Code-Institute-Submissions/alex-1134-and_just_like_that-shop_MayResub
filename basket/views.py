from django.shortcuts import render

def basket(request):
    """ View to see basket """

    return render(request, 'basket/basket.html')