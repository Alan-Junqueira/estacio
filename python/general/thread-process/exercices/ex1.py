#
# ? Implement a solution using Thread.
# * 1- Start a thread execution.
# * 2- Put the thread to sleep for 2 second.
# * 3- Print the start and end of thread execution.

import threading
import time


def thread_function():
    print("Task start")
    time.sleep(2)
    print("Task end")


thread = threading.Thread(target=thread_function)
thread.start()
print("Waiting for thread to finish.")
thread.join()
print("Thread finished")

# ? Solution


def task(waiting_time, message):
    print(f"\nStarting task {message}")
    time.sleep(waiting_time)
    print(f"Ending task {message}")


ex_thread = threading.Thread(target=task, args=(2, "Thread executing."))

ex_thread.start()
print("Waiting for thread to finish.")
ex_thread.join()
print("Thread finished")
