from socket import *
import json
import time
import argparse

s = socket (AF_INET,SOCK_STREAM)

def Create():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--address')
    parser.add_argument ('-p','--port',type=int)

    return parser

if __name__ == '__main__':
    parser = Create()
    name= parser.parse_args()

b,c=None,None

if name.address:
    b=name.address
else:
    b='localhost'
if name.port:
    c=name.port
else:
    c=7777
s.connect((b,c))

presense_message={
    'action':'presense',
    'time':time.ctime(time.time()),
    "user": {
        "user_name": "user_name",
        "status": "online"        }
    }
presense_message=json.dumps(presense_message)
presense_message=presense_message.encode('utf-8')
s.send(presense_message)
response=s.recv(1024)
response=response.decode('utf-8')
response=json.loads(response)
s.close()
print(response['response'],response['time'])
