import time
import threading

def sayhai(name):
    for _ in range(5):
        time.sleep(0.2)
        print("Hai\n")

def sayhello(name):
    for _ in range(5):
        time.sleep(0.2)
        print("Hello\n")

w1="E"
w2="W"
t1=threading.Thread(target=sayhai,args=w1)
t2=threading.Thread(target=sayhello,args=w2)

t1.start()
t2.start()

t1.join()
t2.join()

print("exit")