from django.urls import path
from . import views


urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('login/',views.SingInClass.as_view(),name='login'),
    path('signup/',views.registration,name='signup'),
    path('logout/',views.log_out,name='logout'),
    path('detail/<int:id>',views.post_detail,name='detail'),
    path('category/<str:category_slug>',views.movie_list, name='category')
]