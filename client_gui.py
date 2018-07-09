from PyQt5 import QtWidgets, uic
import sys
import client_db
import sqlite3
import hashlib

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(r'C:\Users\пользователь\Desktop\welcome.ui')
window_signin= uic.loadUi(r'C:\Users\пользователь\Desktop\signin_form.ui')
window_join= uic.loadUi(r'C:\Users\пользователь\Desktop\join_form.ui')
window_exists=uic.loadUi(r'C:\Users\пользователь\Desktop\login_exists.ui')
window_enter=uic.loadUi(r'C:\Users\пользователь\Desktop\enter.ui')

def sign_click():
    window.close()
    window_signin.show()

def join_click():
    window.close()
    window_join.show()

def exists_close():
    window_exists.close()
    window_join.lineEdit.clear()
    window_join.lineEdit_3.clear()

def enter_close():
    window_enter.close()
    window_join.close()
    window_signin.show()

def save_to_db():
    login=window_join.lineEdit.text()
    password = hashlib.pbkdf2_hmac('sha256', window_join.lineEdit_3.text().encode('utf-8'), b'salt', 100000)
    login_base=[]
    with sqlite3.connect(r'C:\Users\пользователь\Desktop\sqlite\sql_client.sqlite') as conn:
                    cursor = conn.cursor()
                    cursor.execute('select Login_name from Login')
                    result=cursor.fetchall()
                    for i in result:
                        login_base.append(i[0])
                    if login in login_base:
                        window_exists.show()
                        window_exists.pushButton.clicked.connect(exists_close)
                    else:
                        cursor.execute('insert into LogIn (Login_name,Password) values(?,?)',(login,password))
                        conn.commit()
                        cursor.execute('select Login_name,Password from Login')
                        result=cursor.fetchall()
                        window_enter.show()
                        window_enter.pushButton.clicked.connect(enter_close)

def sign_in():
    dic={}
    login=window_signin.lineEdit.text()
    password = hashlib.pbkdf2_hmac('sha256', window_signin.lineEdit_3.text().encode('utf-8'), b'salt', 100000)
    with sqlite3.connect(r'C:\Users\пользователь\Desktop\sqlite\sql_client.sqlite') as conn:
                    cursor = conn.cursor()
                    cursor.execute('select Login_name,Password from LogIn')
                    result=cursor.fetchall()
                    for i in result:
                        dic[i[0]]=i[1]
                    if dic.get(login)!=None:
                        if password==dic.get(login):
                            print('Welcome')
                        else:
                            print('Неверный логин или пароль')
                    else:
                        print('Неверный логин или пароль')


window.show()
window.pushButton.clicked.connect(sign_click)
window.pushButton_2.clicked.connect(join_click)
window_join.pushButton.clicked.connect(save_to_db)
window_signin.pushButton.clicked.connect(sign_in)

sys.exit(app.exec_())





