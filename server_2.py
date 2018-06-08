from socket import *
import time
import json
import argparse
import select
import logging
import log_config
 
log = logging.getLogger('server')

class Create():
    def __init__(self):
        pass
    def create(self):
        parser = argparse.ArgumentParser()
        parser.add_argument ('-a','--address')
        parser.add_argument ('-p','--port',type=int)
        return parser
    def get_parser(self):
        parser = self.create()
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
        return addr,port
    def connect(self):
        result=self.get_parser()
        s= socket(AF_INET,SOCK_STREAM)
        s.bind((result[0],result[1]))
        s.listen(10) 
        s.settimeout(0.2)
        return s


class Presense_msg():
    def __init__(self):
        pass
    def get_presense_message(self,client):
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

class Read_msg():
    def __init__(self):
        pass
    def read_msg(self,client,all_clients):
        try:
            msg=client.recv(1024)
            k=1
            for client_r in all_clients:
                if client_r!=client and len(all_clients)>1:
                    messg=client_r.send(msg)
                    print ('Сообщение направлено клиенту',client_r.fileno(), client_r.getpeername())
                    k+=1
                else:
                    pass
            if k==1:
                msg=msg.decode('ascii')
                print('Сообщение получено')
            else:
                pass
        except:
            print("Клиент {} {} не в сети".format(client.fileno(), client.getpeername()))
            all_clients.remove(client)
        return client


class Mainloop():
    def __init__(self):
        pass
    def mainloop(self):
        s=Create().connect()
        clients=[]
        while True:
            try:
                client, addr_client = s.accept()
                Presense_msg().get_presense_message(client)
                print('Получен запрос на соединение от' ,str(addr_client))
                clients.append(client)
            except OSError as error:
                pass 
            finally:
                wait = 0
                readers = []
                writers = []
                try:
                    read=Read_msg()
                    for client in clients:
                        read.read_msg(client,clients)
                        writers.append(client)
                    readers, writers, error = select.select(clients, clients,[], 0)
                    print('Пишут:',writers)
                    print('Слушают:',readers)
                except:
                    pass
    
if __name__ == '__main__':
    print("On!")
    do=Mainloop()
    do.mainloop()
