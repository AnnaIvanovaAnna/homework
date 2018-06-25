from PyQt5 import QtWidgets, uic
import sys
import server_db
import sqlite3

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(r'C:\Users\пользователь\Desktop\server_2.ui')

def load_clients():
    with sqlite3.connect(r'C:\Users\пользователь\Desktop\sqlite\sql.sqlite') as conn:
                    cursor = conn.cursor()
                    cursor.execute('select LogIn from Client')
                    result=cursor.fetchall()
                    for client in result:
                        window.listWidget.addItem(str(client))

def log_in_time():
     with sqlite3.connect(r'C:\Users\пользователь\Desktop\sqlite\sql.sqlite') as conn:
                    cursor = conn.cursor()
                    cursor.execute('select IP_address,Time from ClientHistory')
                    result=cursor.fetchall()
                    for client in result:
                        window.listWidget_3.addItem(str(client))

load_clients()
log_in_time()


window.show()
sys.exit(app.exec_())
