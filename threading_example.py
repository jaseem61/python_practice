#just a sample program to show threading
import threading
import time

def func():
    for i in range(1,6):
        print(i)
        time.sleep(0.9)

x=threading.Thread(target=func)
x.start()
ls=['a','b','c','d','e']
for x in ls:
    print(x)
    time.sleep(1)

print("the program is finally done!")
