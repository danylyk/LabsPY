import threading

class RWLock:
    def __init__(self):
        self.rw = 0
        self.write_requests = 0
        self.monitor = threading.Lock()
        self.readers = threading.Condition(self.monitor)
        self.writers = threading.Condition(self.monitor)

    def read_lock (self):
        self.monitor.acquire()
        while self.rw < 0 or self.write_requests:
            self.readers.wait()
        self.rw += 1
        self.monitor.release()        

    def write_lock (self):
        self.monitor.acquire()
        while self.rw != 0:
            self.write_requests += 1
            self.writers.wait()
            self.write_requests -= 1
        self.rw = -1
        self.monitor.release()

    def unlock (self):
        self.monitor.acquire()
        if self.rw < 0:
            self.rw = 0
        else:
            self.rw -= 1
        wake_writers = self.write_requests and self.rw == 0
        wake_readers = self.write_requests == 0
        self.monitor.release()
        if wake_writers:
            self.writers.acquire()
            self.writers.notify()
            self.writers.release()
        elif wake_readers:
            self.readers.acquire()
            self.readers.notifyAll()
            self.readers.release()
        

class Book:
    def __init__ (self):
        self.rwlock = RWLock()

    def read (self):
        self.rwlock.read_lock()
        print("Reading")
        self.rwlock.unlock()

    def write (self):
        self.rwlock.write_lock()
        print("Writing")
        print("Writing.")
        print("Writing..")
        print("Writing...")
        self.rwlock.unlock()

if __name__ == "__main__":
    book = Book()
    t1 = threading.Thread(target=book.write)
    t2 = threading.Thread(target=book.read)
    t1.start();
    t2.start();
    t1.join();
    t2.join();
