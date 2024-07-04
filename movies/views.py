from django.shortcuts import render,get_object_or_404,redirect
from . import models



def movie_list(request,category_slug=None):
    category = None
    categories = models.Category.objects.all()
    movies  = models.Movies.objects.all()
    if category_slug:
        category = get_object_or_404(models.Category,slug=category_slug)
    return render(request,'movie_list.html',{
        'category':category,
        'categories':categories,
        'movies':movies
    })
# Create your views here.
