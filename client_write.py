from socket import *
import json
import time
import argparse

def create():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--address')
    parser.add_argument ('-p','--port',type=int)
    parser.add_argument('-w','--write', required=True)

    return parser

if __name__ == '__main__':
    parser = create()
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


def message_client():
    with socket(AF_INET, SOCK_STREAM) as s: 
        s.connect((addr,port))
        while True:
            message = input('Введите сообщение: ')
            if message ==' ':
                break
            s.send(message.encode('ascii'))     
            response = s.recv(1024)
            response= response.decode('ascii')
            print('Ответ:', response)

if __name__ == '__main__':
    message_client()