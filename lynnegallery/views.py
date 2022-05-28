from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Pictures, Category,Location

# Create your views here.

def about(request):
    return render(request,'about.html')

def pictures(request):
    try:
        pictures = Pictures.objects.all()
    except Pictures.DoesNotExist:
        raise Http404()
    return render(request,"pictures.html", {"pictures":pictures})
def index(request):
    all_pictures = Pictures.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request,'index.html', {'all_pictures':all_pictures,'location_results':location_results,'category_results':category_results})



def search_results(request):

    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_pictures = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"all_pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Pictures.objects.filter(category = category)
    return render(request,'index.html',{'all_pictures':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request,location):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Pictures.objects.filter(location= location)
    return render(request,'index.html',{'all_pictures':location_result,'category_results':category_results,'location_results':location_results})