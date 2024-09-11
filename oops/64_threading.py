import time 
from datetime import datetime

import threading


def task1():
    print("Task 1 started")
    time.sleep(2)

def task2():
    print("Task 2 started")
    time.sleep(2)

def task3():
    print("Task 3 started")
    time.sleep(2)

t1 = datetime.now()
print("****************with threading********************")

task_1 = threading.Thread(target=task1)
task_2 = threading.Thread(target=task2)
task_3 = threading.Thread(target=task3)

task_1.start()
task_2.start()
task_3.start()

task_1.join()
task_2.join()
task_3.join()


t2 = datetime.now()

# Calculate execution time
execution_time = t2 - t1

total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds")



