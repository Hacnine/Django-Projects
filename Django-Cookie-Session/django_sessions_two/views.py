from django.http import HttpResponse
from django.shortcuts import render


def count_page(request):
    ct = request.session.get('count', 0)
    new_count = ct + 1
    request.session['count'] = new_count
    return render(request, 'page_count.html', {'new_count': new_count})


def set_session(request):

    request.session['name'] = 'Tanvir'
    return render(request, 'set_session_two.html')


def get_session(request):
    # request.session.set_expiry(20)

    if 'name' in request.session:
        name = request.session['name']
        # 5 seconds after data is not modified then session is expired.
        # request.session.modified = True
        return render(request, 'get_session_two.html', {'name': name})
    else:
        return HttpResponse('Your session is expired.')


def del_session(request):
    request.session.flush()  # To delete all cookies
    request.session.clear_expired()  # To clear database

    response = render(request, 'delete_session_two.html')
    return response
