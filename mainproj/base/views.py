from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
import subprocess,os
from .models import command
from django.http import JsonResponse
from .serializers import commandSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .tasks import sleepy
from .tasks import sleeps
from time import sleep
import requests

from django.views.generic.list import ListView
from .forms import commandForm
from django.utils import timezone

class commandList(ListView):
    model:command



def index(request):
    return render(request,'main.html')

def channel(request):
    return render(request,'channel.html')


def new_feat(request):
    #task 2
    #celery progress bar
    cmd=""
    n=0
    sleep_dur=0
    response=requests.get('http://127.0.0.1:8000/api/commands').json()
    for i in response:
        cmd=i['cmd']
        n=i['repetition']
        sleep_dur=i['sleep_dur']
    task=sleeps.delay(cmd,n,sleep_dur)
    #return HttpResponse(task)
    return render(request,'track.html',{'task_id': task.task_id})

def normal_fun(request):
    cmd=""
    n=0
    sleep_dur=0
    response=requests.get('http://127.0.0.1:8000/api/commands').json()
    for i in response:
        cmd=i['cmd']
        n=i['repetition']
        sleep_dur=i['sleep_dur']
    abc=normal_exec(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})

def cel_fun(request):
    cmd=""
    n=0
    sleep_dur=0
    response=requests.get('http://127.0.0.1:8000/api/commands').json()
    for i in response:
        cmd=i['cmd']
        n=i['repetition']
        sleep_dur=i['sleep_dur']
    abc=cel_exec(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})



#return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def normal_exec(cmd,n,sleep_dur):
    d=""
    for i in range(n):
        sleep(sleep_dur)
        output=os.popen(cmd)
        d+="\n"+output.read()
    return d

def cel_exec(cmd,n,sleep_dur):
    d=""
    for i in range(n):
        sleepy.delay(sleep_dur)
        output=os.popen(cmd)
        d+="\n"+output.read()
    return d

def task3(request):
    """ return render(request,'task3.html',context={'text':'hello'})"""
    #model forms
    form=commandForm()
    if request.method =='POST':
        form=commandForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'task3.html',context)


#api Methods

@api_view(['GET','POST'])
def main(request):
    if request.method=='GET':
        commands=command.objects.all()
        serializer=commandSerializer(commands,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=commandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #a=serializer.get_attribute
            
            #return HttpResponse(a)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            

@api_view(['GET','PUT','DELETE'])
def command_detail(request,id):
    try:
        commands=command.objects.get(pk=id)
    except command.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=commandSerializer(commands)
        return Response(serializer.data)

    if request.method=='PUT':
        serializer=commandSerializer(commands,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method=='DELETE':
        commands.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def cleared_channel(request):
    return render(request,'channel_2.html')