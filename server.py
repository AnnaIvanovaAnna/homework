from socket import *
import json
import time
import argparse
 
s= socket(AF_INET,SOCK_STREAM)

def create():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--address')
    parser.add_argument ('-p','--port',type=int)

    return parser

if __name__ == '__main__':
    parser = create()
    name= parser.parse_args()

addr,port=None,None

if name.address:
    addr=name.address
else:
    addr=' '
if name.port:
    port=name.port
else:
    port=7777

s.bind((addr,port))
s.listen(2)


while True:
    client, addr_client = s.accept()
    print('Получен запрос на соеднение от' ,str(addr_client))
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
