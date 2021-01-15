from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.per_site_caching, name='page'),
    path('per_view_caching', views.per_view_caching, name='per_view_caching'),

    path('i_do_not_want_this_url_to_cache', views.specific_part_cache, name='without_cache'),
    path('specific_part_cache', cache_page(20)(views.specific_part_cache), name='specific_part_cache'),

    path('template_fragment_cache', views.template_fragment_cache, name='template_fragment_cache'),

]
