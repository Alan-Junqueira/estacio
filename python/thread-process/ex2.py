import threading
import time


def func_1():
    for i in range(3):
        print(i, "Executing thread!")
        time.sleep(1)


print('Starting program')
threading.Thread(target=func_1).start()
print("Ending program")
