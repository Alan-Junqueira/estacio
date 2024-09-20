#
# ? Implement a solution using Thread.
# * 1- Start a execution of 2 threads.
# * 2- Put the thread wait, the first should wait 3 seconds, the second should wait 2 seconds .
# * 3- Print threads execution order.

from threading import Thread
from time import sleep

def task(waiting_time, message):
    print(f"\nStarting task {message}")
    sleep(waiting_time)
    print(f"Ending task {message}")

first_thread = Thread(target=task, args=(3, "First thread executing."))
second_thread = Thread(target=task, args=(2, "Second thread executing."))

first_thread.start()
second_thread.start()

print("Waiting for threads to finish.")
first_thread.join()
second_thread.join()
print("Threads finished")

# ? Solution - The solution is similar