import threading
import time

print("Main Thread Execution Started")

def single_task():
    print('Single Task Execution Started')
    time.sleep(2)
    print('Single Task Execution Completed')

thread = threading.Thread(target=single_task)
thread.start()
thread.join()
print('Main Thread execution completed')