from socket import *
import json
import time
import argparse
 
s= socket(AF_INET,SOCK_STREAM)

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
    b=' '
if name.port:
    c=name.port
else:
    c=7777

s.bind((b,c))
s.listen(2)


while True:
    client, addr = s.accept()
    print('Получен запрос на соеднение от' ,str(addr))
    message=client.recv(1024)
    if message:
        response_message={
            'response':'Соединение установлено',
            'time':time.ctime(time.time())
            }
    else:
        response_message={
            'response':'Соединение не установлено',
            'time':time.ctime(time.time())
            }
    response_message=json.dumps(response_message)
    client.send(response_message.encode('utf-8'))
    client.close()