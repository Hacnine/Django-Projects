import json
from .models import *


def cookie_cart(request):

    try:
        cart_cookie = json.loads(request.COOKIES['cart'])

    except:
        cart_cookie = {}

    print('Cart Cookie', cart_cookie)
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
    cart_items = order['get_cart_items']

    for i in cart_cookie:
        try:
            cart_items += cart_cookie[i]['quantity']

            product = Product.objects.get(id=i)
            total = product.price * cart_cookie[i]['quantity']

            order['get_cart_total'] += total
            order['get_cart_items'] = cart_cookie[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image_url,
                },
                'quantity': cart_cookie[i]['quantity'],
                'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True

        except:
            pass

    return {'cart_items': cart_items, 'order': order, 'items': items}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        cookie_data = cookie_cart(request)
        cart_items = cookie_data['cart_items']
        order = cookie_data['order']
        items = cookie_data['items']

    return {'cart_items': cart_items, 'order': order, 'items': items}


