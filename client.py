import socket
import os
import threading

HOST = '127.0.0.1'
PORT = 65432




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    def myListen():
        while True:
            data = s.recv(1024)
            if data:
                print('Received', repr(data))

    def mySend():
        while True:
            my = input()
            s.sendall(bytes(my, 'utf-8') )
    

    t1 = threading.Thread(target = myListen)
    t2 = threading.Thread(target = mySend)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threads finished")
   

