from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from accounts.decorators import unauthenticated_user, allowed_user, admin_only
from accounts.filters import OrderFilter
from accounts.forms import OrderForm, CreateUserForm, LoginForm, CustomerForm
from accounts.models import Product, Order, Customer


@unauthenticated_user
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # phone_number = form.cleaned_data.get('phone_number')
            #
            # group = Group.objects.get(name='customers')
            # user.groups.add(group)
            #
            # Customer.objects.create(user=user, name=user.username, email=email, phone=phone_number)
            messages.success(request, f'Account is created for {username}')
            return redirect('/')
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def login_page(request):

    forms = LoginForm()
    context = {'forms': forms}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User name or password is not correct')

    return render(request, 'login_page.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customers'])
def user_profile(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    print('orders', orders)
    context = {'orders': orders, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    return render(request, 'user_profile.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customers'])
def account_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'account_settings.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    all_product = Product.objects.all()
    context = {'products': all_product}
    return render(request, 'products.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request, pks):
    customers = Customer.objects.get(id=pks)

    orders = customers.order_set.all()
    order_count = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    print(my_filter.qs)
    context = {'customers': customers, 'orders': orders, 'order_count': order_count,
               'my_filter': my_filter}
    return render(request, 'customer.html', context)

    # # search product
    #    product_data = ''
    #    from_date = ''
    #    to_date = ''
    #
    #    customers_name = ProductForm()
    #    customers_date = DateForm()
    #
    #    if request.method == 'POST':
    #        form2 = DateForm(request.POST)
    #
    #        if form2.is_valid():
    #            from_date = form2.cleaned_data['from_date']
    #            to_date = form2.cleaned_data['to_date']
    #            # print(to_date)
    #
    #    if request.method == 'POST':
    #        form = ProductForm(request.POST)
    #
    #        if form.is_valid():
    #            name = form.cleaned_data['name']
    #            # student_data = Student.objects.filter(pass_date__range=('2020-12-22', '2021-01-09'))
    #            product_data = Product.objects.filter(name__iexact=name) and Product.objects.filter(date_created__range=(from_date, to_date))
    #            # date_field = Product.objects.filter(date_created__range=(from_date, to_date))
    #
    #            # if date_field and date_field is not None:
    #            #     print("none", product_data)
    #
    #
    #    # print(from_date)
    #    context = {'customers': customers, 'orders': orders, 'order_count': order_count,
    #               'customers_name': customers_name, 'customers_date': customers_date, 'product_data': product_data}
    #    return render(request, 'customer.html', context)


def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def create_order(request, pk):
    order_form_set = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer_id = Customer.objects.get(id=pk)

    formset = order_form_set(queryset=Order.objects.none(), instance=customer_id)

    if request.method == 'POST':
        formset = order_form_set(request.POST, instance=customer_id)
        print('formset', formset)

        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset, 'customer': customer_id}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update_order(request, order_id):
    updates = Order.objects.get(pk=order_id)
    form = OrderForm(instance=updates)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updates)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'order_form.html', {'formset': form})


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def delete_data(request, emp_id):
    pi = Order.objects.get(pk=emp_id)
    context = {'item': pi}
    if request.method == 'POST':
        pi.delete()
        return redirect('/')
    return render(request, 'delete.html', context)
