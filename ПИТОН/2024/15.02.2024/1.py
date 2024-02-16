import threading
import time

def worker_function():
    print("asdkmasd askld  asd")
    n=0
    for i in range(99999999):
        n += i % 3
    print("пака")

thread = threading.Thread(target=worker_function)

thread.start()
print("main potok")
exit()