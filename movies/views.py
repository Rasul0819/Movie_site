from django.shortcuts import render,get_object_or_404,redirect
from . import models
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout
from . import forms
from django.urls import reverse_lazy

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


class SingInClass(LoginView):
    authentication_form = forms.SignInForm
    template_name='sign_in.html'
    # success_url=reverse_lazy('movie_list')
    
    # def get_success_url(self):
    #     return reverse_lazy('movie_list')


def registration(reqeust):
    if reqeust.method =='POST':
        form = forms.SingUpForm(reqeust.POST)
        if form.is_valid():
            user = form.save()
            login(reqeust,user)
            return redirect('movie_list')
    else:
        form = forms.SingUpForm()
    return render(reqeust,'sign_up.html',{'form':form})


def log_out(request):
    logout(request)
    return redirect('movie_list')

def post_detail(request,id):
    movie = get_object_or_404(models.Movies,id=id)
    comments = models.Comment.objects.all()
    if  request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.author = request.user
            new_comment.save()
            return redirect('detail',id=movie.id)
    else:
        comment_form = forms.CommentForm()
    return render(request,'movie_detail.html',{
        'movie':movie,
        'comments':comments,
        'comment_form':comment_form
        })

