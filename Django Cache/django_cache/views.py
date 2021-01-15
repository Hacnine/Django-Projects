from django.shortcuts import render
from django.views.decorators.cache import cache_page


# to activate per site cache uncomment middleware
def per_site_caching(request):
    return render(request, 'home.html')


@cache_page(10)
def per_view_caching(request):
    return render(request, 'per_view_caching.html')


def specific_part_cache(request):
    return render(request, 'per_view_caching.html')


def template_fragment_cache(request):
    return render(request, 'template_fragment_cache.html')
