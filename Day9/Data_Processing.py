import threading
import time

print("Main Thread Execution Started")

print("Sub Task Execution Started")
def calculate_sum(chunk):
    print(f"Sum of chunk {chunk} is {sum(chunk)}")
    time.sleep(2)

chunks = [
    list(range(1, 101)),
    list(range(101, 10001)),
    list(range(1, 100000))
]

threads = []

for chunk in chunks:
    thread = threading.Thread(target=calculate_sum, args=(chunk,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Sub Task Execution Completed")
print("Main Thread Execution Completed")