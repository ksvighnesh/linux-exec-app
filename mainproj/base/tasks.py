from celery import shared_task
from time import sleep
from django.shortcuts import render
import os

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def executeCommand():
    sleep(10)
    cmd="ls"
    n=1000
    abc=command1(cmd,n)
    return abc

def command1(cmd,n):
    n=1000
    i=1
    d=""
    while i<n:
        cmd="ls"
        abc=os.popen(cmd)
        d+="\n"+abc.read()
        i+=1
    return d