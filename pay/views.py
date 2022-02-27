from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import NewForm
from basket.contexts import basket_contents

import stripe


def pay(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty :(")
        return redirect(reverse('items'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    new_form = NewForm()

    if not stripe_public_key:
        message.warning(request, 'Stripe public key missing')

    template = 'pay/pay.html'
    context = {
        'new_form': new_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
