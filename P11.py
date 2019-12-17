from contextlib import contextmanager
import threading

class RWLock:
    def __init__(self):
        self.read_requests = 0
        self.readers = threading.Lock()
        self.writers = threading.Lock()

    def read_lock (self):
        self.readers.acquire()
        self.read_requests += 1
        if self.read_requests == 1:
            self.writers.acquire()
        self.readers.release()

    def write_lock (self):
        self.writers.acquire()

    def read_unlock (self):
        assert self.write_requests > 0
        self.readers.acquire()
        self.write_requests -= 1
        if self.write_requests == 0:
            self.writers.release()
        self.readers.release()
        
    def write_unlock (self):
        self.writers.release()
        
    @contextmanager
    def read_locked(self):
        try:
            self.read_lock()
            yield
        finally:
            self.read_unlock()

    @contextmanager
    def write_locked(self):
        try:
            self.write_lock()
            yield
        finally:
            self.write_unlock()
        

class Book:
    def __init__ (self):
        self.rwlock = RWLock()

    def read (self):
        with self.rwlock.read_locked():
            print("Reading")

    def write (self):
        with self.rwlock.write_locked():
            print("Writing")
            print("Writing.")
            print("Writing..")
            print("Writing...")

if __name__ == "__main__":
    book = Book()
    t1 = threading.Thread(target=book.write)
    t2 = threading.Thread(target=book.read)
    t1.start();
    t2.start();
    t1.join();
    t2.join();
