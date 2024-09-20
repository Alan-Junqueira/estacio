from threading import Thread
from multiprocessing import Process


def func_a(nome):
    print(nome)


def main():
    t = Thread(target=func_a, args=("Minha Thread",))
    t.start()

    p = Process(target=func_a, args=("Meu Processo",))
    p.start()


if __name__ == '__main__':
    main()
