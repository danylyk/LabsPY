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
