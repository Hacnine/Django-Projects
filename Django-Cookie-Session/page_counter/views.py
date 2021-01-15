from django.shortcuts import render


def count_page(request):
    ct = request.session.get('count', 0)
    new_count = ct + 1
    request.session['count'] = new_count
    return render(request, 'page_count.html', {'new_count': new_count})
