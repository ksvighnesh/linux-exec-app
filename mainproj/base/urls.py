from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ls',views.ls,name='ls'),
    path('pwd',views.pwd,name='pwd'),
    path('echo',views.echo,name='echo'),
    path('df',views.df,name='df'),
    path('test_fun',views.test_fun,name='t'),
    path('cel_fun',views.cel_fun,name='c'),
#    path('mnfun',views.mnfun,name='mnfun'),
    path('api/commands',views.main,name='main'),
    path('api/commands/<int:id>',views.command_detail,name='command_detail'),
    path('new_f',views.new_feat,name="new_f"),
]
