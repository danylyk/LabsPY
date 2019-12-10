import threading

class RWLock:
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.write_requests = 0

    def read_lock (self):
        while self.writers > 0 or self.write_requests > 0 : pass
        self.readers += 1

    def read_unlock (self):
        self.readers -= 1

    def write_lock (self):
        self.write_requests += 1
        while self.readers > 0 or self.writers > 0 : pass
        self.write_requests -= 1
        self.writers += 1

    def write_unlock (self):
        self.writers -= 1

class Book:
    def __init__ (self):
        self.rwlock = RWLock()

    def read (self):
        self.rwlock.read_lock()
        print("Reading")
        self.rwlock.read_unlock()

    def write (self):
        self.rwlock.write_lock()
        print("Writing")
        print("Writing.")
        print("Writing..")
        print("Writing...")
        self.rwlock.write_unlock()

if __name__ == "__main__":
    book = Book()
    t1 = threading.Thread(target=book.write)
    t2 = threading.Thread(target=book.read)
    t1.start();
    t2.start();
    t1.join();
    t2.join();