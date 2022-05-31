from django.urls import re_path as url
from . import views


urlpatterns=[
    
    url(r'^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^about/', views.about, name='about'),
    url(r'^pictures/',views.pictures,name ='pictures'),
    url(r'^category/(\w+)', views.get_category,name='get_category'),
    url(r'^location/(\w+)', views.get_location,name='get_location'),
    
]