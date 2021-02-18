import stripe
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    stripe.api_key = 'sk_test_51ILs3ZHwMcJPanXfAcmA4rP9yQ2XoLUdCC2BRE83GsIQkL76qJ5KOtDFX2SYP1V3sRDK63zHKSnlYN14r7H4g60s008qPt8tjj'
    return render(request, 'index.html')


# 4242424242424242
def charge(request):
    # amount = int(request.POST['amount'])
    amount = int(request.POST['amount'])

    if request.method == 'POST':
        print('Data:', request.POST)

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description='Donation'
        )

    return redirect(reverse('success', args=[amount]))


def success_msg(request, args):
    amount = args
    return render(request, 'success.html', {'amount': amount})
