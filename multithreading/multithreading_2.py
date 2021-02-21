import threading
import time

def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thread executing")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()

for i in range(1,10):
    time.sleep(2)
    print("main thread is rxecuting")
print(threading.currentThread().getName())