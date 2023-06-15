import stripe
from django.conf import settings
from django.shortcuts import render
from django.template import context
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)

        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    # Получить разрешение
    permission = Permission.objects.get(codename='special_status')

    # Получить пользователя
    u = request.user

    # Добавить в набор разрешений пользователя
    u.user_permissions.add(permission)

    if request.method == 'POST':

        # стоимость берем из скрытой формы data-amount в шаблоне
        amount = int(request.POST['data-amount'])

        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )

        return render(request, 'orders/charge.html')
