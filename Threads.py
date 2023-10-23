""" Creating Threads using threading module"""

import threading
import os


def my_task1():
    """ Creating task to be assigned to the thread """

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def my_task2():
    """ Creating task to be assigned to the thread """

    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    thr1 = threading.Thread(target=my_task1, name='thr1')
    thr2 = threading.Thread(target=my_task2, name='thr2')

    # starting threads
    thr1.start()
    thr2.start()

    # wait until all threads finish
    thr1.join()
    thr2.join()
