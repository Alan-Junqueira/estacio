#
# ? Implement a solution using Thread.
# * 1- Start a execution of 2 threads.
# * 2- The first thread should calc a number cube.
# * 3- The second thread should calc a number square.
# * 4- Put the first thread to wait 3 seconds, and second thread to wait 2 seconds.
# * 5- Print threads execution order.

from threading import Thread
from time import sleep
from math import pow, sqrt


def calc_cube(waiting_time, number):
    print(f"\nStarting calc_cube")
    sleep(waiting_time)
    print(f"Ending calc_cube")
    value = pow(number, 3)
    print(f"Cube of {number} is {value}")
    return value


def calc_square(waiting_time, number):
    print(f"\nStarting calc_square")
    sleep(waiting_time)
    print(f"Ending calc_square")
    value = sqrt(number)
    print(f"Square of {number} is {value}")
    return value


first_thread = Thread(target=calc_cube, args=(3, 2))
second_thread = Thread(target=calc_square, args=(2, 4))

first_thread.start()
second_thread.start()

print("Waiting for threads to finish.")
first_thread.join()
second_thread.join()
print("Threads finished")
