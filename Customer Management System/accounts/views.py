from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import OrderForm
from accounts.models import Product, Order, Customer


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
               'total_customers': total_customers, 'delivered': delivered,
               'pending': pending}
    return render(request, 'dashboard.html', context)


def products(request):
    all_product = Product.objects.all()
    context = {'products': all_product}
    return render(request, 'products.html', context)


def customer(request, pks):
    customers = Customer.objects.get(id=pks)
    orders = customers.order_set.all()
    order_count = orders.count()
    context = {'customers': customers, 'orders': orders, 'order_count': order_count}
    return render(request, 'customer.html', context)


#
#
# def create_update(request, em_id):
#     if request.method == 'POST':
#         updates = User.objects.get(pk=em_id)
#         form = UserRegistration(request.POST, instance=updates)
#         if form.is_valid():
#             form.save()
#     else:
#         updates = User.objects.get(pk=em_id)
#         form = UserRegistration(instance=updates)
#     return render(request, 'update_delete.html', {'forms': form})

def create_order(request):
    form = OrderForm()

    if request.method == 'POST':
        # updates = User.objects.get(pk=order_id)
        # print('Updates:', updates)
        form = OrderForm(request.POST)
        # form = OrderForm(request.POST, instance=updates)

        if form.is_valid():
            form.save()
            return redirect('/')

    # else:
        # updates = User.objects.get(pk=order_id)
        # print('Updates1:', updates)

        # form = OrderForm(instance=updates)
    return render(request, 'order_form.html', {'forms': form})


def update_order(request, order_id):
    updates = Order.objects.get(pk=order_id)
    form = OrderForm(instance=updates)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updates)

        if form.is_valid():
            form.save()
            return redirect('/')

    # else:
    #     updates = User.objects.get(pk=order_id)
    #     print('Updates1:', updates)

        # form = OrderForm(instance=updates)
    return render(request, 'order_form.html', {'forms': form})