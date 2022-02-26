from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import NewForm

def pay(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty :(")
        return redirect(reverse('items'))

    new_form = NewForm()
    template = 'pay/pay.html'
    context = {
        'new_form': new_form,
    }

    return render(request, template, context)
