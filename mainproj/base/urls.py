from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('normal_fun',views.normal_fun,name='n'),
    path('cel_fun',views.cel_fun,name='c'),
    path('task3',views.task3,name='task3'),
    path('api/commands',views.main,name='main'),
    path('api/commands/<int:id>',views.command_detail,name='command_detail'),
    path('new_f',views.new_feat,name="new_f"),
    path('commands',views.commandList.as_view,name="commands"),

]
