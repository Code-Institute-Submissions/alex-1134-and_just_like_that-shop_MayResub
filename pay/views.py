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
        'stripe_public_key': 'pk_test_51KXZnYAR7anLVzL844SdsfnDoxv9P3fNC3HRXxCaeHbh2wWUn3MhRBcmQnqwie5rkB8LPoongq9JUnVyBUooFSjz00rVpwV6vn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
