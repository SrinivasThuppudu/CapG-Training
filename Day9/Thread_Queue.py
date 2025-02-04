import threading
import queue
import time

def producer(q):
    for i in range(1, 6):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(1)

q = queue.Queue()

producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))
producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)
consumer_thread.join()
print("Thread communication complete")