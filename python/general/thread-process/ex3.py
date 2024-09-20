import threading
import time


def func_1(message):
    for i in range(3):
        print(i, message)
        time.sleep(1)


print('Starting program')
x = threading.Thread(target=func_1, args=("Executing!",))
x.start()
print("Ending program")
