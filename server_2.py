from socket import *
import time
import argparse
import select
 
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


def read_msg(client,all_clients):
    try:
        msg=client.recv(1024)
        messg=client.send(msg)
    except:
        print("Клиент {} {} не в сети".format(sock.fileno(), sock.getpeername()))
        all_clients.remove(client)


def mainloop():
    s= socket(AF_INET,SOCK_STREAM)
    s.bind((addr,port))
    s.listen(10)
    s.settimeout(0.2)
    clients=[]
    while True:
        try:
            client, addr_client = s.accept()
            print('Получен запрос на соединение от' ,str(addr_client))
            clients.append(client)
        except OSError as error:
            pass 
        finally:
            wait = 0
            readers = []
            writers = []
            try:
                readers, writers, error = select.select(clients, clients,[], 0)
                print('Пишут:',writers)
            except:
                pass
            for client in clients:
                read_msg(client,clients)
    

print("On!")
mainloop()
