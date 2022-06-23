import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer
import os
import requests

class commandConsumer(WebsocketConsumer):
    
    def connect(self):
        cmd="echo channels working!"
        n=10
        sleep_dur=1
        self.accept()
        d=""
        for i in range(n):
            sleep(sleep_dur)
            output=os.popen(cmd)
            d+="Iteration: "+ f' {i+1} \n'+output.read() +"\n"
            self.send(json.dumps({'output':d}))

    """ 

    self.send(text_data=json.dumps({
            'type': 'connection established',
            'message':'channels connection success'
        })) """

        