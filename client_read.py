from socket import *
import json
import time
import argparse

class Create():
    def __init__(self):
        pass
    def create(self):
        parser = argparse.ArgumentParser()
        parser.add_argument ('-a','--address')
        parser.add_argument ('-p','--port',type=int)
        parser.add_argument('-r','--read'), #required=True)
        return parser
    def get_parser(self):
        parser = self.create()
        name= parser.parse_args()
        addr,port=None,None
        if name.address:
            addr=name.address
        else:
            addr='localhost'
        if name.port:
            port=name.port
        else:
            port=7777
        return addr,port

class Presense_msg():
    def __init__(self):
        pass
    def send_presense_message(self,s):
        presense_message={
        'action':'presense',
        'time':time.ctime(time.time()),
        "user": {
            "user_name": "user_name",
            "status": "online" 
            }
        }
        presense_msg =json.dumps(presense_message)
        presense_msg=presense_msg.encode('utf-8')
        s.send(presense_msg)
        response=s.recv(1024)
        response=response.decode('utf-8')
        response=json.loads(response)
        print(response['response'],response['time'])

class Message_client():
    def __init__(self):
        pass
    def message_client(self):
        with socket(AF_INET, SOCK_STREAM) as s: 
            result=Create().get_parser()
            s.connect((result[0],result[1]))
            Presense_msg().send_presense_message(s)
            while True:
                try:
                    resp = s.recv(1024)
                    resp= resp.decode('ascii')
                    print('Ответ:', resp)
                except:
                    print('Error')
        

if __name__ == '__main__':
    do=Message_client()
    do.message_client()
