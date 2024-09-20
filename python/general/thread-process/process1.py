from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []


def func_a(index):
    for i in range(100000):
        minha_lista.append(1)
        print("Termino thread ", index)


def main():
    tarefas = []
    for index in range(10):
        tarefa = Process(target=func_a, args=(index,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))


if __name__ == "__main__":
    main()
