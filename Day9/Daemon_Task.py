import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running.....")
        time.sleep(1)

daemon_thread = threading.Thread(target=daemon_task, daemon=True)
daemon_thread.start()

time.sleep(10)
print("Main Thread Execution Completed")
