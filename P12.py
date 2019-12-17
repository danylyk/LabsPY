import os
import hashlib
import threading
import math

class FilesInDirectory:
    def __init__ (self, dir:str):
        self.dir = dir
        self.duplicates = {}
        self.duplicates_pos = []
        self.files_list = []

        self.__files_from_dir()

    def __files_from_dir (self):
        for dir in os.walk(self.dir):
            for i in dir[2]:
                self.files_list.append(dir[0]+"/"+i)

    def get_duplicates (self, n):
        files_shift = math.ceil(len(self.files_list)/n)
        files_start = -files_shift
        threads = []

        while True:
            files_start += files_shift
            files_end = files_start+files_shift
            if files_end > len(self.files_list): 
                files_end = len(self.files_list)
            t = threading.Thread(target=self.__get_duplicates_proccess, args=[files_start, files_end, 65536])
            t.start()
            threads.append(t)
            if files_end == len(self.files_list): break

        for t in threads:
            t.join()

        res = []
        for i in self.duplicates_pos:
            res.append(self.duplicates[i])

        return res

    def __get_duplicates_proccess (self, files_start, files_end, chunk_size):
        for i in range(files_start, files_end):
            hasher = hashlib.md5()
            with open(self.files_list[i], 'rb') as file:
                buf = file.read(chunk_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(chunk_size)
            file.close()
            data = hasher.hexdigest()
            try:
                self.duplicates[data].append(self.files_list[i])
                if len(self.duplicates[data]) == 2: # If file has already existed in dictionary
                    self.duplicates_pos.append(data)

            except: self.duplicates[data] = [self.files_list[i]]


if __name__ == '__main__':
    dir = FilesInDirectory("C:/Users/webvi/OneDrive/Documents/GitHub/")
    print(dir.get_duplicates(20))
