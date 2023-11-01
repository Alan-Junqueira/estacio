from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []


def func_a(index):
    for i in range(100000):
        minha_lista.append(1)
        print("Termino thread ", index)


tasks = []


def main():
    for index in range(10):
        task = Thread(target=func_a, args=(index,))
        tasks.append(task)
        task.start()


print("Antes de aguardar o termino!", len(minha_lista))

for task in tasks:
    task.join()

print("Após aguardar o termino!", len(minha_lista))

if __name__ == "__main__":
    main()
