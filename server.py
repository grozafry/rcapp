#Server-side code
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        print("Connected to:" , addr)

        def myListen():
            while True:
                data = conn.recv(1024)
                if data:
                    print('SReceived', repr(data))

        def mySend():
            while True:
                my = input()
                conn.sendall(bytes(my, 'utf-8') )
        

        t1 = threading.Thread(target = myListen)
        t2 = threading.Thread(target = mySend)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("Threads finished")
        
