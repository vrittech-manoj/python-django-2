import time 
from datetime import datetime


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

print("****************without threading********************")

task1()
task2()
task3()


t2 = datetime.now()

# Calculate execution time
execution_time = t2 - t1

total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds")



