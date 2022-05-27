from django.urls import re_path as url
from . import views


urlpatterns=[
    
    url(r'^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^pictures/',views.pictures,name ='pictures')
    
]