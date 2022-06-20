from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import subprocess,os
from .models import command
from django.http import JsonResponse
from .serializers import commandSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .tasks import sleepy
from .tasks import executeCommand
import requests


def index(request):
    return render(request,'main.html')

def test_fun(request):
    cmd=""
    n=0
    sleep_dur=0
    response=requests.get('http://127.0.0.1:8000/api/commands').json()
    for i in response:
        cmd=i['cmd']
        n=i['repetition']
        sleep_dur=i['sleep_dur']
    abc=command1(cmd,n,sleep_dur)
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

def ls(request):
    sleepy.delay(10)
    cmd="ls"
    n=100
    sleep_dur=0
    abc=command1(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})


def cel(request):
    abc=executeCommand.delay()
    return render(request,'home.html',{'abc':abc})


def pwd(request):
    vr=sleepy.delay(5)
    cmd="pwd"
    n=1000    
    sleep_dur=0
    abc=command1(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})

def echo(request):
    sleepy.delay(5)
    cmd="echo hello"
    n=1000    
    sleep_dur=0
    abc=command1(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})

def df(request):
    sleepy.delay(55)
    cmd="df"
    n=100
    sleep_dur=0
    abc=command1(cmd,n,sleep_dur)
    return render(request,'home.html',{'abc':abc})

#return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

"""
# Create your views here.
def mnfun(request):
    sleepy.delay(10)
    cmd="pwd"
    n=100
    abc=command1(cmd,n)
    return render(request,'home.html',{'abc':abc}) """

def command1(cmd,n,sleep_dur):
    i=0
    d=""
    while i<n:
        abc=os.popen(cmd)
        sleepy(sleep_dur)
        d+="\n"+abc.read()
        i+=1
    return d

def cel_exec(cmd,n,sleep_dur):
    i=0
    d=""
    while i<n:
        abc=os.popen(cmd)
        sleepy.delay(sleep_dur)
        d+="\n"+abc.read()
        i+=1
    return d




# Create your views here.
#def main(request):
 #   return render(request,'main.html')

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