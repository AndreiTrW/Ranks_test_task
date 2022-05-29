import environ
import stripe
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from items_app.models import Price

env = environ.Env()
environ.Env.read_env()

stripe.api_key = env("STRIPE_SECRET_KEY")
DOMAIN = env('DOMAIN')


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/buy/success/',
            cancel_url=DOMAIN + '/buy/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "checkout/success.html"


class CancelView(TemplateView):
    template_name = "checkout/cancel.html"
