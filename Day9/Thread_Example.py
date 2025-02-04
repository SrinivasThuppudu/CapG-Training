import threading
import time

print("Main Thread Execution Started")

def task1():
    print("Sub Task1 Execution Started")
    for i in range(1, 11):
        print(f"Square of {i} is {i * i}")
        time.sleep(1)

def task2():
    print("Sub Task2 Execution Started")
    for i in range(1, 11):
        print(f"Cube of {i} is {i * i * i}")
        time.sleep(1)


th1 = threading.Thread(target = task1)
th1.start()
th2 = threading.Thread(target = task2)
th2.start()
th1.join()
th2.join()
print("Sub Task Execution Completed")
print("Main Thread Execution Completed")