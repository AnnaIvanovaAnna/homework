from socket import *
import json
import time
import argparse
import sqlite3

class Create():
    def __init__(self):
        pass
    def create(self):
        parser = argparse.ArgumentParser()
        parser.add_argument ('-a','--address')
        parser.add_argument ('-p','--port',type=int)
        parser.add_argument('-w','--write')
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
   


class Send_msg():
    def __init__(self):
        pass
    def send_presense_message(self,s,message):
        presense_message={
        'action':message,
        'time':time.ctime(time.time()),
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
            Send_msg().send_presense_message(s,'presense')
            while True:
                message = input('Введите сообщение: ')
                with sqlite3.connect(r'C:\Users\пользователь\Desktop\sqlite\sql_client.sqlite') as conn:
                    cursor = conn.cursor()
                    cursor.execute('insert into MessageHistory (Msg) values (?)',(str(message),))
                    conn.commit()
                if message ==' ':
                    break
                s.send(message.encode('ascii'))     

if __name__ == '__main__':
    do=Message_client()
    do.message_client()