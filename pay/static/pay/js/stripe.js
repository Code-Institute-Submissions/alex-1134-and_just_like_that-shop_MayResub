var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#FF00FF',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '18px',
        '::placeholder': {
            color: '#A0A0A0'
        }
    },
    invalid: {
        color: '#585858',
        iconColor: '#d#585858'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
