from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def set_session(request):
    request.session['name'] = 'Tanvir'
    request.session['last_name'] = 'Azam'
    return render(request, 'set_session.html')


def get_session(request):
    sess = request.session
    # sess.set_expiry(60)
    sess.set_expiry(2)

    name = request.session.get('name', default="Guest")
    last_name = request.session.get('last_name', default="Guest")
    age = sess.setdefault('age', '26')
    items = request.session.items()
    name = request.get_signed_cookie('name', default='Salt value is not matched.Please check salt value.', salt='nmm')
    return render(request, 'get_session.html', {'name': name, 'last_name': last_name, 'items': items, 'age': age})

    # if 'name' in request.session:
    #     name = request.session['name']
    #     return render(request, 'get_session_two.html', {'name': name})
    # else:
    #     return HttpResponse('Your session is expired.')


def del_session(request):
    request.session.flush()  # To delete all cookies
    request.session.clear_expired()  # To clear database

    # if 'name' in request.session:
    #     del request.session['name']
    response = render(request, 'delete_session.html')
    return response


def set_test_cookie(request):
    sess = request.session
    sess.set_test_cookie()
    return render(request, 'test_cookie/set_test_cookie.html', )


def check_test_cookie(request):
    sess = request.session
    sess.set_test_cookie()
    print(sess.test_cookie_worked())
    return render(request, 'test_cookie/check_test_cookie.html', )


def del_test_cookie(request):
    request.session.delete_test_cookie()
    return render(request, 'test_cookie/del_test_cookie.html')

