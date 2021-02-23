from datetime import datetime, timedelta
import stripe
from django.shortcuts import render, redirect
from accounts.models import Course, CourseModule, Profile


def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)


def view_course(request, slug):
    course = Course.objects.filter(slug=slug).first()
    course_module = CourseModule.objects.filter(course=course)

    context = {'course': course, 'course_module': course_module}
    return render(request, 'course.html', context)


def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership', 'MONTHLY')
        amount = 1000
        if membership == 'YEARLY':
            amount = 12000

            #
            stripe.api_key = 'sk_test_51ILs3ZHwMcJPanXfyNKqB9d6F9xaK9B119Np60ggUc8PLqHN12m6XPAgKaufnIgISHyEGpyA0ThNKN2daYDJp6Kx00dpeRhJ0c'
            customer = stripe.Customer.create(
                email=request.POST['email'],
                # name=request.POST['nickname'],
                source=request.POST['stripeToken']
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=amount * 100,
                currency='usd',
                description='Membership'
            )
            if charge['paid']:
                profile = Profile.objects.filter(user=request.user).first()
                if charge['amount'] == 100000:
                    profile.subscription_type = 'M'
                    profile.is_pro = True
                    expiry = datetime.now() + timedelta(30)
                    profile.pro_expiry_date = expiry
                    profile.save()

                elif charge['amount'] == 1100000:
                    profile.subscription_type = 'Y'
                    profile.is_pro = True
                    expiry = datetime.now() + timedelta(30)
                    profile.pro_expiry_date = expiry
                    profile.save()

            return redirect('/success/')

        # 4242424242424242
    context = {}
    return render(request, 'become_pro.html', context)


def success(request):
    return render(request, success.html)