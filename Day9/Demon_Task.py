import threading
import time

def demon_task():
    while True:
        print("Demon thread running.....")
        time.sleep(1)

demon_thread = threading.Thread(target=demon_task, daemon=True)
demon_thread.start()

time.sleep(10)
print("Main Thread Execution Completed")