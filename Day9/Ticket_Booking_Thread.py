import threading
import time

class TicketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()

    def book_ticket(self, name):
        with self.lock:
            print(f"{name} has acquired the lock")
            if self.available_tickets > 0:
                print(f"{name} ticket booked successfully")
                self.available_tickets -= 1
            else:
                print("Sorry! No tickets available")
            print(f"{name} has released the lock")

ticket = TicketBooking(1)

threads = []
users = ["ALice", "bob"]

for user in users:
    thread = threading.Thread(target=ticket.book_ticket, args=(user,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()