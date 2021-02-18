from django.shortcuts import render
from shopping_cart.models import Order

from accounts.models import Profile


def user_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    user_orders = Order.objets.filter(is_ordered=True, owner=my_user_profile)
    context = {'user_orders': user_orders}
    return render(request, 'home.html', context)
