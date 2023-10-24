"""
    Module comparing the time for I/O tasks executing threads and processes.
    The same is done with CPU bound tasks.
"""

import os
import time
from multiprocessing import Process, current_process
from threading import current_thread, Thread

COUNT = 200000000
SLEEP = 10


def io_bound_task(sec):
    """Function that executes I/O bound tasks"""
    process_id = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{process_id} * {process_name} * {thread_name} \
        ---> Start sleeping...")

    time.sleep(sec)

    print(f"{process_id} * {process_name} * {thread_name} \
        ---> Finished sleeping...")


def cpu_bound_task(n):
    """Function that executes I/O bound tasks"""

    process_id = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{process_id} * {process_name} * {thread_name} \
        ---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{process_id} * {process_name} * {thread_name} \
        ---> Finished counting...")


def io_tasks_with_processes():
    start = time.time()

    # I/O tasks
    io_bound_task(SLEEP)
    io_bound_task(SLEEP)

    # I/O tasks using 2 processes

    p1 = Process(target=io_bound_task, args=(SLEEP,))
    p2 = Process(target=io_bound_task, args=(SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print('Time taken in seconds -', end - start)


def io_tasks_with_threads():
    start = time.time()

    # I/O tasks
    io_bound_task(SLEEP)
    io_bound_task(SLEEP)

    # I/O tasks using 2 threads

    thr1 = Thread(target=io_bound_task, args=(SLEEP,))
    thr2 = Thread(target=io_bound_task, args=(SLEEP,))
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()

    end = time.time()

    print('Time taken in seconds -', end - start)


def cpu_tasks_with_threads():
    start = time.time()

    # CPU tasks
    cpu_bound_task(COUNT)
    cpu_bound_task(COUNT)

    # CPU tasks using 2 threads

    t1 = Thread(target=cpu_bound_task, args=(COUNT,))
    t2 = Thread(target=cpu_bound_task, args=(COUNT,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)


def cpu_tasks_with_processes():
    start = time.time()

    # CPU tasks
    cpu_bound_task(COUNT)
    cpu_bound_task(COUNT)

    # CPU tasks using 2 processes

    pr1 = Process(target=cpu_bound_task, args=(COUNT,))
    pr2 = Process(target=cpu_bound_task, args=(COUNT,))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)


if __name__ == "__main__":

    run_task = int(input("Press 1 to run I/O bound tasks with threads.\n"
                         "Press 2 to run I/O bound tasks with processes.\n"
                         "Press 3 to run CPU bound tasks with threads\n"
                         "Press 4 to run CPU bound tasks with processes\n"
                         "Press 0 to quit.\n"))

    match run_task:
        case 1:
            print('\n I/O bound tasks with threads\n')
            io_tasks_with_threads()
        case 2:
            print('\n I/O bound tasks with processes\n')
            io_tasks_with_processes()
        case 3:
            print('\n CPU bound tasks with threads\n')
            cpu_tasks_with_threads()
        case 4:
            print('\n CPU bound tasks with processes\n')
            cpu_tasks_with_processes()
        case _:
            print('\n Exiting of the program')
            pass
