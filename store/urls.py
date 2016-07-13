from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index),
    url(r'^index/$', view=views.index, name='index'),
    url(r'^product_detail/(?P<id>\d+)', view=views.product_detail, name='product_detail'),
    url(r'^category/(?P<id>\d+)', view=views.category, name='category'),
    url(r'^search/$', view=views.search, name='search'),
]