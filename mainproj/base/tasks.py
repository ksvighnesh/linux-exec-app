from asyncio import subprocess
from celery import shared_task
from time import sleep
from django.shortcuts import render
import os
from celery_progress.backend import ProgressRecorder

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task(bind=True)
def sleeps(self,cmd,n,sleep_dur):
    d=""
    progress_recorder=ProgressRecorder(self)
    for i in range(n):
        sleep(sleep_dur)
        output=os.popen(cmd)
        d+="\n"+output.read()
        progress_recorder.set_progress(i+1,n,f' {d} ')
    return 'Done'



